import json

with open("moonboard_160_template.json") as f:
    data = json.load(f)

# Quick check
print(f"Loaded {len(data)} problems")

# Print the first one
print(json.dumps(data["0"], indent=4))
