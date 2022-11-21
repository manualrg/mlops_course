FROM python:3.7.9-slim

RUN pip install pandas \
    && pip install pandas_datareader==0.10.0

RUN mkdir -p /home/app
COPY ./app /home/app
WORKDIR /home/app

ENTRYPOINT ["python3", "run.py"]
