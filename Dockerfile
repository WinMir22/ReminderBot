FROM python:3.13-slim-bullseye AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt
FROM base
COPY . /app
CMD ["python", "app.py"]
