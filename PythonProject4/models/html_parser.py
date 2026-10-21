import json
from bs4 import BeautifulSoup

def parse_html(path):
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    result = []
    for row in soup.find_all("tr")[1:]:
        cells = row.find_all("td")
        if len(cells) < 3:
            continue
        result.append({
            "inventory_number": cells[0].text.strip(),
            "name": cells[1].text.strip(),
            "status": cells[2].text.strip(),
        })
    return result


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)