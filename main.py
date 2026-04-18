from scanner import scan_directory
from hasher import calculate_sha256
from database import check_local_db, init_db
from api_client import check_online


def main():
    path = input("Введите путь к папке: ")

    init_db()
    files = scan_directory(path)

    total = 0
    malicious = 0
    safe = 0
    unknown = 0

    local_found = 0
    online_checked = 0

    for file in files:
        total += 1
        try:
            file_hash = calculate_sha256(file)

            # --- ЛОКАЛЬНАЯ ПРОВЕРКА ---
            if check_local_db(file_hash):
                status = "MALICIOUS"
                source = "LOCAL"
                malicious += 1
                local_found += 1

            else:
                status = check_online(file_hash)
                source = "ONLINE"
                online_checked += 1

                if status == "MALICIOUS":
                    malicious += 1
                elif status == "SAFE":
                    safe += 1
                else:
                    unknown += 1

            print("\nФайл:", file)
            print("Хэш:", file_hash)
            print("Статус:", status)
            print("Источник:", source)
            print("-" * 30)

        except Exception as e:
            print("Ошибка:", e)

    print("\n=== ИТОГ ===")
    print("Всего файлов:", total)
    print("Вредоносных:", malicious)
    print("Безопасных:", safe)
    print("Неизвестных:", unknown)

    print("\n=== ПО ИСТОЧНИКАМ ===")
    print("Найдено локально:", local_found)
    print("Проверено через API:", online_checked)


if __name__ == "__main__":
    main()