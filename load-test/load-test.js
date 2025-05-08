import http from 'k6/http';
import { check, group } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 500 },
    { duration: '1m', target: 500 },
    { duration: '30s', target: 0 },
  ],
};

const token = "keycloak-token"; // Replace with your actual token

export default function () {
  const params = { headers: { Authorization: `Bearer ${token}` } };

  group('single_gateway', () => {
    const res = http.get('http://localhost:8888/api/data', params);
    check(res, { 'status is 200': (r) => r.status === 200 });
  });

  group('three_gateways', () => {
    const res = http.get('http://localhost:8889/api/data', params);
    check(res, { 'status is 200': (r) => r.status === 200 });
  });
}
