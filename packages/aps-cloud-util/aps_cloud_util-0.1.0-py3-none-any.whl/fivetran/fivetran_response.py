import collections
import json
import logging
from datetime import datetime as dt


class TypedRecords(collections.UserList):
    """Class to create records objects for a fivetran schema.
    :param records: The records of the entity.
    """

    def __init__(self, records: list[dict] = None):
        super().__init__()
        self.list = []
        for record in records:
            self.check_type(record)
            self.check_dict(record)
        else:
            self.list = records

    def check_type(self, item):
        if not isinstance(item, dict):
            raise TypeError("Records must be a list of dicts.")

    def check_dict(self, item):
        for key, value in item.items():
            if not isinstance(key, str):
                raise TypeError("Keys must be strings.")
        for d in self.list:
            if set(d) != set(item):
                raise TypeError("All dicts must have the same keys.")

    def __setitem__(self, i: int, item) -> None:
        self.check_type(item)
        self.check_dict(item)
        self.list[i] = item

    def insert(self, i: int, item) -> None:
        self.check_type(item)
        self.check_dict(item)
        self.list.insert(i, item)

    def append(self, item) -> None:
        self.check_type(item)
        self.check_dict(item)
        self.list.append(item)

    def extend(self, items) -> None:
        for item in items:
            self.check_type(item)
            self.check_dict(item)
        self.list.extend(items)

    def to_dict(self):
        return self.list


class State:
    def __init__(self, state: dict, has_more: bool, has_more_token: str = None):
        self.state = state
        self.has_more = has_more
        self.has_more_token = has_more_token

    def to_dict(self):
        return {
            "entity_state": self.state,
            "has_more_token": self.has_more_token
        }


class Entity:
    """Class to create entity objects for a fivetran schema.
    :param name: The name of the entity.
    :param primary_key: The primary key of the entity.
    :param data: The data of the entity. This is optional. If not provided, the
    entity will return the dict object necessary for the schema.
    """

    def __init__(self, name: str, primary_key: list[str], data: TypedRecords, state: State):
        self.name = name
        self.primary_key = primary_key
        self.state = state
        self.data = data

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def to_dict(self):
        return {
            self.name: self.data
        }

    def to_schema(self):
        return {
            self.name: {
                "primary_key": self.primary_key
            }
        }

    def has_more(self):
        if self.state.has_more:
            return True
        else:
            return False


class Schema:
    """Class to create the json object for a fivetran schema.
    :param entities: The entities of the schema.
    """

    def __init__(self, entities: list[Entity]):
        self.entities = entities

    def to_dict(self):
        schema = {}
        for entity in self.entities:
            schema.update(entity.to_schema())
        return schema


class States:
    def __init__(self, entities: list[Entity]):
        self.entities = entities

    """Class to create the json object for a fivetran state."""

    def __str__(self):
        return [f'{entity.name} - {entity.state}' for entity in self.entities]

    def __repr__(self):
        return [f'{entity.name} - {entity.state}' for entity in self.entities]

    def to_dict(self):
        the_dict = {}
        for entity in self.entities:
            the_dict[entity.name] = entity.state.to_dict()

        return the_dict

    def has_more(self):
        for entity in self.entities:
            if entity.state.has_more:
                return True
        else:
            return False


class FiveTranResponse:
    def __init__(self, entities: list[Entity] = None):
        self.state = States(entities)
        self.schema = Schema(entities)
        self.insert = entities

    def to_dict(self):
        if self.insert is None:
            raise ValueError("No data to return.")
        if self.state is None:
            raise ValueError("No state to return.")
        if self.schema is None:
            raise ValueError("No schema to return.")
        response = {
            "state": self.state.to_dict(),
            "schema": self.schema.to_dict(),
            "insert": {entity.name: entity.data.to_dict() for entity in self.insert},
            "hasMore": self.state.has_more()
        }
        logging.info(f"Response: {json.dumps(response, indent=4)}")
        return response
