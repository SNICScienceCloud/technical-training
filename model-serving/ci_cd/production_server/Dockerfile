FROM python:3.6
ADD /technical-training/model-serving/ci_cd/production_server/requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["./app.py","--host=0.0.0.0"]
