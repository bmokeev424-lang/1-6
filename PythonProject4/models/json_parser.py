import json
from models.models import Equipment


def load_equipment(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Equipment.from_dict(item) for item in data]


def show_repair_needed(equipment_list):
    print("\nОборудование, требующее ремонта:")
    for eq in equipment_list:
        if eq.needs_repair():
            print(" -", eq.inventory_number, "|", eq.name, "|", eq.status)