# Operations — Northwind Components
*System: MES. Extract 2026-07-02. Fictional firm, synthetic figures.*

## Throughput & delivery
| Metric | June | May | April | Plan |
|---|---|---|---|---|
| Units shipped (000) | 512 | 528 | 519 | 525 |
| Orders shipped | 1,240 | 1,301 | 1,268 | — |
| **On-time delivery %** | **91.2** | **94.0** | 93.6 | 95.0 |
| Late orders | 5 | 2 | 3 | — |
| Avg days late (late orders) | 2.6 | 1.5 | 2.0 | — |

## Late-order detail (June)
| Order | Customer | Days late | Root cause |
|---|---|---|---|
| SO-4471 | Meridian OEM | 4 | supplier X material delay |
| SO-4488 | Halton Aftermarket | 3 | supplier X material delay |
| SO-4502 | Meridian OEM | 2 | supplier X material delay |
| SO-4510 | Delta Contract Mfg | 2 | line B unplanned downtime |
| SO-4525 | Kessler Group | 1 | planning/scheduling error |

*3 of the 5 late orders trace to supplier X.*

## Quality & efficiency
| Metric | June | May | April |
|---|---|---|---|
| First-pass yield % | 96.1 | 97.0 | 96.8 |
| Scrap % | 2.4 | 1.9 | 2.0 |
| OEE % | 78 | 81 | 80 |
| Unplanned downtime (hrs) | 62 | 41 | 47 |

## Utilisation by line
| Line | June util % | May util % | Note |
|---|---|---|---|
| Line A | 82 | 86 | high-margin |
| Line B | 88 | 84 | mid |
| Line C | 94 | 79 | low-margin; run hot to clear backlog |
