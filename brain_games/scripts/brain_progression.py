#!/usr/bin/env python3
from brain_games.games import progression
from brain_games.engine import run_game


def main():
    run_game(progression.get_joined_list_with_replaced_num_and_num,
             progression.GAME_RULE)


if __name__ == "__main__":
    main()
