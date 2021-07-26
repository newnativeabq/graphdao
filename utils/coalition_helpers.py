# coalition_helpers

from typing import List 

from primitives.resources import Coalition, Function
from primitives.actions import Action

from .simple_functions import requires

def build_coalition_member_requirements(coalition: Coalition) -> List[Action]:
    requirements = []
    for actor in coalition.actors:
        requirements.append(
            Action(
                identifier=f'requires_{actor.identifier}',
                actor=coalition,
                resources=[actor],
                function = Function(
                    identifier=f'requires_{actor.identifier}',
                    kwargs={'resource_a': coalition, 'resource_b': actor},
                    fn=requires,
                )
            )
        )
    return requirements