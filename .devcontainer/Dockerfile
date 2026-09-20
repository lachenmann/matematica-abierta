FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl git xz-utils zstd unzip \
    && rm -rf /var/lib/apt/lists/*
