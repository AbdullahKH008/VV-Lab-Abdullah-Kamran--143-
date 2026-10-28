# Pre-Formal Abstraction

## Entities and Attributes

| Entity | Attributes |
|---|---|
| Depositor | depositorId, registered |
| Box | boxId, owner, species, status, location, viability, inspected |
| Chamber | chamberId, capacity, temperature, maintenanceMode |
| Species | speciesId, name, viabilityThreshold |

## Relationships

- A box has exactly one depositor as owner.
- A box contains samples of one species.
- A stored box is located in one chamber.
- A chamber contains zero or more stored boxes.
- A depositor may own multiple boxes.
- A species may be represented by multiple boxes.

## Operations

- Deposit
- Withdraw
- Redeposit
- MoveBox
- DeclareEmergency
