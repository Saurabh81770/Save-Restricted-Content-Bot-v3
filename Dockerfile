FROM python:3.10-slim-bookworm

# System dependencies install karte hain
RUN apt update && apt install -y git curl ffmpeg && rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app

# Requirements copy karo
COPY requirements.txt .

# Python dependencies install karo
RUN pip install --no-cache-dir -U pip wheel && pip install --no-cache-dir -r requirements.txt

# Baaki project files copy karo
COPY . .

# Flask ya port expose ki zarurat nahi hai
CMD ["python3", "main.py"]

