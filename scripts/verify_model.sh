#!/bin/bash

cosign verify-blob \
  --key cosign.pub \
  --bundle models/signatures/safe.pkl.bundle \
  models/safe.pkl
