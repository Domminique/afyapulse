import random
import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Mapping Kakamega sub-counties to real GPS coordinates
# These points center on the main hubs of each sub-county
kakamega_coords = {
    "Lurambi": {"lat": 0.2827, "lon": 34.7519},
    "Malava": {"lat": 0.4433, "lon": 34.8550},
    "Butere": {"lat": 0.1456, "lon": 34.4856},
    "Mumias West": {"lat": 0.3344, "lon": 34.4892},
    "Shinyalu": {"lat": 0.2117, "lon": 34.8450},
    "Ikolomani": {"lat": 0.1450, "lon": 34.7433},
    "Lugari": {"lat": 0.5833, "lon": 34.9500}
}

# Use your actual credentials here
ELASTIC_CLOUD_ID = "My_Elasticsearch_project:dXMtY2VudHJhbDEuZ2NwLmVsYXN0aWMuY2xvdWQkYWY4M2E0NWQ4MzEzNGE1MjljOGRkM2M2N2JhOTJhNzUuZXMkYWY4M2E0NWQ4MzEzNGE1MjljOGRkM2M2N2JhOTJhNzUua2I="
ELASTIC_API_KEY = "WmJrNWdKd0I4eWxCaWM5Y1RKM1o6NG0tZGxKRElIQlR3MlVLY2J6U3RKQQ=="

es = Elasticsearch(cloud_id=ELASTIC_CLOUD_ID, api_key=ELASTIC_API_KEY)

def generate_mock_data(n=60):
    actions = []
    sub_counties = list(kakamega_coords.keys())
    # 1*1=Fever, 1*2=Rash, 1*3=Cough, 2*1=Animal Death (Critical), 2*2=Sick Cattle
    symptoms = ["1*1", "1*2", "1*3", "2*1", "2*2"]

    for i in range(n):
        county = random.choice(sub_counties)
        coords = kakamega_coords[county]
        
        # Increased jitter (0.05) to simulate spread across rural terrain
        lat = coords["lat"] + random.uniform(-0.05, 0.05)
        lon = coords["lon"] + random.uniform(-0.05, 0.05)

        doc = {
            "_index": "health-reports",
            "_source": {
                "session_id": f"rural_mock_{i}",
                "phone": f"+2547{random.randint(10000000, 99999999)}",
                "raw_input": random.choice(symptoms),
                "location": {"lat": lat, "lon": lon},
                "location_code": county,
                "timestamp": (datetime.datetime.now() - datetime.timedelta(hours=random.randint(0, 48))).isoformat(),
                "region": "Kakamega County"
            },
            "pipeline": "disease-triage-pipeline"
        }
        actions.append(doc)
    
    success, _ = bulk(es, actions)
    print(f"✅ Success! Injected {success} rural reports in Kakamega.")

if __name__ == "__main__":
    generate_mock_data(60)




