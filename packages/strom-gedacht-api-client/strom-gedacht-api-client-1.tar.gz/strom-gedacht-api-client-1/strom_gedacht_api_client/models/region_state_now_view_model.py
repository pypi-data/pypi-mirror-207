from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.region_state import RegionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegionStateNowViewModel")


@attr.s(auto_attribs=True)
class RegionStateNowViewModel:
    """
    Attributes:
        state (Union[Unset, RegionState]): <p>Possible values:</p>
            <ul>
            <li><b>1</b> = green</li>
            <li><b>2</b> = yellow</li>
            <li><b>3</b> = orange</li>
            <li><b>4</b> = red</li>
            </ul>
    """

    state: Union[Unset, RegionState] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, RegionState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RegionState(_state)

        region_state_now_view_model = cls(
            state=state,
        )

        return region_state_now_view_model
