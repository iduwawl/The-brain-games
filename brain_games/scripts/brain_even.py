#!/usr/bin/env python3
from games import even
import engine


def main():
    engine.run_game(even.get_num_and_is_even_answer,
                    even.GAME_RULE)


if __name__ == "__main__":
    main()
