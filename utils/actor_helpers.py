# actor_helpers.py

from typing import List 

from primitives.resources import Actor, Function
from primitives.actions import Action

from .simple_functions import requires

def build_actor_consensus_requirements(actor: Actor) -> List[Action]:
    requirements = []
    if hasattr(actor.consensus.fn, 'identifier'):
        resources = actor.consensus.fn.kwargs.values()
        for resource in resources:
            # print(resource, type(resource))  # Debug
            requirements.append(
                Action(
                    identifier=f'requires_{resource.identifier}',
                    actor=actor,
                    resources=[resource],
                    function = Function(
                        identifier=f'requires_{actor.identifier}',
                        kwargs={'resource_a': actor, 'resource_b': resource},
                        fn=requires,
                    )
                )
            )
    return requirements