import json

with open("data.json") as f:
    data = json.load(f)

print("\nPredicted Traffic in Riyadh Branches:\n")

for b in data["branches"]:
    diff = b["next_hour"] - b["current"]

    if diff > 20:
        status = "High Increase Expected"
    elif diff > 5:
        status = "Small Increase"
    else:
        status = "Stable"

    print(f"Branch: {b['name']}")
    print(f"  Current: {b['current']}")
    print(f"  Next Hour: {b['next_hour']}")
    print(f"  Prediction: {status}\n")