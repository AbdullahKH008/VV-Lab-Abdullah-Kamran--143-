# Clarification Questions and Resolved Statements

The following resolutions are proposed interpretations for the formal model. Where the lab wording does not supply an answer, an assumption is explicitly identified.

| Defect ID | Clarification Question | Resolved Statement / Assumption |
|---|---|---|
| D01 | What does “large number” mean? | ASSUMPTION-1: S3 provides the operative chamber capacities; S2 means a chamber supports many boxes within that limit. |
| D02 | Are chambers 1–4 the only chambers? | ASSUMPTION-2: The modeled vault has exactly four chambers. |
| D03 | How is registration checked? | ASSUMPTION-3: A depositor is eligible when its identifier is in the registered-depositor set. |
| D04 | Does ownership change on withdrawal? | Ownership remains with the depositor; withdrawal changes custody/status, not ownership. |
| D05 | Who declares an emergency and who can request release? | ASSUMPTION-4: Only the vault authority declares an emergency; requester eligibility is controlled by the authority. |
| D06 | Does emergency release override normal owner-only withdrawal? | S5 is treated as an explicit exception to S4 when an emergency is declared and authorized. |
| D07 | What is a safe temperature? | S7 provides the normal maximum of -18°C; maintenance exception is handled by S8. |
| D08 | When may temperature exceed -18°C? | Temperature may be at most 0°C during an authorized maintenance mode; otherwise it must be at most -18°C. |
| D09 | How long may maintenance last? | ASSUMPTION-5: The duration is authorized by the vault authority; no maximum duration is specified in the source. |
| D10 | What threshold and delay define low viability and promptly? | ASSUMPTION-6: The threshold and deadline must be configured by the vault authority because the source gives no values. |
| D11 | What does per year mean? | ASSUMPTION-7: The quota is measured per calendar year. |
| D12 | How is 20% rounded? | ASSUMPTION-8: The maximum number is floor(20% of the eligible species-box count at the start of the calendar year). |
| D13 | What counts as successful re-inspection? | ASSUMPTION-9: A box can be redeposited only when an authorized inspection records a pass. |
| D14 | What makes the audit trail good? | ASSUMPTION-10: Every operation records event type, box ID, actor, timestamp, outcome, and emergency reference if applicable. |
| D15 | Which records prove registration and ownership? | Registration set and box-owner mapping are treated as authoritative state components. |
| D16 | When are constraints checked? | Applicable preconditions are checked before any state change. |
| D17 | What must be recorded for emergency release? | Emergency declaration and release are included in the audit record under ASSUMPTION-10. |
