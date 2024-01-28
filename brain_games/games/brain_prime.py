from random import randint
from brain_games.engine import is_primne

number = randint(90, 92)

prime_n = ""
dia = number // 2

ads = is_primne(n=number)


print(ads)
