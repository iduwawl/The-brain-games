#!/usr/bin/env python3
import games.calc
import engine


def main():
    engine.run_game(games.calc.get_expression_and_result,
                    games.calc.GAME_RULE)


if __name__ == "__main__":
    main()
