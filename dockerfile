
# Use Python 3.12
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install dependencies first for better build caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application and migrations
COPY app/ ./app/
COPY migrations/ ./migrations/

# Application listens on port 8080
EXPOSE 8080

# Start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
