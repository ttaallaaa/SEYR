# alert_system.py
import json

def load_data():
    with open("data.json", encoding="utf-8") as f:
        return json.load(f)

def check_alerts(data):
    print("\n Smart Alert System:\n")

    for branch in data["branches"]:
        name = branch["name"]
        current = branch["current"]
        next_hour = branch["next_hour"]

        diff = next_hour - current

        print(f" {name}")
        print(f"   Current: {current}")
        print(f"   Next Hour: {next_hour}")

        if diff > 20:
            print("Alert! Sudden congestion detected — appointments will be auto-adjusted.\n")
        else:
            print("Stable.\n")

if __name__ == "__main__":
    data = load_data()
    check_alerts(data)
