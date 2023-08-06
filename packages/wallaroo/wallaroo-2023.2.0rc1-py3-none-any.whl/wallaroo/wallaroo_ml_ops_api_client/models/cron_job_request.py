from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.cron_job_request_json import CronJobRequestJson





T = TypeVar("T", bound="CronJobRequest")


@attr.s(auto_attribs=True)
class CronJobRequest:
    """ 
        Attributes:
            json (CronJobRequestJson):
            name (str):
            orch_id (str):
            schedule (str):
            workspace_id (int):
            timeout (Union[Unset, None, int]):
     """

    json: 'CronJobRequestJson'
    name: str
    orch_id: str
    schedule: str
    workspace_id: int
    timeout: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        json = self.json.to_dict()

        name = self.name
        orch_id = self.orch_id
        schedule = self.schedule
        workspace_id = self.workspace_id
        timeout = self.timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "json": json,
            "name": name,
            "orch_id": orch_id,
            "schedule": schedule,
            "workspace_id": workspace_id,
        })
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cron_job_request_json import CronJobRequestJson
        d = src_dict.copy()
        json = CronJobRequestJson.from_dict(d.pop("json"))




        name = d.pop("name")

        orch_id = d.pop("orch_id")

        schedule = d.pop("schedule")

        workspace_id = d.pop("workspace_id")

        timeout = d.pop("timeout", UNSET)

        cron_job_request = cls(
            json=json,
            name=name,
            orch_id=orch_id,
            schedule=schedule,
            workspace_id=workspace_id,
            timeout=timeout,
        )

        cron_job_request.additional_properties = d
        return cron_job_request

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
