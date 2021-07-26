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
            return self.fn(**self.kwargs)
        except Exception as e:
            print('Error: could not execute function')
            raise e

    def __call__(self):
        return self.execute()

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
            raise ValueError(f'{self.identifier} Consensus not True')


######################
### Data & Oracles ###
######################

class Data(Resource):
    store: Any

    def read(self, *args, **kwargs):
        return self.store


class DemoData(Data): 
    
    def read(self, *args, **kwargs):  ## Can be defined in interface
        return self.store
    
    def write(self, *args, **kwargs):  ## Can be defined in interface
        if len(args) > 0:
            self.store.extend(args)
        elif len(kwargs) > 0:
            for key in kwargs:
                self.store.append({key:kwargs[key]})


class UserInput(Data):
    message: Any
    validator: Any

    def prepare_message(self):
        # If not a string, assume a callable
        if type(self.message) == str:
            return self.message
        return self.message()

    def validate(self, data):
        if hasattr(self, 'validator'):
            if self.validator is not None:
                return self.validator(data)
        return data

    def read(self):
        message = self.prepare_message()
        self.store = input(message)
        return super().read()
