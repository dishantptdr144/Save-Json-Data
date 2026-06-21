import json
import os

USER_DATA_FILE = "user_data.json"


def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return {}

    try:
        with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

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