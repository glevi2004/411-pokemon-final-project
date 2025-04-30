FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV FLASK_APP=pokemon/app.py
ENV FLASK_ENV=development
ENV PYTHONPATH=/app
ENV SECRET_KEY=dev-key-for-testing
ENV DATABASE_URL=sqlite:///pokemon.db

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "pokemon/app.py"]
