ARG VERSION

FROM python:3.8.5-slim-buster AS base
LABEL description="services"

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.9/supercronic-linux-amd64 \
    SUPERCRONIC=supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=5ddf8ea26b56d4a7ff6faecdd8966610d5cb9d85

RUN apt-get update \
    && apt-get install -y  \
        locales \
        locales-all \
        curl \
    && curl -fsSLO "$SUPERCRONIC_URL" \
    && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
    && chmod +x "$SUPERCRONIC" \
    && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
    && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic \
    && locale-gen en_US.UTF-8 \
    && apt-get update

RUN useradd -ms /bin/bash user \
    && mkdir -p /home/project/py_scripts/ \
    && chown -R user:user /var /home /etc/fstab

COPY /py_scripts /home/project/py_scripts/


RUN python -m pip install -r /home/project/py_scripts/requirements.txt --no-cache-dir

USER user
WORKDIR /home/project/py_scripts

FROM base AS prod

USER root
RUN apt-get clean \
    && apt-get autoclean \
    && apt-get remove -y \
        gcc \
        unzip \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


