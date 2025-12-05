from __future__ import annotations

from typing import Dict, List


class StatsFetcher:
    """Return lightweight team statistics."""

    def fetch_team_stats(self, team: str) -> Dict[str, float]:
        baseline = {
            "pace": 100.0,
            "offensive_rating": 112.0,
            "defensive_rating": 111.0,
        }
        adjustments = {
            "Golden State Warriors": {"pace": 101.5, "offensive_rating": 114.0},
            "Memphis Grizzlies": {"pace": 99.5, "defensive_rating": 110.0},
        }
        return {**baseline, **adjustments.get(team, {})}


__all__: List[str] = ["StatsFetcher"]
