FROM python:3.10.4-slim-buster

# System dependencies
RUN apt update && apt install -y \
    git curl ffmpeg wget bash neofetch software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -U pip wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose Flask port
EXPOSE 8080

# Set Flask environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Run both Flask and bot together safely
CMD ["bash", "-c", "python3 main.py & flask run"]
