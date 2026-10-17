# 📅 Week X: [Topic Name]

## 🛠️ 1. What I Built
- **Summary**: Week 6 was focused on serving a model using FastAPI, packaging service into a Docker container and building a user interface calling the API.
- **Key Tools Used**: Docker, Streamlit
- **Artifact Location**: https://github.com/tcsai/portfolio-25-26-oskocak-cell/tree/main/models 
https://github.com/tcsai/portfolio-25-26-oskocak-cell/tree/main/StreamLit%20Photos 

- **How to Run** (if applicable):
  1- Install dependencies using requirements.txt using the following command in terminal:
  pip install fastapi uvicorn scikit-learn joblib pandas streamlit requests
  2- Run in terminal: make all
  This should create 2 files in the "models/" folder
  3- Create an api.py file in src/ folder
  4- Run the API in your terminal: uvicorn src.api:app --reload --port 8000
  Keep this running in another tab in your terminal
  5- Run test queries with the following command (in terminal): curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{"text": "the grand design"}'

Here is an example output of this command:
{"prediction":"science"}
6- Add extra endpoints(terminal): curl http://localhost:8000/health
Expected result: {"status": "RMD-OK"}
7- Dockerize your API using requirements.txt (see Docker file):
docker build -t myapi .
docker run -p 8000:8000 myapi
8- test again:
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{"text": "the grand design"}'
9- To run streamlit in terminal:
streamlit run src/app.py

Expected output: https://github.com/tcsai/portfolio-25-26-oskocak-cell/tree/main/StreamLit%20Photos

## 🔍 2. My Exploration
- **What I Investigated Further**:
  - I added /metrics as an additional endpoint. 

- **Link to Evidence** (optional): https://github.com/tcsai/portfolio-25-26-oskocak-cell/blob/main/src/api.py 

## 🤖 3. Use of GenAI (if applicable)
- **What I Asked It To Do**:
2025-10-11: I asked the following question to ChatGPT: "why do we keep API running only in one terminal tab?"
- **What I Got and Did With It**:
I asked a question to ChatGPT to understand why we need to keep API running in a separate terminal tab/window. I solidified my understanding with its answer.
- **Risks or Misuses You Noticed**:
  N/A

## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?**
As the last week of the course, this week rather built on the previous ones to operationalize previous learnings. This week focused web deployment and model serving. In other words, we have learned the main steps to make previously built (data) product available to the outer world, the users.
- **What was most confusing or interesting?**
One point that can be confusing is that the API should be run and kept running. It is rather about the concept of an API. It is important that the API tab in terminal hosts the server process.
