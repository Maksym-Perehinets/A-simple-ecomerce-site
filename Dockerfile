FROM python:3.11-alpine3.19

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY requirements.txt /src/
RUN pip install --upgrade pip \
    pip install -r requirements.txt
COPY . /src/

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]