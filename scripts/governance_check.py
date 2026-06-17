import yaml
import os
import sys

policy = yaml.safe_load(
    open("governance/policy.yml")
)

model = "evil.pkl"

errors = []

if model in policy["blocked_models"]:
    errors.append(
        "Blocked model detected"
    )

if policy["require_mlbom"]:

    if not os.path.exists(
        "mlbom/mlbom.json"
    ):
        errors.append(
            "MLBOM missing"
        )

if errors:

    print(errors)

    sys.exit(1)

print("Governance Passed")