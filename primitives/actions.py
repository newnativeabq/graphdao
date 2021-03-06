# actions.py

from pydantic import BaseModel
from typing import List, Any

from .resources import Resource, Function
    

class Action(BaseModel):
    identifier: str
    resources: List[Resource]
    function: Function
    actor: Any
        
    @property
    def nodes(self) -> list:
        n = []
        n.extend([r.identifier for r in self.resources])
        n.extend([self.actor.identifier])
        return n
    
    @property
    def edges(self) -> list:
        e = []
        e.extend([(self.actor.identifier, r.identifier, {'function':self.function}) for r in self.resources])
        return e
    
    def execute(self):
        return self.function.execute()