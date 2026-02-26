# AfyaPulse 🇰🇪
> Real-time disease surveillance bridging the gap between USSD and AI.

## 🚀 Quick Start
To get this project running locally:

1. **Clone the repo:**
   `git clone https://github.com/domminique/AfyaPulse.git`
   `cd AfyaPulse`

2. **Set up Virtual Environment:**
   `python -m venv venv`
   `source venv/bin/activate`  # On Windows: venv\Scripts\activate

3. **Install Dependencies:**
   `pip install -r requirements.txt`

4. **Configuration:**
   Copy `.env.example` to `.env` and add your **Elastic Cloud ID** and **API Key**.

5. **Run:**
   `python app.py`

## 🛠️ Built With
- **Elasticsearch:** Vector storage and real-time data indexing.
- **Kibana:** Geospatial heatmaps and AI Agent Builder (RAG).
- **Africa's Talking:** USSD Gateway for last-mile connectivity.
- **Flask:** Lightweight backend for USSD callbacks.

## 🧠 Technical Architecture
AfyaPulse uses a **RAG (Retrieval-Augmented Generation)** pattern. When a CHP sends a USSD report, it is enriched via an Elastic Ingest Pipeline and stored. Our **AI Agent** then queries this index to provide epidemiological insights.

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
