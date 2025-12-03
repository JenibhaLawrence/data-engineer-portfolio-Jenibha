# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose port
ENV PORT=8080
CMD ["python", "main.py"]
