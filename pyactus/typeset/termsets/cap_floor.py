# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime
import typing

from pyactus.typeset import enums
from pyactus.typeset import auxiliary
from pyactus.typeset import contracts


@dataclasses.dataclass
class TermsetOfCapFloor(contracts.ContractTermset):
    """Set of applicable terms: CAPFL -> Cap Floors.

    Interest rate option expressed in a maximum or minimum interest rate.

    """
    # Contract Deal Date.
    contract_deal_date: datetime.datetime = None

    # Contract Identifier.
    contract_id: str = None

    # Contract Performance.
    contract_performance: enums.ContractPerformance = enums.ContractPerformance.PF

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Structure.
    contract_structure: typing.List[auxiliary.ContractReference] = None

    # Counterparty Identifier.
    counterparty_id: str = None

    # Creator Identifier.
    creator_id: str = None

    # Currency.
    currency: str = None

    # Delinquency Period.
    delinquency_period: auxiliary.Period = None

    # Delinquency Rate.
    delinquency_rate: float = 0.0

    # Grace Period.
    grace_period: auxiliary.Period = None

    # Life Cap.
    life_cap: float = None

    # Life Floor.
    life_floor: float = None

    # Market Object Code.
    market_object_code: str = None

    # Market Value Observed.
    market_value_observed: float = None

    # Non Performing Date.
    non_performing_date: datetime.datetime = None

    # Price At Purchase Date.
    price_at_purchase_date: float = None

    # Price At Termination Date.
    price_at_termination_date: float = None

    # Purchase Date.
    purchase_date: datetime.datetime = None

    # Seniority.
    seniority: enums.Seniority = None

    # Settlement Currency.
    settlement_currency: str = None

    # Status Date.
    status_date: datetime.datetime = None

    # Termination Date.
    termination_date: datetime.datetime = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a contract. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.CAPFL
