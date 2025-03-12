FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install necessary system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# Upgrade pip
RUN pip install -U pip

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run Gunicorn instead of Django’s dev server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "StoryBuilder.wsgi:application"]
