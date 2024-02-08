#!/usr/bin/env python3
from brain_games.games import progression
from brain_games import engine


def main():
    engine.run_game(progression.str_with_replaced_num,
                    progression.num_from_list,
                    progression.GAME_RULE)


if __name__ == "__main__":
    main()
