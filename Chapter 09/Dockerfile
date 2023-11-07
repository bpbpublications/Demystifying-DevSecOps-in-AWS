FROM python:3.8-alpine
WORKDIR /app
COPY . .
RUN python -m pip install -r requirements.txt
EXPOSE 5000
cmd ["python3", "server.py"]
