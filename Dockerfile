FROM tiangolo/uwsgi-nginx:python3.7-alpine3.8

RUN pip install requests
# Add demo app
COPY ./app /app
WORKDIR /app

ENTRYPOINT [ "python", "main.py"]
