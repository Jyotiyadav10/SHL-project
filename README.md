# SHL Assessment Recommendation System  
A semantic search–based recommendation engine that suggests the most relevant SHL assessments based on a job description, natural language query, or JD URL.

This system uses:
- **Sentence Transformers** for embedding job descriptions  
- **FAISS** for fast vector similarity search  
- **FastAPI** for serving recommendations via API  
- **Python scripts** for scraping, cleaning and ingesting SHL product catalog  

---

## 🚀 Features
- Recommend assessments using natural language queries  
- Supports:
  - Text queries  
  - Full Job Descriptions  
  - URLs containing job descriptions  
- Embedding-based ranking  
- Fast, scalable FAISS vector search  
- Fully working API (FastAPI)  
- Clean modular folder structure  

---

## 📁 Project Structure

├───app
│ ├── embedder.py
│ ├── ingest.py
│ ├── scraper.py
│ ├── utils.py
│ ├── vectorstore.py
│ ├── init.py
│ └── api
│ ├── main.py
│ ├── schemas.py
│ └── init.py
│
├───data
│ ├── embeddings.npy
│ ├── products.csv
│ └── raw_catalog.json
│
├───eval
│ ├── evaluate.py
│ └── train_labels.csv
│
└───frontend
└── README.md

## 🔧 Installation

### 1️⃣ Clone the repository
```bash
git clone 
cd SHLProject
2️⃣ Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

3️⃣ Install dependencies
pip install numpy pandas sentence-transformers faiss-cpu fastapi uvicorn requests beautifulsoup4 openpyxl

🧩 Step-by-Step Setup
Step 1: Scrape SHL Product Catalog

Fetch products from SHL website:

python app/scraper.py


This generates:
data/raw_catalog.json

Step 2: Process & Clean Data
python app/utils.py


This generates:
data/products.csv

Step 3: Generate Embeddings
python app/ingest.py


This generates:
data/embeddings.npy

Step 4: Test Recommendation Function Locally

Open Python shell:

python


Run:

from app.vectorstore import recommend

query = "Hiring a Java developer with teamwork skills"
results = recommend(query, top_k=5)

for r in results:
    print(r['name'], r['url'])

🌐 Run API Server

Start FastAPI server:

uvicorn app.api.main:app --reload


Your API is now live at:

http://127.0.0.1:8000


Open Swagger UI to test:

http://127.0.0.1:8000/docs

📊 Evaluation

Run the evaluator:

python eval/evaluate.py


Uses:

train_labels.csv

Your recommendation engine

Outputs accuracy & ranking metrics.

🖥️ Frontend (Optional)

The frontend/ folder contains a simple UI wrapper.
You can integrate it with the FastAPI backend.
