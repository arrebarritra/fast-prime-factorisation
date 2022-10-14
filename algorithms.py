from functools import partial
from sympy.ntheory.factor_ import factorint, pollard_rho, pollard_pm1
from sympy.ntheory import ecm, qs

ALGORITHMS = {
    "Trial division": partial(factorint,
                                use_trial=True,
                                use_rho=False,
                                use_pm1=False,
                                use_ecm=False
    ),
    "Pollard's rho": pollard_rho,
    "Pollard's p-1": pollard_pm1,
    "Lenstra's elliptic curve": ecm,
    "Quadratic sieve": qs
}