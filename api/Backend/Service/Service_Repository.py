from ..Entity.Models import Service
from pony.orm import *


class ServiceRepository:
    def __init__(self):
        self.service = None

    @db_session
    def add(self, name: str):
        self.service = Service(name=name)
        commit()
        return self.service

    @db_session
    def get(self, service_id: int):
        return Service.get(id=service_id)

    @db_session
    def get_all(self):
        self.service = [s.to_dict() for s in Service.select()]
        return self.service

    @db_session
    def update(self, service_id: int, name: str):
        self.service = Service.get(id=service_id)
        if self.service:
            if name:
                self.service.name = name
                commit()
        return self.service

    @db_session
    def delete(self, service_id: int):
        self.service = Service.get(id=service_id)
        if self.service:
            Service.delete(id=service_id)
