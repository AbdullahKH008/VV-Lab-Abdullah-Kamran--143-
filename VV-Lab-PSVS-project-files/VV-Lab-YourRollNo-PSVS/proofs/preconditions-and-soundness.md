# Pre/Post Reasoning and Soundness

## Preconditions

### Deposit

The simplified precondition is:

- `d? ∈ registered`
- `b? ∉ dom status`
- `c? ∈ dom capacity`
- `load(c?) < capacity(c?)`

These are the registration, uniqueness, valid-chamber, and available-capacity checks.

**Witness:** An empty vault, registered depositor `d1`, new box `b1`, and chamber `c1` with capacity 50,000 satisfy the precondition.

### Withdraw

For the ordinary successful operation:

- `b? ∈ dom status`
- `status(b?) = stored`
- `owner(b?) = d?`
- the box's chamber is not in maintenance mode
- the quota for the depositor/species/year has not been exceeded

**Witness:** Let `b1` be stored in `c1`, owned by registered depositor `d1`, with `c1` not in maintenance and quota remaining. Requesting withdrawal by `d1` satisfies the precondition.

### StartMaintenance

The simplified precondition is `c? ∈ dom temp` and the chamber is not already in maintenance mode.

**Witness:** A chamber `c1` exists in `dom temp` and is not in `maintenanceMode`.

## Invariant Preservation

The Deposit and StartMaintenance proof sketches are in `proof-sketches.md`.

## Total-Operation Coverage

The exception cases need to cover every input/state combination. Check combinations involving unknown box, non-stored box, maintenance, non-owner, quota exceeded, and emergency authorization. The schema definitions must be type-checked and reviewed for overlap in the chosen formal tool before claiming complete coverage.

## Capacity Counterexample

Suppose a chamber has capacity 50,000 and currently stores 50,000 boxes. If Deposit omits the capacity precondition, a new deposit can produce load 50,001, violating `load(c) ≤ capacity(c)`. Restoring `load(c?) < capacity(c?)` prevents this counterexample.

## Reflection on Lab 2

Complete this reflection based on the actual defects identified in Lab 2. Compare defects found by informal review with those exposed by formalization, especially capacity, temperature, ownership, emergency override, and annual quota constraints. Do not claim a defect was missed by informal review unless your Lab 2 record supports that comparison.

## Midterm Viva Verification Summary

The model represents depositors, boxes, chambers, species, status, ownership, location, capacity, temperature, and maintenance mode. Core invariants constrain ownership/location for stored boxes, chamber capacity, and temperature. Deposit, Withdraw, Redeposit, StartMaintenance, and QueryChamberLoad describe key state changes and observations. Remaining verification work includes running a compatible Z type-checker, reviewing total-operation coverage, checking exception overlap, and attaching actual tool output.
