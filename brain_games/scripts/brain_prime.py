#!/usr/bin/env python3
from games import prime
import engine


def main():
    engine.run_game(prime.get_num_and_is_prime_answer,
                    prime.GAME_RULE)


if __name__ == "__main__":
    main()
