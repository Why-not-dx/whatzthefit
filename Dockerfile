FROM python:3.13.0a4-alpine


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

# ADD wait_for_db_and_start_server.sh .

COPY ./whatzthefit/requirements.txt .
RUN pip install -r requirements.txt

COPY ./whatzthefit /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
