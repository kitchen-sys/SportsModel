from __future__ import annotations

import argparse
from dataclasses import asdict
import json

from data.odds_scraper import OddsScraper
from data.team_registry import teams_for_sport
from sports.nba import NBAAnalyzer


def run_demo(sport: str, max_games: int | None = None) -> None:
    analyzer = NBAAnalyzer()
    scraper = OddsScraper()
    odds = scraper.fetch_odds_api(sport=sport, max_games=max_games or 1)

    if sport != "basketball_nba":
        print(f"Scanner data available for {sport}, but demo analysis is NBA-only.")
        print(f"Generated {len(odds)} sample games covering {len(teams_for_sport(sport))} teams.")
        return

    for game in odds:
        edge = analyzer.analyze_game(**game, injuries=[])
        if edge:
            print("⚡ EDGE DETECTED")
            print(json.dumps(asdict(edge), indent=2))
        else:
            print("No edge for game", game["game_id"])


def scan_sports(sport: str | None = None) -> None:
    scraper = OddsScraper()
    sports = [sport] if sport else scraper.list_supported_sports()
    for code in sports:
        teams = teams_for_sport(code)
        games = scraper.fetch_odds_api(sport=code)
        print(f"{code}: {len(teams)} teams -> {len(games)} matchups generated")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="OT betting demo agent")
    parser.add_argument("command", choices=["demo", "scan"], help="Which command to run")
    parser.add_argument("--sport", default="basketball_nba", help="Sport code to scan/demo")
    parser.add_argument("--max-games", dest="max_games", type=int, default=None, help="Limit demo games")
    args = parser.parse_args(argv)

    if args.command == "demo":
        run_demo(sport=args.sport, max_games=args.max_games)
    elif args.command == "scan":
        scan_sports(None if args.sport == "all" else args.sport)


if __name__ == "__main__":
    main()
