# oracle_helpers

from typing import List 

from primitives.resources import Function
from primitives.actions import Action

from .simple_functions import requires

def build_oracle_requirements(oracle) -> List[Action]:
    requirements = []
    # Require interface exist
    requirements.append(
        Action(
            identifier=f'requires_{oracle.interface.identifier}',
            actor=oracle,
            resources=[oracle.interface],
            function = Function(
                identifier=f'requires_{oracle.interface.identifier}',
                kwargs={'resource_a': oracle, 'resource_b': oracle.interface},
                fn=requires,
            )
        )
    )
    return requirements