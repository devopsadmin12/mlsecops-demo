import json

bom = {
  "model":"evil.pkl",
  "framework":"pickle",
  "application":"DVAIA",
  "mcp":"DVMCP"
}

with open("mlbom/mlbom.json","w") as f:
    json.dump(bom,f,indent=2)