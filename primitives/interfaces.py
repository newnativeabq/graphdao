# interfaces.py

from primitives.resources import Resource, Data, Function
from primitives.actions import Action
from utils.simple_functions import null_fn
from typing import Optional, Any

class Interface(Resource):
    data: Data
    fn: Any = null_fn
    
    def read(self, *args, **kwargs):
        return self.data.read(*args, **kwargs)
    
    def write(self, *args, **kwargs):
        return self.data.write(*args, **kwargs)

    @property
    def actions(self):
        return [Action(
            identifier=self.identifier,
            actor=self,
            resources=[self.data],
            function=Function(
                identifier=f'{self.identifier}_{self.data.identifier}',
                kwargs={'interface':self},
                fn=self.fn
            )
        )]