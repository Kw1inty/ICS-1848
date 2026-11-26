import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup

tag = input("Введіть HTML-тег (наприклад, p, a, div): ").strip().lower()
url = input("Введіть URL сторінки: ").strip()

try:
    response = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    count = len(soup.find_all(tag))
    print(f"Кількість тегів <{tag}>: {count}")

    path = Path("result.json")
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, list):
                data = []
        except (json.JSONDecodeError, OSError):
            data = []
    else:
        data = []

    data.append({"url": url, "tag": tag, "count": count})
    path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")
    print("Результат додано до result.json.")
except requests.RequestException as error:
    print(f"Помилка завантаження сторінки: {error}")
