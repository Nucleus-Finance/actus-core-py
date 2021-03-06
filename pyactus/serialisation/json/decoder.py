import dataclasses
import datetime

from pyactus.typeset import CONTRACT_TERMSETS
from pyactus.typeset import ENUM_SET
from pyactus.typeset import Contract
from pyactus.typeset import ContractIdentifier
from pyactus.typeset import ContractLifeCycleEpisode
from pyactus.typeset import ContractReference
from pyactus.typeset import ContractTermset
from pyactus.typeset import ContractType
from pyactus.typeset import Cycle
from pyactus.typeset import Period
from pyactus.utils import convertors


def decode(obj: dict) -> object:
    """Maps an Actus contract in dictionary format to it's python type.

    """
    try:
        contract_type: ContractType = ContractType[obj["contract_type"]]
    except KeyError:
        raise ValueError("Invalid contract type")
    else:
        try:
            termset_cls: ContractTermset = CONTRACT_TERMSETS[contract_type]
        except KeyError:
            raise ValueError("Unsupported contract type")

    return Contract(
        contract_type=contract_type,
        identifiers=[_decode_identifier(i) for i in obj["identifiers"]],
        life_cycle=[_decode_life_cycle_episode(i, termset_cls) for i in obj["lifecycle"]]
        )


def _decode_identifier(obj: dict) -> ContractIdentifier:
    """Decodes a contract identifier, e.g. an ITIN.

    """
    return ContractIdentifier(
        scheme=obj["scheme"],
        value=obj["value"]
        )


def _decode_life_cycle_episode(obj: dict, termset_cls: ContractTermset) -> ContractLifeCycleEpisode:
    """Decodes a life cycle episode, i.e. a termset.

    """
    return ContractLifeCycleEpisode(
        term_set=_decode_term_set(obj, termset_cls),
        timestamp=convertors.to_iso_datetime(obj["timestamp"]),
    )


def _decode_term(field, value):
    """Decodes a term value associated with a financial contract.

    """
    if value is None:
        return _decode_term_when_null(field)
    elif field.type is datetime.datetime:
        return convertors.to_iso_datetime(value)
    elif field.type is float:
        return float(value)
    elif field.type is str:
        return str(value)
    elif field.type is Cycle:
        print("TODO: convert Cycle: ", field.name, value)
        return value
    elif field.type is Period:
        print("TODO: convert Period: ", field.name, value)
        return value
    elif field.type in ENUM_SET:
        # Some enum members begin with a numeric which is 
        # invalid in python, in these cases apply _ prefix.
        try:
            return field.type[value]
        except KeyError:
            try:
                return field.type[f"_{value}"]
            except KeyError:
                raise ValueError(f"Unsupported enum value: {field.type} :: {value}")
    else:
        raise ValueError(f"Unsupported field type: {field.type} :: {value}")


def _decode_term_set(obj: dict, termset_cls) -> ContractTermset:
    """Decodes a term set associated with a financial contract.

    """
    # Instantiate termset & map of term fields.
    termset = termset_cls()
    fields = {i.name: i for i in dataclasses.fields(termset_cls)}

    # For each encoded term, map to a field & assign value.
    for name, value in [i.values() for i in obj["term_set"]]:
        name = convertors.to_underscore_case(name)  # format jsonic name as pythonic name 
        try:
            field = fields[name]
        except KeyError:
            raise KeyError(f"Term name unknown: {termset_cls.__name__} :: {name} :: {value}")
        else:
            # print(field.name, field.type, value, _decode_term(field, value), type(_decode_term(field, value)))
            setattr(termset, name, _decode_term(field, value))

    return termset


def _decode_term_when_null(field):
    """Decodes a null term value associated with a financial contract.

    """
    if field.type is float:
        return float(0)
    else:
        return None
