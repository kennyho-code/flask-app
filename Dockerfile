FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only the files needed for installing dependencies
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV PYTHONPATH=/app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]