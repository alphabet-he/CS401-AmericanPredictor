FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP predict_american_api.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5004"]