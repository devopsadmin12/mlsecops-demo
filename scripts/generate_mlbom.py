import json
import os
import hashlib

os.makedirs("mlbom", exist_ok=True)

with open("models/evil.pkl", "rb") as f:
    model_hash = hashlib.sha256(f.read()).hexdigest()

bom = {
    "application": "DVAIA",
    "mcp": "DVMCP",
    "model": "evil.pkl",
    "framework": "pickle",
    "signed": True,
    "sha256": model_hash
}

with open("mlbom/mlbom.json", "w") as f:
    json.dump(bom, f, indent=2)

print("MLBOM Generated")
