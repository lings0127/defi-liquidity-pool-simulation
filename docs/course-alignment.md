# Course alignment and delivery checklist

This personal repository follows the group's DeFi liquidity-pool case and decision questions. The course baseline remains the 7-day, single-pool constant-product model; this document tracks the personal implementation and evidence, not a replacement research scope.

## Shared baseline to confirm with the group

- Initial reserves: 1,000,000 Token A and 2,000,000 Token B; pool spot price: 2 B per A.
- Swap interarrival: exponential with mean 5 minutes; order mix 60%/30%/10%; sizes 100–1,000 / 1,000–10,000 / 10,000–50,000 A; slippage tolerances 1%/3%/5%.
- Base fee 0.3%; LP add interval EXPO(2 h), removal interval EXPO(3 h); external-price hourly change N(0%, 2%); duration 168 h; 10 replications suggested.
- Planned comparisons in the group README: fee 0.3% vs 0.5%, volatility sigma 2% vs 5%, large-order share 10% vs 20%, and liquidity changes/withdrawal shock.

These are course scenario assumptions, not measured on-chain data. Before comparing results, agree with the group on event tie-breaking, whether failed swaps affect volume, fee denomination/conversion, LP share accounting, price process, and the impermanent-loss benchmark.

## Full course workflow

1. System analysis and problem definition: identify pool, actors, events, boundaries, decision variables, and performance measures.
2. Conceptual model: document event flow, state variables, assumptions, and same-time event priority; map each item to Arena and Python components.
3. Data and parameters: label each value as course-given, assumed, or observed; record units, distribution, source, and rationale.
4. Software model: deliver the Arena model required by the course. Python is a separately implemented formula-checking, batch-run, and analysis companion unless the instructor explicitly accepts it as a substitute.
5. Verification and validation: formula unit tests, deterministic hand-calculation cases, extreme-condition checks, parameter checks, trace checks, and Arena/Python benchmark comparison.
6. Multi-scenario experiments: use the shared factors above, hold other factors fixed for one-factor comparisons, then assess selected interactions if time permits.
7. Results analysis: report replication count, seed policy, means, dispersion/confidence intervals, plots, and trade-offs.
8. Optimization: compare a small, explicitly defined set of course-relevant alternatives; disclose the objective and constraints.
9. Management recommendations: make recommendations only when supported by model results and state assumptions and risks.
10. Final presentation: provide the report, Arena model/screenshots, source, parameter table, output files, validation evidence, and reproducible run instructions.

## Personal contribution and status

- The public personal repository initially contained planning documentation and empty Arena/Python/data/results directory notes, not an executable model.
- This branch adds a minimal Python package and an independently written, pure v2 swap-quote function with tests. It does not yet implement the event simulation, LP accounting, external price process, Arena model, experiments, charts, or course report.
- Group-level case framing and parameters are attributed to the group's repository. Record future implementation, tests, analysis, and writing as personal contributions; preserve upstream MIT notices for any code actually reused.

## Status

| Course deliverable | Status in this branch |
| --- | --- |
| System analysis/problem definition | Group case documented; personal analysis pending |
| Conceptual model and Arena mapping | Group baseline available; personal mapping/artifact pending |
| Data and parameter table | Shared baseline listed above; reconciliation and full provenance pending |
| Python baseline calculation | Initial constant-product quote function added; execution not yet verified |
| Arena software model | Not present |
| Verification/validation | Tests authored; not run in this environment |
| Multi-scenario experiments/results | Not implemented |
| Optimization/recommendations | Not implemented |
| Final report/presentation package | Not present |
