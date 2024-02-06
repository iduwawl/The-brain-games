#!/usr/bin/env python3
from games import progression
import engine


def main():
    engine.run_game(progression.get_list_with_replaced_num_and_num,
                    progression.GAME_RULE)


if __name__ == "__main__":
    main()
