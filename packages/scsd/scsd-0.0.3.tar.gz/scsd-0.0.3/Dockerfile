FROM alpine:3.17

# TODO: pyinstaller single executable
RUN apk --no-cache add \
      python3 \
      py3-pip && \
    pip install --no-cache-dir -i https://test.pypi.org/simple/ scsd && \
    mkdir /data && \
    chown 1000:1000 /data && \
    mkdir /config && \
    chown 1000:1000 /config && \
    scsd -h && \
    exit 1


COPY docker/cron-root /etc/crontabs/root

USER 1000

VOLUME ["/data", "/config"]

CMD ["crond", "-f", "-d", "8"]

