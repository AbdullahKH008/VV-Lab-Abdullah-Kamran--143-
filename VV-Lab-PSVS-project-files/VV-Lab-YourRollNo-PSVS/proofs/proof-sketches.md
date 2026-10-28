# Proof Sketches

## Deposit Preserves Invariants

Assume the pre-state satisfies `VaultState` and the Deposit preconditions hold.

1. `d? ∈ registered`, so only a registered depositor can deposit.
2. `b? ∉ dom status`, so the new box does not overwrite an existing box status.
3. The chamber-load precondition requires current load to be strictly less than capacity.
4. Deposit adds exactly one stored box to the chosen chamber, so the new load is at most capacity.
5. The new box receives one owner, one species, one location, and stored status.
6. Temperature, capacity, registration, and maintenance mode are unchanged.

Therefore the ownership, location, capacity, and temperature invariants are preserved, assuming the input chamber is a valid chamber and the schema's partial-function updates are well-typed.

## Withdraw Preserves Invariants

Assume the pre-state satisfies `VaultState` and the ordinary Withdraw preconditions hold.

1. The box exists and is stored.
2. The requesting depositor equals the recorded owner.
3. Ownership and species are unchanged.
4. The status changes from `stored` to `withdrawn`.
5. The box is removed from the stored location mapping, reducing the load of its chamber by one.
6. No chamber load can increase, so capacity remains satisfied.
7. Temperature, capacity, registration, and maintenance mode remain unchanged.

Therefore the modeled invariants are preserved.

## StartMaintenance Preserves Invariants

Assume the pre-state satisfies `VaultState`. StartMaintenance adds the chamber to `maintenanceMode` and leaves temperature unchanged. Since a non-maintenance chamber already has temperature ≤ -18°C, after entering maintenance it satisfies the relaxed maintenance bound ≤ 0°C. Other state components are unchanged, so ownership, location, status, species, and capacity invariants remain satisfied.
