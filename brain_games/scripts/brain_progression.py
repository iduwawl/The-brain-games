#!/usr/bin/env python3
import games.progression
import engine


def main():
    engine.run_game(games.progression.get_str_with_miss_num_and_num,
                    games.progression.GAME_RULE)


if __name__ == "__main__":
    main()
