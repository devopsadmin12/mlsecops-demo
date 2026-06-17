#!/bin/bash

set -e

cosign verify-blob \
  --key cosign.pub \
  --signature models/signatures/evil.pkl.sig \
  models/evil.pkl