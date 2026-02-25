# llms_apps
This repo will contain working codes for different apps/mock businesses built using different foundational models

# Steps to run the app
1. In terminal 1 - cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
2. In terminal 2 - cd frontend
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
