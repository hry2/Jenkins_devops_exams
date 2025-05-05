FROM python:3.8-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install -y gcc \
    && apt-get clean

RUN pip install --no-cache-dir -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
