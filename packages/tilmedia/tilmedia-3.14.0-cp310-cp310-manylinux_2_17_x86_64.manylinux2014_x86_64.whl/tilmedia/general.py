from typing import List, Union, Dict
from . import core


class LiquidMixtureInformation:
    def __init__(
        self,
        supports_mass_fraction: bool = None,
        supports_volume_fraction: bool = None,
        minimum_mass_fraction: float = None,
        maximum_mass_fraction: float = None,
        minimum_volume_fraction: float = None,
        maximum_volume_fraction: float = None,
    ):
        self.supports_mass_fraction: bool = supports_mass_fraction
        "This medium supports setting the composition as mass fraction, and therefore all xi based function can be used."
        self.supports_volume_fraction: bool = supports_volume_fraction
        "This medium supports setting the composition as volume fraction."
        self.minimum_mass_fraction: float = minimum_mass_fraction if minimum_mass_fraction >= 0 else None
        self.maximum_mass_fraction: float = maximum_mass_fraction if maximum_mass_fraction >= 0 else None
        self.minimum_volume_fraction: float = minimum_volume_fraction if minimum_volume_fraction >= 0 else None
        self.maximum_volume_fraction: float = maximum_volume_fraction if maximum_volume_fraction >= 0 else None
        self._property_list = [
            "supports_mass_fraction",
            "supports_volume_fraction",
            "minimum_mass_fraction",
            "maximum_mass_fraction",
            "minimum_volume_fraction",
            "maximum_volume_fraction",
        ]

    def __str__(self):
        return "\n".join(
            f"{name} = {round(getattr(self, name),5) if name.startswith('m') else getattr(self, name)}"
            for name in self._property_list
            if getattr(self, name) is not None
        )

    def __repr__(self):
        return ", ".join(
            f"{name} = {round(getattr(self, name),5) if name.startswith('m') else getattr(self, name)}"
            for name in self._property_list
            if getattr(self, name) is not None
        )


def clear_medium_name_cache():
    """
    Clear the name cache. This might be required if the data path has been changed.
    """
    core.clear_medium_name_cache()


def get_all_liquid_names() -> List[str]:
    """
    Get the list of Liquid names

    Returns:
        list: list of Liquid names
    """
    return core.get_all_liquid_names()


def get_all_liquid_mixture_names() -> Dict[str, LiquidMixtureInformation]:
    """
    Get the list of Liquid names

    Returns:
        list: list of Liquid names
    """
    return dict((key, LiquidMixtureInformation(**value)) for key, value in core.get_all_liquid_mixture_names().items())


def get_all_gas_names() -> List[str]:
    """
    Get the list of Gas names

    Returns:
        list: list of Gas names
    """
    return core.get_all_gas_names()


def get_all_condensing_gas_names() -> List[str]:
    """
    Get the list of Condensing Gas names

    Returns:
        list: list of Condensing Gas names
    """
    return core.get_all_condensing_gas_names()


def get_all_vleFluid_names() -> List[str]:
    """
    Get the list of VLEFluid names

    Returns:
        list: list of VLEFluid names
    """
    return core.get_all_vleFluid_names()


def get_all_adsorption_and_absorption_names() -> List[str]:
    """
    Get the list of medium names

    Returns:
        list: list of medium names
    """
    return core.get_all_adsorption_and_absorption_names()


def get_data_path() -> Union[None, str]:
    """
    Get the TILMediaDataPath

    Returns:
        str : Data path of TILMedia
    """
    return core.get_data_path()


def set_data_path(path: str):
    """
    Set the TILMediaDataPath

    Args:
        path (str): Data path of TILMedia
    """
    core.set_data_path(path)


def license_is_valid() -> bool:
    """
    Check if the TILMedia License is valid.
    """
    return core.license_is_valid()


def get_closest_vleFluid_dpT(d: float, p: float, T: float) -> Union[None, str]:
    """
    detect medium name for a given critical point of a VLEFluid

    Args:
        d (float): critical density
        p (float): critical pressure
        T (float): critical temperature

    Returns:
        str: medium name
    """
    return core.get_closest_vleFluid_dpT(d, p, T)
