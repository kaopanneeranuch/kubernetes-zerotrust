import http from 'k6/http';
import { check, group } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 1000 },
    { duration: '1m', target: 1000 },
    { duration: '30s', target: 0 },
  ],
};

const token = "<keycloak-token>";

export default function () {
  const params = { headers: { Authorization: `Bearer ${token}` } };

  group('cluster1', () => {
    const res = http.get('http://34.131.93.218/api/external-data', params);
    check(res, { 'status is 200': (r) => r.status === 200 });
  });

  group('cluster2', () => {
    const res = http.get('http://35.244.51.99/api/external-data', params);
    check(res, { 'status is 200': (r) => r.status === 200 });
  });
}