#!/usr/bin/env python3
import games.prime
import engine


def main():
    engine.run_game(games.prime.get_num_and_is_prime_answer,
                    games.prime.GAME_RULE)


if __name__ == "__main__":
    main()
