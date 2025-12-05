# OT Sports Betting System

**Optimal Transport AI for Sports Gambling Edge Detection**

A production-grade system that uses Optimal Transport theory to detect arbitrage opportunities in sports betting markets by measuring the geometric distance between true probability distributions and market-implied distributions.

## 🧠 Theory: Why OT Beats the Market
### The Core Insight
Sportsbooks price expected values accurately, but they do **not** price distribution geometry accurately.

Optimal Transport measures the "cost" to morph one probability distribution into another using the Wasserstein distance:

$$W(P_{true}, P_{market}) = \min_\pi \int\int \|x - y\|^2 \, d\pi(x, y)$$

If \(W > \text{threshold}\) → Edge exists → Bet.

This is the same framework used in:

- Quant finance (volatility arbitrage)
- Machine learning (domain adaptation)
- Economics (income inequality measurement)

### Why Books Don't Use This
- Computational cost: OT is expensive
- Data requirements: Need causal models + simulations
- Liquidity constraints: Books balance action, not optimize distributions
- Public betting bias: Books shade lines toward public sentiment

You have a structural edge.

## 📐 Mathematical Framework
### 1. Wasserstein Distance (W₂)
$$W_2(\mu, \nu) = \inf \left\{ \int\int \|x - y\|^2 \, d\pi(x,y) : \pi \in \Pi(\mu, \nu) \right\}$$

Where:

- \(\mu\) = true distribution (from Monte Carlo + causal model)
- \(\nu\) = market distribution (from odds)
- \(\pi\) = transport plan (how to move probability mass)

Interpretation: If \(W_2\) is large, the market is geometrically far from truth.

### 2. Causal DAG
Model causal relationships:

- Injuries → Team Strength → Scoring
- Weather → Passing → Total Points
- Matchup → Pace → Distribution Variance

Books model correlations. You model causation.

### 3. Expected Value with OT Correction
\(\text{EV} = P(\text{true}) \times \text{Payout} - P(\text{market}) \times \text{Stake}\)

If \(W_2(P_{true}, P_{market}) > \delta:\)

\[\text{EV}_{adjusted} = \text{EV} \times (1 + \alpha \times W_2)\]

The OT distance amplifies confidence in EV calculation.

### 4. Kelly Criterion Bet Sizing
\[f^* = \frac{p \times b - q}{b}\]

Where:

- \(p\) = true win probability
- \(b\) = net odds (decimal - 1)
- \(q\) = 1 - p

Use fractional Kelly (0.5×) for risk control.

## 🏗️ System Architecture
```
ot_sports_betting/
│
├── src/
│   ├── models/
│   │   ├── ot_engine.py         # Wasserstein distance computation
│   │   ├── causal_graph.py      # DAG for causal inference
│   │   ├── monte_carlo.py       # MC simulation
│   │   └── distribution.py      # Distribution modeling
│   │
│   ├── data/
│   │   ├── odds_scraper.py      # Fetch odds (The Odds API)
│   │   └── stats_fetcher.py     # Team stats (NBA API, etc.)
│   │
│   ├── edge/
│   │   ├── detector.py          # Edge detection logic
│   │   ├── ev_calculator.py     # EV computation
│   │   └── kelly.py             # Kelly criterion
│   │
│   ├── sports/
│   │   ├── nba.py               # NBA-specific analysis
│   │   ├── nfl.py               # NFL analysis
│   │   ├── nhl.py               # NHL analysis
│   │   ├── ncaaf.py             # College Football analysis
│   │   ├── soccer.py            # Soccer analysis
│   │   └── ufc.py               # UFC analysis (in development)
│   │
│   ├── backtest/
│   │   ├── engine.py            # Backtesting framework
│   │   └── metrics.py           # Performance analytics
│   │
│   └── agent.py                 # Main CLI interface
│
├── config.yaml                  # Configuration
├── requirements.txt
└── README.md
```

## 🚀 Quick Start
1. **Installation**
   ```bash
   cd ot_sports_betting
   ./start.sh
   ```
   This will:
   - Create virtual environment
   - Install dependencies
   - Set up logging

2. **Run Demo**
   ```bash
   python src/agent.py demo
   ```
   Output:
   ```
   ⚡ EDGE DETECTED: OVER 215.5
      EV: 5.2%
      Kelly Bet: 2.1% of bankroll
      Confidence: 73%
   ```

3. **Scan Live Games**
   ```bash
   # Scan all sports
   python live_scanner.py --sport all

   # Scan specific sport
   python live_scanner.py --sport nba
   python live_scanner.py --sport nfl
   python live_scanner.py --sport nhl
   python live_scanner.py --sport ncaaf
   python live_scanner.py --sport soccer
   ```
   Finds edges across all live games with real-time odds.

