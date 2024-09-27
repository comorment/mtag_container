#!/bin/bash
set -eou pipefail

apt-get update && apt-get install -y  --no-install-recommends \
    apt-utils=2.7.14build2 \
    ca-certificates=20240203 \
    curl=8.5.0-2ubuntu10.4 \
    && \
    update-ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
