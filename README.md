# PM/MDL Assignment 1 — Deployment

## Structure

```
.
├─ code/
│  ├─ deployment/
│  │  ├─ api/
│  │  │  ├─ Dockerfile
│  │  │  └─ main.py
│  │  ├─ app/
│  │  │  ├─ Dockerfile
│  │  │  └─ app.py
│  │  └─ docker-compose.yml
│  └─ models/
│     └─ train.py
├─ models/
│  └─ model.joblib     
└─ requirements.txt
```

---

## Launch

Clone and raise services:

```bash
git clone https://github.com/<your-username>/pmldl-assignment1-deploy.git
cd pmldl-assignment1-deploy/code/deployment
docker compose build --no-cache
docker compose up -d
```

Checking:

- API (health):  
  `http://localhost:8000/health` → `{"status":"ok"}`
- UI (Streamlit):  
  `http://localhost:8501`

Stop:

```bash
docker compose down
```
