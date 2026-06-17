import json

bom = {

    "application":"DVAIA",

    "mcp":"DVMCP",

    "model":"evil.pkl",

    "framework":"pickle",

    "signed":True

}

with open("mlbom/mlbom.json","w") as f:

    json.dump(
        bom,
        f,
        indent=2
    )

print("MLBOM Generated")