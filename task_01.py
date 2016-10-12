#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 Synthesizing task 1"""


def get_matches(players):
    '''This new function has been created to take list of players and
    produce unique matchups.
    Args:
        players(list): Includes list of players
    Returns:
        result:(list): Includes list of tuples for matchups
    Examples:
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    '''
    result = []

    for exp1, num1 in enumerate(players):
        for exp2, num2 in enumerate(players):
            if num1 is not num2 and exp1 < exp2:
                result.append((num1, num2))
            else:
                continue
    return result
