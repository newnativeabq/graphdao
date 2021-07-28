# interfaces.py

from primitives.resources import Resource, Data, Function
from primitives.actions import Action
from utils.simple_functions import null_fn
from typing import List, Any

class Interface(Resource):
    data: List[Data]
    fn: Any = null_fn
    
    def read(self, *args, **kwargs):
        if len(self.data) == 1:
            return self.data[0].read(*args, **kwargs)
        else:
            return [data.read(*args, **kwargs) for data in self.data]
    
    def write(self, *args, **kwargs):
        if len(self.data) == 1:
            return self.data[0].write(*args, **kwargs)
        else:
            raise NotImplementedError("Multi data source write interface not implemented.")

    @property
    def actions(self):
        return [
            Action(
            identifier=self.identifier,
            actor=self,
            resources=[data],
            function=Function(
                identifier=f'{self.identifier}_{data.identifier}',
                kwargs={'interface':self},
                fn=self.fn
                )
            )
            for data in self.data
        ]