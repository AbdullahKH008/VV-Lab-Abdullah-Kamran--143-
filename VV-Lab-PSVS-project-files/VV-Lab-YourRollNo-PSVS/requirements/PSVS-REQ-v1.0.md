# PSVS Requirements — Version 1.0

## Scenario

A polar vault stores sealed boxes of crop seeds deposited by registered institutions (gene banks, universities, governments). Each box holds seed samples of one species. The vault has several freezer chambers, and staff handle deposits, withdrawals, and monitoring. Depositors keep ownership of their boxes. The vault is a custodian, not an owner.

## Informal Requirements

- **S1:** The system shall accept seed boxes only from registered depositors.
- **S2:** Each chamber can hold a large number of boxes.
- **S3:** Chambers 1–3 hold at most 50,000 boxes each; Chamber 4 holds at most 20,000.
- **S4:** A box belongs to exactly one depositor, and only that depositor may withdraw it.
- **S5:** In an emergency, the vault authority may release any box to any requesting party.
- **S6:** Boxes shall be stored at a safe temperature.
- **S7:** Chamber temperature shall never rise above -18°C.
- **S8:** During maintenance, a chamber may be warmed to 0°C.
- **S9:** Seed samples with low viability shall be flagged promptly for regeneration.
- **S10:** A depositor may withdraw at most 20% of its boxes of a species per year.
- **S11:** A withdrawn box may be redeposited only after re-inspection.
- **S12:** The system shall keep a good audit trail of all actions.

## Version History

| Version | Description |
|---|---|
| v1.0 | Initial baseline requirements transcribed from the lab assignment |
