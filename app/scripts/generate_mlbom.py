# scripts/generate_mlbom.py

import json

bom = {
    "model": "evil.pkl",
    "framework": "pickle",
    "owner": "AI Team",
    "application": "MLSecOps Demo"
}

with open("mlbom/mlbom.json", "w") as f:
    json.dump(bom, f, indent=2)

print("MLBOM Generated")