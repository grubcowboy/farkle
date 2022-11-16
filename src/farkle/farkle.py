# FARKLE GAME!
import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"{self.name}: \n  score: {self.score}\n"

# class Die(enum):
#     REMOVED = -1
#     UNROLLED = 0
#     ONE = 1
#     TWO = 2
#     ..


def game_over(players):
    for player in players:
        if player.score == 10000:
            return True

    return False


def turn(player):
    print(f"{player.name}, it's your turn")

    dice = [0, 0, 0, 0, 0, 0]
    scored_dice = []

    while True:
        # TODO: if `rolls` is empty repopulate with 6 die

        rolls = roll(dice)

        if is_farkle(rolls):
            print("You farkled")
            break

        # TODO: score function
        # * have user enter in numbers (NOT index) they want to keep from `rolls` OR let them type in `STOP`
        # * validate numbers are in `rolls` and are scoring
        # * remove those dice from `rolls` and increment running total


def roll(dice):
    rolls = []

    for die in dice:
        rolls.append(random.randint(1, 6))

    print(rolls)
    return rolls


def is_farkle(rolls):
    print(rolls)
    die_count = {}

    for die in rolls:
        die_count[die] = die_count[die] + 1 if die in die_count else 1

    print(die_count)

    if 1 in die_count or 5 in die_count:
        return False

    # Looking for 3 pairs in rolls
    pair_count = 0

    for count in die_count.values():
        if count >= 3:
            return False
        if count == 2:
            pair_count += 1

    if pair_count == 3:
        return False

    return True


def main():
    players = [Player("cherry"), Player("grubbie"), Player("coocoo")]

    for player in players:
        print(player)

    turn_count = 0

    while not game_over(players):
        turn(players[turn_count % len(players)])
        turn_count += 1

    print(
        f"{players[(turn_count - 1) % len(players)].name} won! they won in {turn_count}")

    for player in players:
        print(player)


if __name__ == '__main__':
    main()
