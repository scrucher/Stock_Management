FROM python:3.9-slim

WORKDIR /api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn","--preload" , "--bind", "0.0.0.0:5000", "Backend:app"]