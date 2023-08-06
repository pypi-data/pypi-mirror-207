import json
import os
from typing import List

from pydantic import BaseModel, parse_obj_as

from messenger.models import AbstractModel


class Table:
    model: AbstractModel
    schema: BaseModel
    _collection = []

    IMPROPERLY_CONFIGURED_MESSAGE = (
        "model must implement AbstractModel, " "while schema must implement pydantic BaseModel"
    )

    INTEGRATION_ERROR_MESSAGE = "Raw with such 'id' already inserted in the database"

    def all(self):
        with open(self.table_name, "r") as file:
            data_set = json.load(file) if os.path.getsize(self.table_name) != 0 else []
            return parse_obj_as(List[self.schema], data_set)

    def get(self, id: int):
        with open(self.table_name, "r") as file:
            data_set: list = json.load(file) if os.path.getsize(self.table_name) != 0 else []
            res = list(filter(lambda el: el["id"] == id, data_set))
            if not res:
                raise self.model.DoesNotExistError("")
            return self.schema(**res[0])

    def insert(self, instance: AbstractModel):
        with open(self.table_name, "w+") as file:
            data_set: list = json.load(file) if os.path.getsize(self.table_name) != 0 else []
            res = list(filter(lambda el: el["id"] == instance.id, data_set))
            if not res:
                data_set.append(self.schema(**instance.__dict__ | {"id": instance._AbstractModel__id}).dict())
                file.write(json.dumps(data_set))
                return
            raise self.IntegrationError(self.INTEGRATION_ERROR_MESSAGE)

    def update(self, instance: AbstractModel):
        self.delete(instance.id)
        self.insert(instance)
        return self.get(instance.id)  # refreshed value from db

    def delete(self, id):
        with open(self.table_name, "w+") as file:
            data_set: list = json.load(file) if os.path.getsize(self.table_name) != 0 else []
            res = list(filter(lambda el: el["id"] == id, data_set))
            if not res:
                raise self.model.DoesNotExistError(self.model.DOES_NOT_EXIST_MESSAGE)
            updated_data_set = list(filter(lambda el: el["id"] != res["id"], data_set))
            json.dump(updated_data_set, file)
            return self.schema(**res)

    def __init__(self, model: AbstractModel, schema: BaseModel, data_persistent_mode: bool = False):
        if not isinstance(model, AbstractModel) and isinstance(schema, BaseModel):
            raise self.ImproperlyConfiguredError("")
        self.model = model
        self.schema = schema
        self.table_name = f"_table_{model.__name__}.json"
        self.persistent_mode = data_persistent_mode
        if self.persistent_mode:
            with open(self.table_name, "w") as file:
                json.dump(self._collection, file)

    class ImproperlyConfiguredError(Exception):
        pass

    class IntegrationError(Exception):
        pass
