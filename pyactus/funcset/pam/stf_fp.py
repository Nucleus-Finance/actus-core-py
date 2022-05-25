# ************************************
# N.B. Auto-initialised using actus-mp
# ************************************
import datetime
from pyactus.typeset import TermsForPrincipalAtMaturity as ContractTerms
from pyactus.typeset import StateSpace


def execute(
    time: datetime.datetime,
    states: object,
    terms: ContractTerms,
    risk_factor_model: object,
    day_counter: object,
    time_adjuster: object
) -> StateSpace:
    """Executes a PAM contract FP state transition function.
    
    :param time: The schedule time of this particular event.
    :param states: The current state of contract states.
    :param terms: The set of contract terms.
    :param risk_factor_model: An external market model.
    :param day_counter: The day count convention used to calculate day count fractions.
    :param time_adjuster: The business day convention used to shift the schedule time.
    :returns: An array of post-event states of numerical contract states.

    """
    raise NotImplementedError()