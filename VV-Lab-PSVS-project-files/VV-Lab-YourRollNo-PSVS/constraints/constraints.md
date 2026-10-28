# Constraints and Exception Modeling

## Chamber Capacities (S3)

- Chambers 1, 2, and 3 have capacity 50,000 each.
- Chamber 4 has capacity 20,000.
- For every chamber `c`, stored-box count must be less than or equal to `capacity(c)`.

## Annual Withdrawal Quota (S10)

**Time model:** ASSUMPTION-7 — calendar year.

**Rounding model:** ASSUMPTION-8 — floor 20% of the eligible count of the depositor's boxes of a species at the start of the year.

For depositor `d` and species `s` in year `y`:

`withdrawals(d,s,y) <= floor(0.20 * eligibleBoxesAtYearStart(d,s,y))`

The denominator and the yearly counter must be fixed at the start of each calendar year to avoid changing the quota as boxes are withdrawn.

## Emergency Override (S5)

An emergency release is permitted only when the vault authority has declared an emergency and authorized the release. It is an explicit exception to the ordinary owner-only rule in S4. The event must be recorded in the audit trail.

## Redeposit After Inspection (S11)

A withdrawn box may be redeposited only if its inspection result is recorded as passed and the destination chamber has capacity.

## Withdrawal Schemas

The operation specification must distinguish success from errors. The following are schema-level cases to implement in the formal specification:

- `WithdrawOK`
- `NotOwner`
- `ChamberInMaintenance`
- `QuotaExceeded`
- `BoxNotStored`
- `UnknownBox`

Each error case must return `report! : REPORT`.

## Error Priority

Use this priority order where cases overlap:

1. `UnknownBox`
2. `BoxNotStored`
3. `ChamberInMaintenance`
4. `NotOwner`
5. `QuotaExceeded`

An emergency-authorized release is evaluated as an explicit override of `NotOwner`; it does not bypass unknown-box, box-status, or chamber safety checks.
