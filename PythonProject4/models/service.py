class MaintenanceService:
    def __init__(self):
        self.requests = []

    def add_request(self, request):
        self.requests.append(request)
        print("Заявка", request.request_id, "добавлена")

    def find_by_id(self, request_id):
        for r in self.requests:
            if r.request_id == request_id:
                return r
        return None

    def get_all(self):
        return self.requests

    def filter_by_status(self, status):
        result = []
        for r in self.requests:
            if r.status == status:
                result.append(r)
        return result

    def filter_by_priority(self, priority):
        result = []
        for r in self.requests:
            if r.priority == priority:
                result.append(r)
        return result
