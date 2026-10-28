# Verification Summary

## Scope

This report summarizes the requirements and formal model for the polar seed vault.

## Main Checks

- Registration is checked before deposit.
- Stored boxes have an owner and chamber location.
- Chamber occupancy is bounded by its capacity.
- Temperature is at most -18°C outside maintenance mode and at most 0°C during maintenance mode.
- Ordinary withdrawal checks box status and ownership.
- Redeposit requires successful re-inspection.
- Annual withdrawal quota and emergency release are described in the constraints specification.
- Audit records are required for operations.

## Evidence Status

The proof sketches and witness states are documented in `proofs/`. A real Z type-checker output must be attached after running the specification through a compatible tool. Peer-review results must be filled using the actual classmate comparison. The detection rate and chart should be finalized from the resulting review data.

## Viva Points

Be prepared to explain the state invariants, how Deposit preserves capacity, why Withdraw preserves ownership, how the maintenance exception resolves the temperature conflict, and how emergency release interacts with owner-only withdrawal.
