# Primitives & Assemblies
**Specifically, governance primitives**

Primitives for the purpose of govern ance may be a resource or atomic instructions of active resource (individual/actor, dyad, coalition) on another resource.  A primitive is linearizable.  A system of primitives may not be.

## Resources:
- actor
- wallet or account?
- data store or register?
- oracle (external data interface?)
- interface (?)

### Actors
An actor is a unique resource in that it can sign a transaction (can be used to authorize function output, validate data) if consensus in the acting body is reached.  For an individual entity, it's a given that the actor wants to 'act'. For multi-actor entities, various consesus structure might be used.
- Entity - Single actor. Consensus always true.
- Dyad - Dual actor. Consensus all or nothing, 50/50 unweighted, 50/50 weighted.
- Coalition - >2 actors. Consensus all or nothing, fractional weighted, fracional unweighted.

### Wallet/Account
A wallet or account is a unique resource in that it is a pointer to a collection of concrete resources with a sense of contains or not contains.  Transactions can be validated on whether the wallet has funds or tokens intended for transaction.

### Data Store/Register
Data stores internal to the DAO can store start times, steps, votes, cache oracle data or more.  DAO data store states are controlled by instructions within the DAO and not external entities.

### Oracle
An external data provider.  Includes user input, API fetches, and more.

## Instructions:
Actions actors can take.
- read-write
- compare-and-swap
- fetch-and-add
- (debug) Print (I/O, stderr, etc.)

**Functions required for transactions:**
- Validator
- Redeemer


## Higher Order Assemblies
Primitives may be combined into useful higher order structures to run a DAO.  

**Examples**
- Counter: 
- - Resources: actor, data store
- - Instructions: fetch-and-add, read-write
- Timer:
- - Resources: actor, oracle, data store
- - Instructions: read-write, compare-and-swap
- Transaction:
- - Resources: actor, wallet
- - Instructions: redeemer, validator


### References
1. Linearizability: https://en.wikipedia.org/wiki/Linearizability