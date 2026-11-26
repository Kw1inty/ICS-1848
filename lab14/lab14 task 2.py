import requests
from bs4 import BeautifulSoup

url = input("Введіть URL сторінки: ").strip()

try:
    response = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    texts = []
    for link in soup.find_all("a"):
        text = link.get_text(" ", strip=True)
        if text:
            texts.append(text)

    with open("links.txt", "w", encoding="utf-8") as file:
        file.write("\\n".join(texts))

    print(f"Знайдено текстів посилань: {len(texts)}")
    print("Результат записано у links.txt.")
except requests.RequestException as error:
    print(f"Помилка завантаження сторінки: {error}")
