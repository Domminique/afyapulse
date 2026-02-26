from flask import Flask, request, make_response
from elasticsearch import Elasticsearch
import datetime
import os
import random
from dotenv import load_dotenv

# Load variables
load_dotenv()

app = Flask(__name__)

# Connect to Elastic Cloud
ELASTIC_CLOUD_ID = os.environ.get("ELASTIC_CLOUD_ID")
ELASTIC_API_KEY = os.environ.get("ELASTIC_API_KEY")

es = Elasticsearch(
    cloud_id=ELASTIC_CLOUD_ID,
    api_key=ELASTIC_API_KEY
)

KAKAMEGA_HUBS = [
    {"name": "Lurambi", "lat": 0.2827, "lon": 34.7519},
    {"name": "Butere", "lat": 0.1456, "lon": 34.4856},
    {"name": "Mumias", "lat": 0.3344, "lon": 34.4892},
    {"name": "Malava", "lat": 0.4433, "lon": 34.8550},
    {"name": "Shinyalu", "lat": 0.2117, "lon": 34.8450}
]

@app.route('/ussd', methods=['POST'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")

    if text == "":
        response = "CON AfyaPulse: Rural Surveillance\n1. Human Health Issue\n2. Animal Health Issue"
    elif text == "1":
        response = "CON Select Symptom:\n1. Fever\n2. Rash\n3. Cough"
    elif text == "2":
        response = "CON Animal Health:\n1. Unusual death\n2. Sudden sickness"
    else:
        # Data Ingestion
        hub = random.choice(KAKAMEGA_HUBS)
        doc = {
            "session_id": session_id,
            "phone": phone_number,
            "raw_input": text,
            "channel": "ussd",
            "timestamp": datetime.datetime.now().isoformat(),
            "location_code": hub["name"],
            "location": {
                "lat": hub["lat"] + random.uniform(-0.02, 0.02),
                "lon": hub["lon"] + random.uniform(-0.02, 0.02)
            }
        }
        
        try:
            es.index(index="health-reports", document=doc, pipeline="disease-triage-pipeline")
            response = f"END Report received for {hub['name']}.\nAI Triage is notifying the Sub-County Officer."
        except Exception as e:
            print(f"Elastic Error: {e}")
            response = "END Connection error. Please try again later."

    return make_response(response, 200, {'Content-Type': 'text/plain'})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)