from ..Entity.Models import Unit
from pony.orm import *


class UnitRepository:
    def __init__(self):
        self.unit = None

    @db_session
    def add(self, name: str):
        self.unit = Unit(name=name)
        commit()
        return self.unit

    @db_session
    def get(self, unit_id: int):
        return Unit.get(id=unit_id)

    @db_session
    def get_all(self):
        self.unit = [s.to_dict() for s in Unit.select()]
        return self.unit

    @db_session
    def update(self, unit_id: int, name: str):
        self.unit = Unit.get(id=unit_id)
        if self.unit:
            if name:
                self.unit.name = name
                commit()
        return self.unit

    @db_session
    def delete(self, unit_id: int):
        self.unit = Unit.get(id=unit_id)
        if self.unit:
            Unit.delete(id=unit_id)
