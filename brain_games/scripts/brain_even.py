#!/usr/bin/env python3
import games.even
import engine


def main():
    engine.run_game(games.even.get_num_and_is_even_answer,
                    games.even.GAME_RULE)


if __name__ == "__main__":
    main()
