from enum import Enum


class PipelinesGetLogsResponse200Status(str, Enum):
    ALL = "All"
    BYTELIMITED = "ByteLimited"
    RECORDLIMITED = "RecordLimited"
    SCHEMACHANGE = "SchemaChange"

    def __str__(self) -> str:
        return str(self.value)
