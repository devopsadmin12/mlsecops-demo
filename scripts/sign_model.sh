#!/bin/bash

set -e

MODEL=models/evil.pkl

cosign sign-blob \
  --key cosign.key \
  --output-signature models/signatures/evil.pkl.sig \
  $MODEL

echo "Model Signed"