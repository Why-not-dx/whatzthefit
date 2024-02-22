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
        libjpeg-turbo-dev  # Install libjpeg-turbo development headers and library files for JPEG support

COPY ./whatzthefit/requirements.txt .
RUN pip install -r requirements.txt

COPY ./whatzthefit /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
