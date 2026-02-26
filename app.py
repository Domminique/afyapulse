# from flask import Flask, request, make_response
# from elasticsearch import Elasticsearch
# import datetime
# import os
# from dotenv import load_dotenv

# # Load variables locally or from Render environment
# load_dotenv()

# app = Flask(__name__)

# # 1. Connect to Elastic Cloud using Environment Variables
# ELASTIC_CLOUD_ID = os.environ.get("ELASTIC_CLOUD_ID")
# ELASTIC_API_KEY = os.environ.get("ELASTIC_API_KEY")

# if not ELASTIC_CLOUD_ID or not ELASTIC_API_KEY:
#     print("❌ CRITICAL: Missing Elastic Cloud credentials!")

# es = Elasticsearch(
#     cloud_id=ELASTIC_CLOUD_ID,
#     api_key=ELASTIC_API_KEY
# )

# @app.route('/ussd', methods=['POST'])
# def ussd_callback():
#     session_id = request.values.get("sessionId", None)
#     phone_number = request.values.get("phoneNumber", None)
#     text = request.values.get("text", "")

#     # 2. USSD Navigation Logic
#     if text == "":
#         response = "CON Welcome to Sentinel-Pulse\n"
#         response += "1. Report Human Symptoms\n"
#         response += "2. Report Animal Health Issue"
#     elif text == "1":
#         response = "CON What is the primary symptom?\n"
#         response += "1. Fever\n"
#         response += "2. Rash\n"
#         response += "3. Cough"
#     elif text == "2":
#         response = "CON Animal Health: What did you observe?\n"
#         response += "1. Unusual livestock death\n"
#         response += "2. Sudden illness in cattle"
#     else:
#         # 3. Final Input - Send to Elastic Inference Pipeline
#         doc = {
#             "session_id": session_id,
#             "phone": phone_number,
#             "raw_input": text,
#             "channel": "ussd",
#             "timestamp": datetime.datetime.now().isoformat(),
#             "location_code": "KE-01" 
#         }
        
#         try:
#             # The 'pipeline' parameter tells Elastic to run our Risk-Triage logic
#             es.index(
#                 index="health-reports", 
#                 document=doc, 
#                 pipeline="disease-triage-pipeline"
#             )
#             # We use a smart response to show the user the AI is working
#             response = "END Thank you. Your report has been received and triaged by our AI Agent."
#         except Exception as e:
#             print(f"Elastic Error: {e}")
#             response = "END System error. We are working on it."

#     return make_response(response, 200, {'Content-Type': 'text/plain'})

# if __name__ == '__main__':
#     # Bind to Render's dynamic port
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)

from flask import Flask, request, make_response
from elasticsearch import Elasticsearch
import datetime
import os
<<<<<<< HEAD
import random  # <--- CRITICAL: Don't miss this
=======
import random
>>>>>>> d8905dee9486246516e09b095a0d2a18772c7247
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

<<<<<<< HEAD
# Connect to Elastic
=======
# 1. Connect to Elastic Cloud using Environment Variables
ELASTIC_CLOUD_ID = os.environ.get("ELASTIC_CLOUD_ID")
ELASTIC_API_KEY = os.environ.get("ELASTIC_API_KEY")

>>>>>>> d8905dee9486246516e09b095a0d2a18772c7247
es = Elasticsearch(
    cloud_id=os.environ.get("ELASTIC_CLOUD_ID"),
    api_key=os.environ.get("ELASTIC_API_KEY")
)

<<<<<<< HEAD
=======
# Kakamega Coordinate Mapping for the Map "Money Shot"
# If we don't know the exact village, we pick a random hub in Kakamega
>>>>>>> d8905dee9486246516e09b095a0d2a18772c7247
KAKAMEGA_HUBS = [
    {"name": "Lurambi", "lat": 0.2827, "lon": 34.7519},
    {"name": "Butere", "lat": 0.1456, "lon": 34.4856},
    {"name": "Mumias", "lat": 0.3344, "lon": 34.4892},
    {"name": "Malava", "lat": 0.4433, "lon": 34.8550}
]

@app.route('/ussd', methods=['POST'])
def ussd_callback():
<<<<<<< HEAD
    session_id = request.values.get("sessionId")
    phone_number = request.values.get("phoneNumber")
=======
    # Africa's Talking POST data
    session_id = request.values.get("sessionId", None)
    phone_number = request.values.get("phoneNumber", None)
>>>>>>> d8905dee9486246516e09b095a0d2a18772c7247
    text = request.values.get("text", "")

    if text == "":
<<<<<<< HEAD
        response = "CON AfyaPulse: Rural Surveillance\n1. Human Issue\n2. Animal Issue"
    elif text == "1":
        response = "CON Symptoms:\n1. Fever\n2. Rash\n3. Cough"
    elif text == "2":
        response = "CON Animal:\n1. Unusual death\n2. Sickness"
    else:
        hub = random.choice(KAKAMEGA_HUBS)
=======
        # Main Menu
        response = "CON AfyaPulse: Rural Surveillance\n"
        response += "1. Human Health Issue\n"
        response += "2. Animal Health Issue"
    
    elif text == "1":
        # Sub-menu Human
        response = "CON Select Primary Symptom:\n"
        response += "1. Fever\n"
        response += "2. Rash\n"
        response += "3. Respiratory/Cough"
        
    elif text == "2":
        # Sub-menu Animal
        response = "CON Animal Health Observation:\n"
        response += "1. Unusual death (Immediate alert)\n"
        response += "2. Sudden sickness/Lethargy"

    else:
        # 3. Data Ingestion - This executes when a user finishes a choice (e.g., '1*1' or '2*1')
        
        # Pick a location hub for the demo (simulating user location)
        location_hub = random.choice(KAKAMEGA_HUBS)
        
>>>>>>> d8905dee9486246516e09b095a0d2a18772c7247
        doc = {
            "session_id": session_id,
            "phone": phone_number,
            "raw_input": text, # This will be '1*1', '2*1', etc.
            "channel": "ussd",
            "timestamp": datetime.datetime.now().isoformat(),
<<<<<<< HEAD
            "location_code": hub["name"],
            "location": {
                "lat": hub["lat"] + random.uniform(-0.02, 0.02),
                "lon": hub["lon"] + random.uniform(-0.02, 0.02)
=======
            "location_code": location_hub["name"],
            "location": {
                "lat": location_hub["lat"] + random.uniform(-0.02, 0.02),
                "lon": location_hub["lon"] + random.uniform(-0.02, 0.02)
>>>>>>> d8905dee9486246516e09b095a0d2a18772c7247
            }
        }
        try:
<<<<<<< HEAD
            es.index(index="health-reports", document=doc, pipeline="disease-triage-pipeline")
            response = f"END Report received for {hub['name']}. AI Agent is triaging."
        except Exception as e:
            response = "END System busy. Please try again."
=======
            # Trigger the AI Triage Pipeline
            es.index(
                index="health-reports", 
                document=doc, 
                pipeline="disease-triage-pipeline"
            )
            response = f"END Report received for {location_hub['name']}.\nAI Triage is notifying the Sub-County Officer."
        except Exception as e:
            print(f"Elastic Error: {e}")
            response = "END Connection error. Please try again later."
>>>>>>> d8905dee9486246516e09b095a0d2a18772c7247

    # Africa's Talking requires a 200 OK with 'text/plain'
    return make_response(response, 200, {'Content-Type': 'text/plain'})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)