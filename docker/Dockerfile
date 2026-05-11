# Etapa 1: Builder
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Etapa 2: Imagen Final
FROM python:3.9-slim
WORKDIR /app
# Copiamos solo las dependencias instaladas de la etapa anterior
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 5000
CMD ["python", "app.py"]
