import logging
from datetime import datetime

from flask import Flask, redirect
app = Flask(__name__)

HTTP_STATUS_OK = 200

# Disable werkzeug logging for this exercise.
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt = '%m-%d %H:%M',
                    filename = 'app.log',
                    filemode = 'w')

accessLogger = logging.getLogger('app.endpoint.access')

@app.route("/")
def index():
    accessLog("REDIRECT /")
    return redirect('/status')

@app.route("/status")
def status():
    accessLog("status")
    return {
        "result": "OK - healthy"
    }, HTTP_STATUS_OK

@app.route("/metrics")
def metrics():
    accessLog("metrics")
    return { "data" : {
        "UserCount": 100,
        "UserCountActive": 17
    }}, HTTP_STATUS_OK

def accessLog(endpointName):
    timeStamp = datetime.now().strftime("%H:%M:%S")
    accessLogger.debug(f"Endpoint {endpointName} accessed.")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
