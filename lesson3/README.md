# mlops_course: Lesson 2 - Your first py process in Docker!
MLOps Intro Course

# Index
1. FastAPI
2. Get model pickle
3. Deploy a model in FastAPI endpoint (local)
4. Add features to your endpoint: Data Validation and Storage Backend (TODO)
5. Dockerize a prediction service (TODO)

# Steps
0. Create a model .pickle in `/lesson3/models/`
```bash
.venv/bin/python ./lesson3/train.py
```

1. Create a folder to store your app logic and artifacts: `/app` 
2. Write your code: main.py
3. Run the endopoint server locally:
```bash
cd lesson3/app
uvicorn main:app --reload
```
4. Test your local endopont: http://127.0.0.1:8000/docs/






