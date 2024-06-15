FROM python:3.13.0a6-alpine3.19

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# ENV DJANGO_SETTINGS_MODULE fitweb.settings

RUN pip install --upgrade pip

# Install development tools
RUN apk update && \
    apk add --no-cache \
        gcc \
        musl-dev \
        linux-headers \
        libc-dev \
        libffi-dev \
        openssl-dev \
        zlib-dev \
        libjpeg-turbo-dev \ 
        python3-dev \
        mariadb-connector-c-dev \
        mysql-client 


COPY ./whatzthefit/requirements.txt .
RUN pip install -r requirements.txt

COPY ./whatzthefit /app

COPY .env /.env

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
