# EAEA: Evidence-Aware Energy Attribution

Reference implementation and data for the preprint **"Who Pays for the Bit? Evidence-Aware Energy Attribution Across Shared 5G and 6G Network Infrastructure"** by Ghufran Shakeel.

Paper: `paper/Shakeel_Who_Pays_for_the_Bit_preprint.pdf` | Preprint DOI: *(add after publishing on Zenodo)*

## The question

One meter, many services. An operator can measure a machine's energy, but how much belongs to each service? Most equipment draws a large share of power even when idle, so any split is partly a modelling choice. EAEA is an accounting method that checks measurement boundaries, keeps unassigned energy visible, states its allocation rule, and reports "insufficient evidence" when the data cannot support a number.

## What is here

| Path | Content |
|---|---|
| `code/eaea_experiment.py` | EAEA and two baselines (traffic-proportional, resource-weighted); 72,000-trial and 24,000-trial studies; numpy only, seed 20260101 |
| `code/case_study.py` | Deterministic case study on a published macro base-station model, plus an identifiability check |
| `data/` | `results.json`, `scenario_grid.csv`, printed outputs |
| `paper/` | The preprint (PDF, Word) and supplementary material (PDF, Word) |

## Run

```
pip install numpy
cd data
python ../code/eaea_experiment.py
python ../code/case_study.py
```

## Key results (synthetic)

- In the 72,000-trial computational study, EAEA reported a mean allocation error of 0.046 over 59,891 eligible trials. Traffic-proportional and resource-weighted allocation produced mean errors of 0.271 and 0.200, respectively, across all 72,000 trials. These figures use different evaluation populations and should not be interpreted as a matched-sample comparison.
- With published idle-power shares, 0.049 against 0.315 and 0.268.
- Same meter reading, three defensible baseline rules: a low-traffic service's energy differs by 2.5x (92.5 W to 233.7 W).

## Limits (read before citing)

All service-level results are simulated. The simulated reference shares EAEA's cost structure, so its advantage is partly built in. The A to D report categories describe evidence completeness, not error size. See Section 8 of the paper. No measured per-service energy is included.

## Licence

Code: MIT. Paper: CC BY 4.0 (when posted on Zenodo).
