FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY app.py .

RUN useradd appuser
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
