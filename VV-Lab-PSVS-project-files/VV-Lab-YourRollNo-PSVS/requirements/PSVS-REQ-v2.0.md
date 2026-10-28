# PSVS Requirements — Version 2.0

This version makes the original requirements more atomic and testable. Values not provided by the lab are identified as assumptions in `abstractions/clarifications.md`.

| ID | Revised requirement |
|---|---|
| S1 | The system shall accept a box for deposit only when the depositor identifier is in the registered-depositor set. |
| S2 | The system shall store each accepted box in a chamber whose occupancy does not exceed that chamber's capacity. |
| S3 | The system shall limit the occupancy of Chambers 1–3 to 50,000 boxes each and Chamber 4 to 20,000 boxes. |
| S4 | The system shall record exactly one owner for each box and shall permit an ordinary withdrawal only when the requesting depositor is that owner. |
| S5 | When an emergency has been declared by the vault authority, the system shall permit the authority-approved release of a box to a requesting party, subject to the emergency override rule. |
| S6 | The system shall maintain each chamber at or below -18°C except during authorized maintenance mode. |
| S7 | The system shall reject or alarm on a chamber temperature above -18°C when maintenance mode is inactive. |
| S8 | During maintenance mode, the system shall not permit the chamber temperature to exceed 0°C. |
| S9 | The system shall flag a seed sample for regeneration when its recorded viability is below the configured viability threshold. |
| S10 | The system shall limit each depositor's withdrawals of boxes of a species to 20% of the eligible boxes for that species in each calendar year, using the quota rule defined in the model. |
| S11 | The system shall permit redeposit of a withdrawn box only after a successful re-inspection has been recorded. |
| S12 | The system shall record each operation with event type, box identifier, actor, timestamp, and outcome. |

## Classification

| Requirement | Classification | Quantification / verification |
|---|---|---|
| S1 | Operation precondition | Test deposit using registered and unregistered depositors. |
| S2 | State invariant | Count stored boxes and compare with capacity. |
| S3 | State invariant | Check each specified chamber's numeric capacity. |
| S4 | State invariant and operation authorization | Check unique owner mapping and owner-only ordinary withdrawal. |
| S5 | Operation / exception rule | Test authorized emergency release and non-emergency denial. |
| S6 | Non-functional constraint | Temperature sensor readings must be ≤ -18°C outside maintenance. |
| S7 | State invariant / monitoring operation | Verify alarm or rejection for readings above -18°C outside maintenance. |
| S8 | State invariant | Verify temperature is ≤ 0°C during maintenance. |
| S9 | Non-functional monitoring requirement | Check threshold and flagging deadline once configured; exact values are ASSUMPTION-6. |
| S10 | State invariant / operation constraint | Compare annual withdrawals with quota. |
| S11 | Operation precondition | Reject redeposit without successful inspection. |
| S12 | Non-functional / audit requirement | Verify required audit fields for every operation. |

## Version History

| Version | Description |
|---|---|
| v1.0 | Original informal requirements |
| v2.0 | Atomic, testable reformulation after defect analysis |
