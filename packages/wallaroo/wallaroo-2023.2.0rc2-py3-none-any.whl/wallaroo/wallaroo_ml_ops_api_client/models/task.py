import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.arbex_status import ArbexStatus

if TYPE_CHECKING:
  from ..models.task_input_data import TaskInputData





T = TypeVar("T", bound="Task")


@attr.s(auto_attribs=True)
class Task:
    """ 
        Attributes:
            created_at (datetime.datetime):
            input_data (TaskInputData):
            killed (bool):
            status (ArbexStatus):
            updated_at (datetime.datetime):
            workspace_id (int):
     """

    created_at: datetime.datetime
    input_data: 'TaskInputData'
    killed: bool
    status: ArbexStatus
    updated_at: datetime.datetime
    workspace_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        input_data = self.input_data.to_dict()

        killed = self.killed
        status = self.status.value

        updated_at = self.updated_at.isoformat()

        workspace_id = self.workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "input_data": input_data,
            "killed": killed,
            "status": status,
            "updated_at": updated_at,
            "workspace_id": workspace_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_input_data import TaskInputData
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))




        input_data = TaskInputData.from_dict(d.pop("input_data"))




        killed = d.pop("killed")

        status = ArbexStatus(d.pop("status"))




        updated_at = isoparse(d.pop("updated_at"))




        workspace_id = d.pop("workspace_id")

        task = cls(
            created_at=created_at,
            input_data=input_data,
            killed=killed,
            status=status,
            updated_at=updated_at,
            workspace_id=workspace_id,
        )

        task.additional_properties = d
        return task

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
