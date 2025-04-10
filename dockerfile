# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose Flask port
EXPOSE 5050

# Start Flask app
CMD ["python", "app.py"]