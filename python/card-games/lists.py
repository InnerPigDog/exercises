"""Card Games Exercise (https://exercism.org/tracks/python/exercises/card-games) from https://exercism.org/
"""

import statistics


def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    return list(range(number, number+3))


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """
    first_last_avg = (hand[0]+hand[-1])/2
    median = statistics.median(hand)
    return card_average(hand) == first_last_avg or card_average(hand) == median


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_nums = []
    odd_nums = []
    for card in hand:
        if card % 2 == 0:
            even_nums.append(card)
        else:
            odd_nums.append(card)
    return sum(even_nums)/len(even_nums) == sum(odd_nums)/len(odd_nums)


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
