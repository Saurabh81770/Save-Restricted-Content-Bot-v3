FROM python:3.10-slim-bookworm

RUN apt update && apt install -y git curl ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -U pip wheel && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

