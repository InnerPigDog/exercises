def eat_ghost(power_pellet_active, touching_ghost):
    """ Indicates if Pac-Man eats a ghost.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool - Pac-Man eats a ghost if a power pellect is active and he touching a ghost.
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """ Indicates if Pac-Man scores points.

    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool - Pac-Man scores points if he touches a power pellet or a dot.
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """ Indicates if Pac-Man loses the game.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - Pac-Man loses if he has no active power pellet and touches a ghost.
    """
    return (not power_pellet_active) and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """ Indicitates if Pac-Man wins the game.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool - Pac-Man wins if he has eaten all dots and did not lose so far.
    """
    return has_eaten_all_dots and (not lose(power_pellet_active, touching_ghost))
