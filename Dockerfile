# Use official Python image
FROM python:3.11-slim

# Don't write .pyc files and force stdout flush
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory inside container
WORKDIR /app

# Copy everything from your local project to /app inside the container
COPY . .

# Install Django (or use requirements.txt if you have one)
RUN pip install --no-cache-dir django

# Expose port 8000 so you can access the app
EXPOSE 8000

# Run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
