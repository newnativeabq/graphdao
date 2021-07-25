# resources.py

from pydantic import BaseModel
from typing import List, Dict, Any

from utils.signatures import add_general_signature

#######################
### Basic Primitives ##
#######################

class Resource(BaseModel):
    identifier: str

    def __repr__(self):
        return self.identifier
    

class Consensus(BaseModel):
    fn: Any
        
    def resolve(self, *args, **kwargs):
        return self.fn(*args, **kwargs)


class Function(BaseModel):
    identifier: str
    kwargs: Dict[str, Resource]
    fn: Any
    
    def execute(self):
        try:
            self.fn(self.kwargs)
        except Exception as e:
            print('Error: could not execute function')
            raise e

#############################################
### Actors and Acting Bodies (Coalitions) ###
#############################################

class Actor(Resource):
    identifier: str
    consensus: Consensus
    key: str
    
    def __repr__(self):
        return self.identifier
    
    def sign(self, transaction):
        # Add a signature
        if self.consensus.resolve():
            return add_general_signature(self.identifier, self.key, transaction)
        else:
            raise ValueError(f'{self.identifer} Consensus not True')


class Coalition(Actor):
    actors: List[Actor]
        
    def sign(self, transaction):
        if self.consensus.resolve(self.actors):
            for actor in self.actors:
                add_general_signature(actor.identifier, actor.key, transaction)
            return transaction
        else:
            raise ValueError(f'{self.identifer} Consensus not True')


######################
### Data & Oracles ###
######################

class Data(Resource):
    store: List[Any]


class DemoData(Data): 
    
    def read(self, *args, **kwargs):  ## Can be defined in interface
        return self.store
    
    def write(self, *args, **kwargs):  ## Can be defined in interface
        if len(args) > 0:
            self.store.extend(args)
        elif len(kwargs) > 0:
            for key in kwargs:
                self.store.append({key:kwargs[key]})


class Interface(Resource):
    data: Data
    
    def read(self, *args, **kwargs):
        return self.data.read(*args, **kwargs)
    
    def write(self, *args, **kwargs):
        return self.data.write(*args, **kwargs)


class Oracle(Actor):
    interface: Interface
    data: Data
        
    def collect(self):
        if self.consensus.resolve():
            return self.interface.read()
        
    # Oracles have an associated action.
    #  Register the Action to build the graph
    @property
    def action(self) -> Action:
        return Action(
            identifier=self.identifier,
            resources=[self.interface, self.data],
            function=self.build_oracle_function(),
            actor=self.interface,
        )
    
    def build_oracle_function(self):
        return Function(
            identifier=self.identifier,
            kwargs={'interface': interface},
            fn=build_read_from_interface(interface)
        )
