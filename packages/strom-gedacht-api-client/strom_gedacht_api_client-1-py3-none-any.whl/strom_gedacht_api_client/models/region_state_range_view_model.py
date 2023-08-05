from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.region_state_view_model import RegionStateViewModel


T = TypeVar("T", bound="RegionStateRangeViewModel")


@attr.s(auto_attribs=True)
class RegionStateRangeViewModel:
    """
    Attributes:
        states (Union[Unset, None, List['RegionStateViewModel']]):
    """

    states: Union[Unset, None, List["RegionStateViewModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        states: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.states, Unset):
            if self.states is None:
                states = None
            else:
                states = []
                for states_item_data in self.states:
                    states_item = states_item_data.to_dict()

                    states.append(states_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if states is not UNSET:
            field_dict["states"] = states

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.region_state_view_model import RegionStateViewModel

        d = src_dict.copy()
        states = []
        _states = d.pop("states", UNSET)
        for states_item_data in _states or []:
            states_item = RegionStateViewModel.from_dict(states_item_data)

            states.append(states_item)

        region_state_range_view_model = cls(
            states=states,
        )

        return region_state_range_view_model
