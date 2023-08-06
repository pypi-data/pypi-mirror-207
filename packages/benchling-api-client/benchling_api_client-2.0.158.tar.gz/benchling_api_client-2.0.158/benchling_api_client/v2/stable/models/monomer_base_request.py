from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.monomer_visual_symbol import MonomerVisualSymbol
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonomerBaseRequest")


@attr.s(auto_attribs=True, repr=False)
class MonomerBaseRequest:
    """  """

    _custom_molecular_weight: Union[Unset, None, float] = UNSET
    _name: Union[Unset, str] = UNSET
    _natural_analog: Union[Unset, str] = UNSET
    _smiles: Union[Unset, str] = UNSET
    _symbol: Union[Unset, str] = UNSET
    _visual_color: Union[Unset, None, str] = UNSET
    _visual_symbol: Union[Unset, MonomerVisualSymbol] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def __repr__(self):
        fields = []
        fields.append("custom_molecular_weight={}".format(repr(self._custom_molecular_weight)))
        fields.append("name={}".format(repr(self._name)))
        fields.append("natural_analog={}".format(repr(self._natural_analog)))
        fields.append("smiles={}".format(repr(self._smiles)))
        fields.append("symbol={}".format(repr(self._symbol)))
        fields.append("visual_color={}".format(repr(self._visual_color)))
        fields.append("visual_symbol={}".format(repr(self._visual_symbol)))
        fields.append("additional_properties={}".format(repr(self.additional_properties)))
        return "MonomerBaseRequest({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        custom_molecular_weight = self._custom_molecular_weight
        name = self._name
        natural_analog = self._natural_analog
        smiles = self._smiles
        symbol = self._symbol
        visual_color = self._visual_color
        visual_symbol: Union[Unset, int] = UNSET
        if not isinstance(self._visual_symbol, Unset):
            visual_symbol = self._visual_symbol.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if custom_molecular_weight is not UNSET:
            field_dict["customMolecularWeight"] = custom_molecular_weight
        if name is not UNSET:
            field_dict["name"] = name
        if natural_analog is not UNSET:
            field_dict["naturalAnalog"] = natural_analog
        if smiles is not UNSET:
            field_dict["smiles"] = smiles
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if visual_color is not UNSET:
            field_dict["visualColor"] = visual_color
        if visual_symbol is not UNSET:
            field_dict["visualSymbol"] = visual_symbol

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_custom_molecular_weight() -> Union[Unset, None, float]:
            custom_molecular_weight = d.pop("customMolecularWeight")
            return custom_molecular_weight

        try:
            custom_molecular_weight = get_custom_molecular_weight()
        except KeyError:
            if strict:
                raise
            custom_molecular_weight = cast(Union[Unset, None, float], UNSET)

        def get_name() -> Union[Unset, str]:
            name = d.pop("name")
            return name

        try:
            name = get_name()
        except KeyError:
            if strict:
                raise
            name = cast(Union[Unset, str], UNSET)

        def get_natural_analog() -> Union[Unset, str]:
            natural_analog = d.pop("naturalAnalog")
            return natural_analog

        try:
            natural_analog = get_natural_analog()
        except KeyError:
            if strict:
                raise
            natural_analog = cast(Union[Unset, str], UNSET)

        def get_smiles() -> Union[Unset, str]:
            smiles = d.pop("smiles")
            return smiles

        try:
            smiles = get_smiles()
        except KeyError:
            if strict:
                raise
            smiles = cast(Union[Unset, str], UNSET)

        def get_symbol() -> Union[Unset, str]:
            symbol = d.pop("symbol")
            return symbol

        try:
            symbol = get_symbol()
        except KeyError:
            if strict:
                raise
            symbol = cast(Union[Unset, str], UNSET)

        def get_visual_color() -> Union[Unset, None, str]:
            visual_color = d.pop("visualColor")
            return visual_color

        try:
            visual_color = get_visual_color()
        except KeyError:
            if strict:
                raise
            visual_color = cast(Union[Unset, None, str], UNSET)

        def get_visual_symbol() -> Union[Unset, MonomerVisualSymbol]:
            visual_symbol = UNSET
            _visual_symbol = d.pop("visualSymbol")
            if _visual_symbol is not None and _visual_symbol is not UNSET:
                try:
                    visual_symbol = MonomerVisualSymbol(_visual_symbol)
                except ValueError:
                    visual_symbol = MonomerVisualSymbol.of_unknown(_visual_symbol)

            return visual_symbol

        try:
            visual_symbol = get_visual_symbol()
        except KeyError:
            if strict:
                raise
            visual_symbol = cast(Union[Unset, MonomerVisualSymbol], UNSET)

        monomer_base_request = cls(
            custom_molecular_weight=custom_molecular_weight,
            name=name,
            natural_analog=natural_analog,
            smiles=smiles,
            symbol=symbol,
            visual_color=visual_color,
            visual_symbol=visual_symbol,
        )

        monomer_base_request.additional_properties = d
        return monomer_base_request

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

    def get(self, key, default=None) -> Optional[Any]:
        return self.additional_properties.get(key, default)

    @property
    def custom_molecular_weight(self) -> Optional[float]:
        """ Optional molecular weight value that the user can provide to override the calculated molecular weight """
        if isinstance(self._custom_molecular_weight, Unset):
            raise NotPresentError(self, "custom_molecular_weight")
        return self._custom_molecular_weight

    @custom_molecular_weight.setter
    def custom_molecular_weight(self, value: Optional[float]) -> None:
        self._custom_molecular_weight = value

    @custom_molecular_weight.deleter
    def custom_molecular_weight(self) -> None:
        self._custom_molecular_weight = UNSET

    @property
    def name(self) -> str:
        """ Name of the monomer """
        if isinstance(self._name, Unset):
            raise NotPresentError(self, "name")
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @name.deleter
    def name(self) -> None:
        self._name = UNSET

    @property
    def natural_analog(self) -> str:
        """ Symbol for the natural equivalent of the monomer. Acceptable natural analog values include IUPAC bases, r, and p. """
        if isinstance(self._natural_analog, Unset):
            raise NotPresentError(self, "natural_analog")
        return self._natural_analog

    @natural_analog.setter
    def natural_analog(self, value: str) -> None:
        self._natural_analog = value

    @natural_analog.deleter
    def natural_analog(self) -> None:
        self._natural_analog = UNSET

    @property
    def smiles(self) -> str:
        """ The chemical structure in SMILES format. """
        if isinstance(self._smiles, Unset):
            raise NotPresentError(self, "smiles")
        return self._smiles

    @smiles.setter
    def smiles(self, value: str) -> None:
        self._smiles = value

    @smiles.deleter
    def smiles(self) -> None:
        self._smiles = UNSET

    @property
    def symbol(self) -> str:
        """ User-defined identifier of the monomer, unique on the monomer type. """
        if isinstance(self._symbol, Unset):
            raise NotPresentError(self, "symbol")
        return self._symbol

    @symbol.setter
    def symbol(self, value: str) -> None:
        self._symbol = value

    @symbol.deleter
    def symbol(self) -> None:
        self._symbol = UNSET

    @property
    def visual_color(self) -> Optional[str]:
        """ The hex color code of the monomer visual symbol """
        if isinstance(self._visual_color, Unset):
            raise NotPresentError(self, "visual_color")
        return self._visual_color

    @visual_color.setter
    def visual_color(self, value: Optional[str]) -> None:
        self._visual_color = value

    @visual_color.deleter
    def visual_color(self) -> None:
        self._visual_color = UNSET

    @property
    def visual_symbol(self) -> MonomerVisualSymbol:
        """ The shape of the monomer visual symbol. """
        if isinstance(self._visual_symbol, Unset):
            raise NotPresentError(self, "visual_symbol")
        return self._visual_symbol

    @visual_symbol.setter
    def visual_symbol(self, value: MonomerVisualSymbol) -> None:
        self._visual_symbol = value

    @visual_symbol.deleter
    def visual_symbol(self) -> None:
        self._visual_symbol = UNSET
