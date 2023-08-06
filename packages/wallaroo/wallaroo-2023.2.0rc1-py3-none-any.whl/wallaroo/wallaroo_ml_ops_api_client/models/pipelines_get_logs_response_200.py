from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipelines_get_logs_response_200_status import \
    PipelinesGetLogsResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.pipelines_get_logs_response_200_records import \
      PipelinesGetLogsResponse200Records





T = TypeVar("T", bound="PipelinesGetLogsResponse200")


@attr.s(auto_attribs=True)
class PipelinesGetLogsResponse200:
    """  Successful response to pipeline creation request.

        Attributes:
            status (PipelinesGetLogsResponse200Status):  Record query status
            cursor (Union[Unset, None, str]):  Cursor to request next page of results
            records (Union[Unset, None, PipelinesGetLogsResponse200Records]):
     """

    status: PipelinesGetLogsResponse200Status
    cursor: Union[Unset, None, str] = UNSET
    records: Union[Unset, None, 'PipelinesGetLogsResponse200Records'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        cursor = self.cursor
        records: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.records, Unset):
            records = self.records.to_dict() if self.records else None


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
        })
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pipelines_get_logs_response_200_records import \
            PipelinesGetLogsResponse200Records
        d = src_dict.copy()
        status = PipelinesGetLogsResponse200Status(d.pop("status"))




        cursor = d.pop("cursor", UNSET)

        _records = d.pop("records", UNSET)
        records: Union[Unset, None, PipelinesGetLogsResponse200Records]
        if _records is None:
            records = None
        elif isinstance(_records,  Unset):
            records = UNSET
        else:
            records = PipelinesGetLogsResponse200Records.from_dict(_records)




        pipelines_get_logs_response_200 = cls(
            status=status,
            cursor=cursor,
            records=records,
        )

        pipelines_get_logs_response_200.additional_properties = d
        return pipelines_get_logs_response_200

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
