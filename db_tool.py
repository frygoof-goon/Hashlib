import json
from database import init_db, add_hash

def main():
    init_db()

    with open("hashes.json", "r") as f:
        data = json.load(f)

    count = 0

    for item in data:
        try:
            add_hash(item)
            count += 1
        except:
            pass

    print(f"Добавлено {count} хэшей")

if __name__ == "__main__":
    main()