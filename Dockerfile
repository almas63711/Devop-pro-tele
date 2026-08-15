FROM python:3.10-slim

COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/docker

WORKDIR /app

RUN pip install --no-cache-dir python-telegram-bot

COPY app.py .

CMD ["python", "app.py"]