4. **Analyze Specific Game**
   ```python
   from src.sports.nba import NBAAnalyzer

   analyzer = NBAAnalyzer()
   edge = analyzer.analyze_game(
       game_id="nba_001",
       home_team="Golden State Warriors",
       away_team="Memphis Grizzlies",
       total_line=215.5,
       over_odds=-110,
       under_odds=-110,
       injuries=[]
   )

   if edge:
       print(f"Bet {edge.recommendation} {edge.line}")
       print(f"EV: {edge.expected_value:.2%}")
       print(f"Kelly: {edge.kelly_fraction:.2%}")
   ```

## 📊 Usage Examples
### Example 1: NBA Game with Injury
```python
from src.sports.nba import NBAAnalyzer

analyzer = NBAAnalyzer()

edge = analyzer.analyze_game(
    game_id="nba_001",
    home_team="Golden State Warriors",
    away_team="Memphis Grizzlies",
    total_line=215.5,
    over_odds=-110,
    under_odds=-110,
    injuries=[
        {'player': 'Steph Curry', 'status': 'out', 'impact': -5.8}
    ]
)

if edge:
    print(f"Bet {edge.recommendation} {edge.line}")
    print(f"EV: {edge.expected_value:.2%}")
    print(f"Kelly: {edge.kelly_fraction:.2%}")
```

### Example 2: Batch Analysis
```python
from src.data.odds_scraper import OddsScraper

scraper = OddsScraper()
odds = scraper.fetch_odds_api(sport="basketball_nba")

edges = []
for game in odds:
    edge = analyzer.analyze_game(...)
    if edge:
        edges.append(edge)

print(f"Found {len(edges)} edges")
```

### Example 3: Backtesting
```python
from src.backtest.engine import BacktestEngine

engine = BacktestEngine(initial_bankroll=10000)
result = engine.run_backtest(edges, outcomes)

print(f"ROI: {result.roi:.1%}")
print(f"Sharpe: {result.sharpe_ratio:.2f}")
```

## 🎲 Sports Supported
| Sport | Teams | Status | Key Features |
| --- | --- | --- | --- |
| NBA | 30 | ✅ | Pace, injuries, RAPTOR, home court, totals + spreads |
| NFL | 32 | ✅ | EPA, weather, key numbers, totals + spreads |
| NHL | 32 | ✅ | Poisson goals, save%, corsi, totals + puck lines |
| NCAAF | 17 | ✅ | EPA, higher variance, home advantage, totals + spreads |
| Soccer | 40 | ✅ | EPL + La Liga, Poisson goals, xG, totals + handicaps |
| UFC | - | 🚧 | In development (style matchups, bimodal outcomes) |

## ⚙️ Configuration
Edit `config.yaml`:

```yaml
# Optimal Transport
ot:
  threshold: 0.15        # Minimum W distance for edge
  p_norm: 2              # Wasserstein-2
  reg: 0.01              # Sinkhorn regularization

# Edge Detection
edge:
  min_ev: 0.03           # 3% minimum EV
  min_kelly: 0.01
  max_kelly: 0.05        # Max 5% of bankroll

# Monte Carlo
simulation:
  num_paths: 10000
  confidence_interval: 0.95

# Risk Management
risk:
  max_exposure_per_game: 0.02   # 2% per game
  max_daily_exposure: 0.10      # 10% per day
  stop_loss_daily: -0.05        # Stop at 5% daily loss
```

## 📈 Performance Metrics
The system tracks:

- Expected Value (EV): Percentage edge per bet
- Wasserstein Distance (W): OT distance measure
- Kelly Fraction: Optimal bet size
- Confidence Score: Reliability (0-1)
- Closing Line Value (CLV): Beat the closing line?
- Sharpe Ratio: Risk-adjusted returns
- Max Drawdown: Worst loss streak

### Example Output
```
⚡ EDGE DETECTED
  Game: Memphis @ Golden State
  Bet: UNDER 215.5
  Odds: -110
  Expected Value: 4.8%
  Kelly Bet Size: 1.9% of bankroll
  Confidence: 81%
  True P(Under): 54.2%
  Market P: 50.0%
  Wasserstein Distance: 0.187
```

## 🔬 How It Works (Technical)
### Pipeline
1. **Fetch Data**
   - Odds from The Odds API
   - Stats from NBA API / ESPN
   - Injury reports from RotoWire

2. **Build Causal Model**
   - Create DAG of causal relationships
   - Add injury nodes
   - Model matchup interactions

3. **Monte Carlo Simulation**
   - Simulate 10,000 game outcomes
   - Apply causal effects
   - Generate true distribution

