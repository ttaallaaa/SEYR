import json

def load_data():
    with open("data.json", encoding="utf-8") as f:
        return json.load(f)

def show_predictions(data):
    print("\n🔮 Smart Prediction for the Next Hour:\n")

    for branch in data["branches"]:
        name = branch["name"]
        current = branch["current"]
        next_hour = branch["next_hour"]
        diff = next_hour - current

        print(f"📍 {name}")
        print(f"   Current: {current}")
        print(f"   Next Hour: {next_hour}  (Change: {diff})")

        if diff > 20:
            print("   🔴 High increase expected\n")
        elif diff > 5:
            print("   🟡 Slight increase\n")
        else:
            print("   🟢 Stable\n")

if __name__ == "__main__":
    data = load_data()
    show_predictions(data)