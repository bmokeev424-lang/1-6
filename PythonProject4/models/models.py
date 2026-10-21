from datetime import datetime

class Equipment:
    def __init__(self, inventory_number, name, equipment_type, department,
                 production_year, status="working"):
        self.inventory_number = inventory_number
        self.name = name
        self.equipment_type = equipment_type
        self.department = department
        self.production_year = production_year
        self.status = status

    def show_info(self):
        print(f"Инвентарный номер: {self.inventory_number}")
        print(f"Название: {self.name}")
        print(f"Тип: {self.equipment_type}")
        print(f"Подразделение: {self.department}")
        print(f"Год выпуска: {self.production_year}")
        print(f"Состояние: {self.status}")

    def change_status(self, new_status):
        self.status = new_status

    def needs_repair(self):
        return self.status in {"repair", "broken"}

    @classmethod
    def from_dict(cls, item):
        return cls(
            item["inventory_number"],
            item["name"],
            item["equipment_type"],
            item["department"],
            item["production_year"],
            item.get("status", "working")
        )

class MaintenanceRequest:
    ALLOWED_STATUSES = {"new", "in_progress", "completed", "cancelled"}
    ALLOWED_PRIORITIES = {"low", "medium", "high", "critical"}

    def __init__(self, request_id, equipment, description, priority="medium"):
        self.request_id = request_id
        self.equipment = equipment
        self.description = description
        self.priority = priority
        self.status = "new"
        self.created_at = datetime.now()

    def show_info(self):
        print("Заявка №", self.request_id)
        print("Оборудование:", self.equipment.name)
        print("Описание:", self.description)
        print("Приоритет:", self.priority)
        print("Статус:", self.status)
        print("Создана:", self.created_at)

    def start(self):
        if self.status != "new":
            raise ValueError("В работу можно взять только новую заявку")
        self.status = "in_progress"

    def complete(self):
        if self.status != "in_progress":
            raise ValueError("Завершить можно только заявку в работе")
        self.status = "completed"

    def cancel(self):
        if self.status == "completed":
            raise ValueError("Завершённую заявку отменить нельзя")
        self.status = "cancelled"

    def change_priority(self, priority):
        if priority not in self.ALLOWED_PRIORITIES:
            raise ValueError("Недопустимый приоритет")
        self.priority = priority