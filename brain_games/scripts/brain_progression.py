#!/usr/bin/env python3
from brain_games.games import progression
from brain_games import engine


def main():
    engine.run_game(progression.get_joined_list_with_replaced_num_and_num,
                    progression.GAME_RULE)


if __name__ == "__main__":
    main()
