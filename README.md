## 💾 JSON Database Functions

### Load User Data

```python
def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return {}

    try:
        with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}
```

### Save User Data

```python
def save_user_data(order_Id, data):
    users = load_user_data()

    users[order_Id] = data

    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)
```

### Update User Data

```python
def update_user_data(order_id, data):
    users = load_user_data()

    if order_id not in users:
        users[order_id] = {}

    users[order_id].update(data)

    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)
```

### Example Usage

```python
data = {
    "name": "dishant"
}

update_user_data("ORDER-1", data)
```

### Example Database

```json
{
    "ORDER-1": {
        "name": "dishant",
        "email": "example@gmail.com"
    }
}
```

### Features

* Load JSON data
* Save JSON data
* Update existing records
* Create records automatically if not found
* Simple file-based database system
