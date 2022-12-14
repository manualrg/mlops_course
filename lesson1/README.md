# mlops_course: Lesson 1 - Your first app in Docker!
MLOps Intro Course

# Index
1. Your first app in Docker!
2. Pull an image from DockerHub
3. Run Hello World container
4. Run container interactively
5. Start a Service: jupyter-lab environment

# Steps
1. Pull your desired image from DockerHub
```bash
docker pull hello-world
docker image ls
```

2. Run container
```bash
docker run hello-world
```

3. Pull a base image and run it interactively
Pull image
```bash
docker pull python:3.7.9-slim
docker image ls
```

```bash
docker run python:3.7.9-slim
docker run -d -t python:3.7.9-slim
docker ps
```
copy CONTANIER_ID: 6441082fc62f or NAME: romantic_murdock

```bash
docker exec -it 6441082fc62f bash
python --version
pip list
exit
```

Stop the container
```bash
docker stop 6441082fc62f
docker ps -a
```
Container status is stored in exit state, but image is NOT modified (can be modified, but more on this later)

```bash
docker rm 6441082fc62f
docker ps -a
```

4. Start a Service: jupyter-lab environment
```bash
docker pull jupyter/scipy-notebook
docker image ls
```
Start a jupyter lab server inside the container

```bash
docker run -p 8888:8888 \
    -e JUPYTER_ENABLE_LAB=yes jupyter/scipy-notebook
```