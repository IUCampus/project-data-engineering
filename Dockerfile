FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "load_data.py"]
# Expose port if needed, e.g., EXPOSE 8000
EXPOSE 8000