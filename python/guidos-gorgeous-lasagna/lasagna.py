# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME: int = 40


# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME: int = 2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(time_in_oven: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time_in_oven

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here

def preparation_time_in_minutes(n_layers: int) -> int:
    """Calculate the preparation time based on number of layers in the lasagne

    :param n_layers: int number of layers that will be prepared.
    :return: int time needed to prepare all layers.
    """
    return n_layers*PREPARATION_TIME

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """ Sum of preparation time and time the lasagna is already in the oven.

    :param number_of_layers: int number of layers that were prepared
    :param elapsed_bake_time: int time in minutes that the lasagna is already in the oven.
    :return: int Total elapsed time, calculated as sum of preparation time and time the lasagna is already in the oven.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
