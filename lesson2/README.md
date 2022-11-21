# mlops_course: Lesson 2 - Your first py process in Docker!
MLOps Intro Course

# Index
1. Write your process logic
2. Create a Dockerfile that defines your image
3. Run container
4. (Optional): Push your image to a private container repository

# Steps
0. Create a folder to store your app logic and artifacts: `/app` 
1. Write your code: run.py
2. Write a Dockerfile with RUN statement
3. Build custom image
```python
docker build -t my_first_app .
docker image ls
```
4. Run a container
```python
docker run my_first_app -dt
```


