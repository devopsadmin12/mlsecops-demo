from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.output.json import JsonV1Dot6
import hashlib
import os

# Create directory
os.makedirs("mlbom", exist_ok=True)

with open("models/evil.pkl", "rb") as f:
    sha256 = hashlib.sha256(f.read()).hexdigest()

bom = Bom()

model_component = Component(
    name="evil.pkl",
    type=ComponentType.APPLICATION,
    version="1.0"
)

model_component.description = f"SHA256={sha256}"

bom.components.add(model_component)

mcp_component = Component(
    name="DVMCP",
    type=ComponentType.APPLICATION,
    version="1.0"
)

bom.components.add(mcp_component)

output = JsonV1Dot6(bom)

with open("mlbom/mlbom-cyclonedx.json", "w") as f:
    f.write(output.output_as_string())

print("CycloneDX MLBOM Generated")
