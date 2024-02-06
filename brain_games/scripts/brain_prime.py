#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.engine import run_game


def main():
    run_game(prime.get_num_and_is_prime_answer,
             prime.GAME_RULE)


if __name__ == "__main__":
    main()
