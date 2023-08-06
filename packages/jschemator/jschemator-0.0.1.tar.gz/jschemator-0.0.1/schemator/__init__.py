class ComplexType:
    def render(self):
        raise NotImplementedError

    value = None
    contribute_to_class = True


class BooleanField(ComplexType):
    def render(self):
        return {"type": "boolean"}


class IntegerField(ComplexType):
    def render(self):
        return {"type": "integer"}


class DateTimeField(ComplexType):
    def render(self):
        return {
            "type": "string",
            "pattern": "^([\\+-]?\\d{4}(?!\\d{2}\\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$",
        }


class UrlField(ComplexType):
    def render(self):
        return {
            "type": "string",
            "pattern": "^([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\\.)+[a-zA-Z]{2,}",
        }


class ArrayField(ComplexType):
    def __init__(self, type):
        self.type = type

    def render(self):
        return {"type": "array", "items": self.type.render()}


class EnumField(ComplexType):
    def __init__(self, enum):
        self.enum = enum

    def render(self):
        return {
            "type": "string",
            "enum": [e.value for e in self.enum],
        }


class StringField(ComplexType):
    def render(self):
        return {"type": "string"}

    def __get__(self, __instance__, __owner__):
        return self.value

    def __set__(self, __instance__, value):
        self.value = value


class JsonSchema:
    def schema(self):
        schema_fields = []
        for attribute_name, attribute_description in type(self).__dict__.items():
            if (
                not "__" in attribute_name
                and type(attribute_description).contribute_to_class
            ):
                schema_fields.append(attribute_name)
        properties = {
            schema_field: type(self).__dict__[schema_field].render()
            for schema_field in schema_fields
        }
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": properties,
        }
