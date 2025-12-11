# suggestions.py
import json

def load_data():
    with open("data.json", encoding="utf-8") as f:
        return json.load(f)

def suggest_best_branch(data):
    branches = data["branches"]
    # Choose the branch with the lowest "current" value
    best = min(branches, key=lambda x: x["current"])
    return best

if __name__ == "__main__":
    data = load_data()
    best = suggest_best_branch(data)

    print(" Best Branch to Visit Now:")
    print(f"{best['name']} — Current Visitors: {best['current']}")
