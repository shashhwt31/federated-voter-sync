FROM python:3.11-slim

WORKDIR /app

COPY state_service/requirements.txt .
RUN pip install -r requirements.txt

COPY state_service/app ./app
COPY common ./common

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
