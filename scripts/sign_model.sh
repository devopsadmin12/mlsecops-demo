#!/bin/bash

set -e

MODEL=models/safe.pkl

cosign sign-blob \
  --key cosign.key \
  --bundle models/signatures/safe.pkl.bundle \
  $MODEL

echo "Model Signed"
