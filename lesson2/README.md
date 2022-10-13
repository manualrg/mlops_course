# mlops_course: Lesson 1 - Your first app in Docker!
MLOps Intro Course

# Index
1. Write your .py
2. Create a Dockerfile that defines your image
3. Run container
4. (Optional): Push your image to a private container repository

# Steps
1. Write your code: run.py
2. Write a Dockerfile
3. Build custom image
```python
docker build -t my_first_app .
docker image ls
```
4. Run a container
```python
docker run my_first_app -dt
```


