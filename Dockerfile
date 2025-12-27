# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy ONLY requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI
CMD uvicorn main:app --host 0.0.0.0 --port 8000
