from prometheus_client import Counter

REQUEST_COUNT = Counter('predict_requests_total', 'Total predict requests')
