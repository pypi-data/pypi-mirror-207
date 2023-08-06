import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.arbex_status import ArbexStatus

if TYPE_CHECKING:
  from ..models.get_by_id_1_response_200_input_data import \
      GetById1Response200InputData





T = TypeVar("T", bound="GetById1Response200")


@attr.s(auto_attribs=True)
class GetById1Response200:
    """ 
        Attributes:
            created_at (datetime.datetime):
            input_data (GetById1Response200InputData):
            killed (bool):
            status (ArbexStatus):
            updated_at (datetime.datetime):
            workspace_id (int):
     """

    created_at: datetime.datetime
    input_data: 'GetById1Response200InputData'
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
        from ..models.get_by_id_1_response_200_input_data import \
            GetById1Response200InputData
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))




        input_data = GetById1Response200InputData.from_dict(d.pop("input_data"))




        killed = d.pop("killed")

        status = ArbexStatus(d.pop("status"))




        updated_at = isoparse(d.pop("updated_at"))




        workspace_id = d.pop("workspace_id")

        get_by_id_1_response_200 = cls(
            created_at=created_at,
            input_data=input_data,
            killed=killed,
            status=status,
            updated_at=updated_at,
            workspace_id=workspace_id,
        )

        get_by_id_1_response_200.additional_properties = d
        return get_by_id_1_response_200

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