4. **OT Distance**
   - Convert market odds to distribution
   - Compute Wasserstein distance
   - Detect geometric edge

5. **Edge Detection**
   - Calculate EV
   - Apply Kelly sizing
   - Check risk constraints
   - Output recommendation

### Example: NBA Totals
```python
# True distribution (MC simulation)
true_samples = simulate_nba_game(warriors, grizzlies, injuries)
# → μ = 212.3, σ = 10.8

# Market distribution (from odds)
market_dist = totals_to_distribution(line=215.5, odds=-110)
# → μ = 215.5, σ = 12.0

# OT distance
W = wasserstein_distance(true_dist, market_dist)
# → W = 0.193

# Edge detected! (W > 0.15)
# Market is overpricing total → Bet UNDER
```

## 🎯 Best Practices
1. Start Small
   - Test with paper trading first
   - Use fractional Kelly (0.5×)
   - Max 2% per game
2. Track CLV
   - Closing Line Value is the #1 indicator
   - If you consistently beat closing lines, you're winning long-term
3. Diversify
   - Don't bet one sport only
   - Spread across uncorrelated games
   - Use portfolio Kelly for multiple bets
4. Risk Management
   ```python
   # Daily limits
   max_exposure = bankroll * 0.10  # 10% max daily
   stop_loss = bankroll * 0.05     # Stop at 5% down

   # Per-game limits
   max_bet = bankroll * 0.02       # 2% per game
   ```
5. Monitor Performance
   ```python
   # Key metrics
   if avg_clv > 0:
       print("✅ Beating closing lines")

   if sharpe > 1.5:
       print("✅ Excellent risk-adjusted returns")

   if max_drawdown < 0.20:
       print("✅ Good risk control")
   ```

## 📊 Data Sources
### Live Odds
The Odds API: https://the-odds-api.com/ (500 free requests/month)

Get API key and set: `export ODDS_API_KEY=your_key`

### Stats APIs
- NBA: nba_api (free) - 30 teams
- NFL: Pro Football Reference / ESPN - 32 teams
- NHL: NHL API / Hockey Reference - 32 teams
- NCAAF: ESPN / College Football Data - 17 major FBS teams
- Soccer: Football-Data.org / StatsBomb - 40 teams (EPL + La Liga)
- UFC: UFCStats.com (in development)

## 🧪 Testing Individual Components
- Test OT Engine: `python src/models/ot_engine.py`
- Test Causal Graph: `python src/models/causal_graph.py`
- Test Monte Carlo: `python src/models/monte_carlo.py`
- Test Edge Detection: `python src/edge/detector.py`

Each module has standalone examples.

## 🚨 Disclaimer
This is for educational and research purposes.

Sports betting involves risk
Past performance ≠ future results
Only bet what you can afford to lose
Check local laws and regulations
Use responsible bankroll management
The authors assume no liability for losses.

## 📚 Mathematical References
- Optimal Transport: Villani, "Optimal Transport: Old and New"
- Wasserstein Distance: Cuturi, "Sinkhorn Distances" (NIPS 2013)
- Kelly Criterion: Kelly, "A New Interpretation of Information Rate" (1956)
- Causal Inference: Pearl, "Causality" (2000)
- Sports Analytics: Macdonald, "Adjusted Plus-Minus Models" (2011)

## 🤝 Contributing
Contributions welcome!

Areas for improvement:
- Real-time odds streaming
- Player prop betting
- Live in-game betting
- Machine learning priors
- Multi-book arbitrage
- Automated execution

## 📧 Support
For questions or issues:
- Check documentation
- Review examples
- Open GitHub issue

## ⭐ Key Features
- ✅ Optimal Transport for edge detection
- ✅ Causal DAG modeling
- ✅ Monte Carlo simulation
- ✅ Kelly Criterion bet sizing
- ✅ Multi-sport support
- ✅ Backtesting framework
- ✅ Risk management built-in
- ✅ Production-ready code

## 🎓 Learn More
### Tutorials
- `notebooks/01_ot_basics.ipynb` - OT fundamentals
- `notebooks/02_nba_example.ipynb` - Full NBA analysis
- `notebooks/03_backtesting.ipynb` - Strategy testing

### Theory Deep Dives
- `docs/optimal_transport.md` - OT mathematics
- `docs/causal_inference.md` - DAG construction
- `docs/kelly_criterion.md` - Bet sizing theory

## 🏆 Why This Works
Sports betting markets are efficient at pricing means, but inefficient at pricing distributions.

By using Optimal Transport to measure distribution geometry, you gain an edge that traditional betting models miss.

Combined with causal modeling and rigorous risk management, this system provides a systematic, quantitative approach to sports betting.

Good luck, and bet responsibly! 🎯
