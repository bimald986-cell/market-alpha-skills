# Market Alpha Skills

A curated set of AI agent skills for evidence-based market research, stock screening, and risk-aware investment analysis.

**Market focus:** Bybit-listed U.S. stock instruments and xStocks, when current availability can be verified.

## What this repository covers

- Market regime and breadth analysis
- Quality screening using documented frameworks such as CAN SLIM and VCP
- Single-stock research covering fundamentals, technicals, catalysts, valuation, and risks
- Structured conviction scoring with explicit uncertainty
- Clear buy, hold, watchlist, or avoid assessments supported by dated evidence

## How to use

1. Install or load the skill files in your supported agent environment.
2. Ask for a market regime review or a deep dive on a specific ticker.
3. Require current sources and an explicit as-of timestamp for any claim about today's market.
4. Review the assumptions, risks, and evidence before making an investment decision.

## Skill files currently included

- `SKILL.md` — End-to-end orchestrator covering market regime, screening, deep dives, conviction scoring, and output format.
- `skills/market-regime/SKILL.md` — Market health, breadth, trend, volatility, and sector leadership.
- `skills/stock-deep-dive/SKILL.md` — Single-stock fundamentals, technical setup, catalysts, valuation, risks, and conviction score.

**Inventory note:** `stock-screener` and `conviction-score` are workflow sections in the top-level `SKILL.md`; they are not separate standalone skill files yet. Do not treat them as separately installable skills until those files exist.

## Evidence and risk standards

- Date and identify sources for current prices, market conditions, catalysts, and instrument availability.
- Separate observed facts from interpretation. If current data cannot be verified, say so instead of guessing.
- Treat conviction scores as structured judgement, not a probability of profit or a promise of returns.
- Do not assume a Bybit instrument is an ordinary share. Verify whether it is a share, tokenized product, or another instrument, and identify material differences when evidence is available.
- Do not imply that analysis executes a trade. Never request or store exchange passwords, API keys, or signing credentials in this repository.

The skills support research and decision preparation. They do not guarantee results or replace an individual's risk assessment.
