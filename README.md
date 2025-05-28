# Kubernetes Zero Trust

This project demonstrates how to implement Zero Trust security principles in a Kubernetes environment using Istio, Keycloak, and RBAC for secure communication.

## Features

- Zero Trust network policies with Istio
- Secure service-to-service communication (mTLS)
- Authentication and authorization using Keycloak (OIDC/JWT)
- Fine-grained RBAC with Istio AuthorizationPolicy
- Example manifests and configurations for internal and external services
- Load testing and monitoring setup Apache Benchmark (ab) and Python script for performance comparison

## Project Structure

- `external-cloud-service-1/` and `external-cloud-service-2/`: Example Node.js services simulating external cloud APIs
- `internal-api-service-1/` and `internal-api-service-2/`: Example Python Flask APIs for internal services
- `istio/`: Istio Gateway, PeerAuthentication (mTLS), and HPA manifests
- `keycloak/`: Keycloak realm export for authentication/authorization
- `kube-api-server/`: Example RBAC manifests for Kubernetes API server access
- `load-test/`: Load testing scripts

## Prerequisites

- Kubernetes cluster (v1.20+ recommended)
- kubectl installed and configured
- Istio installed in your cluster
- Keycloak instance
- Docker (for local load testing)

## Getting Started

1. **Set up Istio:**
    - Install Istio with the default profile:
      ```
      istioctl install --set profile=default -y
      ```
    - Enable automatic sidecar injection for the `default` namespace:
      ```
      kubectl label namespace default istio-injection=enabled
      ```

2. **Clone the repository:**
    ```
    git clone https://github.com/kaopanneeranuch/kubernetes-zerotrust.git
    cd kubernetes-zerotrust
    ```

3. **Review and apply the manifests:**
    - Istio setup:  
      ```
      kubectl apply -f istio/
      ```
    - Deploy internal and external services:  
      ```
      kubectl apply -f internal-api-service-1/
      kubectl apply -f internal-api-service-2/
      kubectl apply -f external-cloud-service-1/
      kubectl apply -f external-cloud-service-2/
      ```
    - Apply Keycloak and RBAC configs as needed.

4. **Set up Keycloak:**
    - Import the realm from `keycloak/realm-export.json` into your Keycloak instance.
    - Update service endpoints and secrets as needed.

5. **Run Load Tests (optional):**
    - Use the Python script in `load-test/load-test.py` for benchmarking and performance comparison.
    - This script uses [Apache Benchmark (ab)](https://httpd.apache.org/docs/2.4/programs/ab.html) to generate HTTP load and measure service performance.
    - **Requirements:**  
      - Python 3.x  
      - `matplotlib` Python package (install with `pip install matplotlib`)  
      - [Apache Benchmark (ab)](https://httpd.apache.org/docs/2.4/programs/ab.html) must be installed and available in your system PATH.
    - You can configure the concurrency level and number of requests by editing the `concurrency` and `num_requests` variables in `load-test.py`.
    - Example usage:
      ```
      cd load-test
      python load-test.py
      ```
    - Edit `load-test.py` to set the correct URLs and Keycloak token for your services.
    - The script will run benchmarks and visualize the results for easy comparison.

6. **kube-api-server (optional):**
    - The `kube-api-server/` directory contains RBAC manifests (such as `internal-api-1-rbac.yaml` and `internal-api-2-rbac.yaml`) for configuring Kubernetes API server access.
    - These manifests can be used to compare the performance and security posture of a standard Kubernetes cluster (without a service mesh) against a cluster with Istio service mesh enabled.
    - Apply the RBAC manifests as needed to test and benchmark access control and performance in both scenarios.
    - To enable OIDC authentication and RBAC on your Kubernetes API server, configure the following flags in your API server startup options:
      ```
      --authorization-mode=Node,RBAC
      --oidc-issuer-url=https://keycloak.neeranuchj.org/realms/kubernetes-zerotrust
      --oidc-client-id=account
      --oidc-username-claim=preferred_username
      --oidc-groups-claim=realm_access.roles
      --oidc-signing-algs=RS256
      ```
    - These settings integrate Keycloak as the OIDC provider for authentication and enable RBAC for fine-grained access control.

## Documentation

- [Zero Trust Architecture (NIST)](https://csrc.nist.gov/publications/detail/sp/800-207/final)
- [Istio Security Concepts](https://istio.io/latest/docs/concepts/security/)
- [Keycloak Documentation](https://www.keycloak.org/documentation)