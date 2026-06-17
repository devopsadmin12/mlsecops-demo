#!/bin/bash

cosign verify-blob \
  --key cosign.pub \
  --bundle models/signatures/evil.pkl.bundle \
  models/evil.pkl