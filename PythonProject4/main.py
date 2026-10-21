from models.models import Equipment, MaintenanceRequest
from models.service import MaintenanceService
from models.json_parser import load_equipment, show_repair_needed
from models.html_parser import parse_html, save_json


def main():
    print("Задача 1")
    machine = Equipment("EQ-001", "Токарный станок 16К20", "станок",
                        "Механический цех", 2025)
    machine.show_info()

    print("\nМеняем состояние...")
    machine.change_status("repair")
    print("Требуется ремонт:", machine.needs_repair())

    print("\nЗадача 2")
    req = MaintenanceRequest(1, machine, "Не включается", "high")
    req.show_info()
    req.start()
    req.change_priority("critical")
    req.complete()

    print("\nПроверка отменённой заявки ")
    req2 = MaintenanceRequest(2, machine, "Шумит кулер", "low")
    req2.cancel()
    try:
        req2.complete()
    except ValueError as e:
        print("Ошибка (ожидаемо):", e)

    print("\n Задача 3 ")
    service = MaintenanceService()
    service.add_request(req)
    service.add_request(req2)
    service.add_request(MaintenanceRequest(3, machine, "Течёт масло", "critical"))
    service.add_request(MaintenanceRequest(4, machine, "Профилактика", "low"))

    print("\nВсе заявки:")
    for r in service.get_all():
        print(" - №", r.request_id, "|", r.status, "|", r.priority)

    print("\nПоиск заявки №3:")
    found = service.find_by_id(3)
    if found:
        found.show_info()
    else:
        print("Не найдена")

    print("\nФильтр по статусу new:")
    for r in service.filter_by_status("new"):
        print(" - №", r.request_id)

    print("\nФильтр по приоритету critical:")
    for r in service.filter_by_priority("critical"):
        print(" - №", r.request_id)

    print("\nЗадача 4")
    equipment_list = load_equipment("models/equipment.json")
    print("Загружено единиц:", len(equipment_list))
    for eq in equipment_list:
        eq.show_info()
        print("-" * 30)
    show_repair_needed(equipment_list)

    print("\nЗадача 5")
    html_data = parse_html("models/equipment.html")
    print("Из HTML извлечено:", len(html_data), "записей")
    for item in html_data:
        print(item)
    save_json(html_data, "models/parsed_equipment.json")
    print("Сохранено в models/parsed_equipment.json")

    print("\nЗадача 6")
    print("Открытые заявки с приоритетом high и critical:")
    for r in service.get_all():
        if r.status == "new" and r.priority in ("high", "critical"):
            print(" - №", r.request_id, "|", r.priority, "|", r.description)

    f = open("models/report.txt", "w", encoding="utf-8")
    f.write("ОТЧЁТ ПО ЗАЯВКАМ\n")
    f.write("=" * 30 + "\n")
    for r in service.get_all():
        f.write("Заявка " + str(r.request_id) + ": " + r.description
                + " (" + r.priority + ", " + r.status + ")\n")
    f.close()
    print("Отчёт сохранён в models/report.txt")


if __name__ == "__main__":
    main()