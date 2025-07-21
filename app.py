from flask import Flask
import random
from prometheus_client import Counter, generate_latest
from flask import Response

app = Flask(__name__)

# Create Prometheus counters
REQUEST_COUNT = Counter('request_count', 'Total requests')
ERROR_COUNT = Counter('error_count', 'Total errors')

@app.route('/')
def index():
    REQUEST_COUNT.inc()
    if random.random() < 0.3:
        ERROR_COUNT.inc()
        return "❌ Simulated error", 500
    return "✅ Success"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run()
