import requests
import time

API_KEY = "ba49802ae8adf980d74f38137b80eb7302da2156aecd6259f02c61336f4b1bd0"


def check_online(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

    headers = {
        "x-apikey": API_KEY
    }

    try:
        response = requests.get(url, headers=headers)

        # --- УСПЕШНЫЙ ОТВЕТ ---
        if response.status_code == 200:
            data = response.json()

            stats = data["data"]["attributes"]["last_analysis_stats"]

            malicious = stats.get("malicious", 0)
            suspicious = stats.get("suspicious", 0)

            if malicious > 0 or suspicious > 0:
                result = "MALICIOUS"
            else:
                result = "SAFE"

        # --- НЕ НАЙДЕН ---
        elif response.status_code == 404:
            result = "UNKNOWN"

        # --- ЛИМИТ API ---
        elif response.status_code == 429:
            print("⚠ Превышен лимит API, ждем...")
            time.sleep(20)
            return "UNKNOWN"

        # --- ДРУГИЕ ОШИБКИ ---
        else:
            print(f"Ошибка API: {response.status_code}")
            return "UNKNOWN"

        # --- ЗАДЕРЖКА (ВАЖНО) ---
        time.sleep(15)

        return result

    except Exception as e:
        print("Ошибка подключения к API:", e)
        return "UNKNOWN"