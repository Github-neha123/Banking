FROM python:3.9-slim

WORKDIR /app

COPY banking_system.py .

CMD ["python", "banking_system.py"]