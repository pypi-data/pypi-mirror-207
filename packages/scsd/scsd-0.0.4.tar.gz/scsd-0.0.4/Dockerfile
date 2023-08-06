FROM alpine:3.17

# TODO: pyinstaller single executable
RUN apk --no-cache add \
      python3 \
      py3-pip && \
    pip install --no-cache-dir scsd && \
    mkdir /data && \
    chown 1000:1000 /data && \
    mkdir /config && \
    chown 1000:1000 /config


COPY docker/cron-root /etc/crontabs/root

VOLUME ["/data", "/config"]

CMD ["crond", "-f", "-d", "8"]

