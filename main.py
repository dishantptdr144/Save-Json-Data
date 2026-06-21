import json
import os

USER_DATA_FILE = "user_data.json"


def load_user_data(user_id=None):
    if not os.path.exists(USER_DATA_FILE):
        return "Not found"

    try:
        with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if user_id is None:
            return data

        return data.get(str(user_id), "Not found")

    except Exception:
        return "Not found"

def save_user_data(order_Id, data):
    users = load_user_data()

    users[order_Id] = data

    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def update_user_data(order_id, data):
    users = load_user_data()

    if order_id not in users:
        users[order_id] = {}

    users[order_id].update(data)

    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)


data = {
    "name": "dishant",
}

update_user_data("ORDER-1", data)

# data = load_order_details()
# print(data)
