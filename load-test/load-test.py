import subprocess
import time
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to run Apache Benchmark (`ab`) with concurrency and number of requests
def run_ab_benchmark(url, token, concurrency, num_requests):
    ab_command = [
        'ab', 
        '-c', str(concurrency),  # concurrency level
        '-n', str(num_requests),  # total number of requests
        '-H', f'Authorization: Bearer {token}',  # JWT token in header
        url
    ]
    
    result = subprocess.run(ab_command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Results for URL: {url}")
        print(result.stdout)  # Print the raw Apache Benchmark result
        return parse_ab_results(result.stdout)
    else:
        print(f"Error running Apache Benchmark for {url}: {result.stderr}")
        return None

# Function to parse Apache Benchmark results
def parse_ab_results(output):
    results = {}
    for line in output.splitlines():
        if 'Requests per second' in line:
            results['requests_per_second'] = float(line.split(':')[1].strip().split()[0])
        if 'Time per request' in line:
            results['time_per_request'] = float(line.split(':')[1].strip().split()[0])
        if 'Failed requests' in line:
            results['failed_requests'] = int(line.split(':')[1].strip())
        if 'Transfer rate' in line:
            results['transfer_rate'] = float(line.split(':')[1].strip().split()[0])
    return results

# Function to compare performance of two URLs
def compare_performance(url1, url2, concurrency, num_requests, token):
    # Run benchmark for URL 1
    print(f"Running benchmark for URL 1 ({url1})...")
    result1 = run_ab_benchmark(url1, token, concurrency, num_requests)

    # Run benchmark for URL 2
    print(f"Running benchmark for URL 2 ({url2})...")
    result2 = run_ab_benchmark(url2, token, concurrency, num_requests)

    # Visualize the comparison if both results are available
    if result1 and result2:
        labels = ['Requests per second', 'Time per request (ms)', 'Failed requests', 'Transfer rate (Kbytes/sec)']
        url1_values = [result1['requests_per_second'], result1['time_per_request'], result1['failed_requests'], result1['transfer_rate']]
        url2_values = [result2['requests_per_second'], result2['time_per_request'], result2['failed_requests'], result2['transfer_rate']]

        # Create a window for Requests per second
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        ax1.bar([0], result1['requests_per_second'], label='1 Gateway')
        ax1.bar([1], result2['requests_per_second'], label='3 Gateways')
        ax1.set_title('Requests per second Comparison', fontsize=14)
        ax1.set_ylabel('Requests per second', fontsize=12)
        ax1.set_xticks([0, 1])
        ax1.set_xticklabels(['1 Gateway', '3 Gateways'], fontsize=12)
        ax1.legend()

        # Add value labels on top of bars
        ax1.text(0, result1['requests_per_second'] + 0.1, f'{result1["requests_per_second"]:.2f}', ha='center', va='bottom')
        ax1.text(1, result2['requests_per_second'] + 0.1, f'{result2["requests_per_second"]:.2f}', ha='center', va='bottom')

        # Adjust layout for better spacing
        # plt.tight_layout()
        plt.show()

        # Create a window for Time per request
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        ax2.bar([0], result1['time_per_request'], label='1 Gateway')
        ax2.bar([1], result2['time_per_request'], label='3 Gateways')
        ax2.set_title('Time per request Comparison', fontsize=14)
        ax2.set_ylabel('Time per request (ms)', fontsize=12)
        ax2.set_xticks([0, 1])
        ax2.set_xticklabels(['1 Gateway', '3 Gateways'], fontsize=12)
        ax2.legend()

        # Add value labels on top of bars
        ax2.text(0, result1['time_per_request'] + 50, f'{result1["time_per_request"]:.2f}', ha='center', va='bottom')
        ax2.text(1, result2['time_per_request'] + 50, f'{result2["time_per_request"]:.2f}', ha='center', va='bottom')

        # Adjust layout for better spacing
        # plt.tight_layout()
        plt.show()

# Main function
def main():
    service = 'external-cloud-service-1'

    if service == 'internal-api-service-1':
        url1 = 'http://localhost:8888/api/data'
        url2 = 'http://localhost:8889/api/data'
    elif service == 'internal-api-service-2':
        url1 = 'http://localhost:8888/api/report'
        url2 = 'http://localhost:8889/api/report'
    elif service == 'external-cloud-service-1':
        url1 = 'http://34.131.93.218/api/external-data'
        url2 = 'http://35.244.51.99/api/external-data'
    elif service == 'external-cloud-service-2':
        url1 = 'http://34.131.93.218/api/external-report'
        url2 = 'http://35.244.51.99/api/external-report'

    token = "your_jwt_token_here"  # Replace with your actual JWT token
    concurrency = 100
    num_requests = 100

    compare_performance(url1, url2, concurrency, num_requests, token)

if __name__ == '__main__':
    main()