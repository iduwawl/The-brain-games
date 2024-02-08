#!/usr/bin/env python3
from brain_games.games import calc
from brain_games import engine


def main():
    engine.run_game(calc.result_of_expression,
                    calc.expression,
                    calc.GAME_RULE)


if __name__ == "__main__":
    main()
