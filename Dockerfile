FROM python:3.10-slim-bookworm

# Install system packages
RUN apt update && apt install -y \
    git curl ffmpeg wget bash neofetch software-properties-common && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

# Flask settings (optional)
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

CMD ["bash", "-c", "python3 main.py & flask run"]
