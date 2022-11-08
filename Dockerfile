FROM python:3.10

WORKDIR /code

COPY app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

ENV FLASK_DEBUG=1
CMD flask run --host=0.0.0.0