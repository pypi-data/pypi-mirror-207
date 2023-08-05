import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.region_state import RegionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegionStateViewModel")


@attr.s(auto_attribs=True)
class RegionStateViewModel:
    """
    Attributes:
        from_ (Union[Unset, datetime.datetime]):
        to (Union[Unset, datetime.datetime]):
        state (Union[Unset, RegionState]): <p>Possible values:</p>
            <ul>
            <li><b>1</b> = green</li>
            <li><b>2</b> = yellow</li>
            <li><b>3</b> = orange</li>
            <li><b>4</b> = red</li>
            </ul>
    """

    from_: Union[Unset, datetime.datetime] = UNSET
    to: Union[Unset, datetime.datetime] = UNSET
    state: Union[Unset, RegionState] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_: Union[Unset, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: Union[Unset, str] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, datetime.datetime]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, datetime.datetime]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        _state = d.pop("state", UNSET)
        state: Union[Unset, RegionState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RegionState(_state)

        region_state_view_model = cls(
            from_=from_,
            to=to,
            state=state,
        )

        return region_state_view_model
