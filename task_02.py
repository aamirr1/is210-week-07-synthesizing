#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Week 7 Synthesizing Task 2"""

import getpass
import authentication


def login(username, maxattempts=3):
    ''' This function takes only 2 functions. Login and password
    Args:
        username(string): This will be a username for login
        maxattempts(optional int): This will include number of login attempts
        till user gets locked
    Returns:
        positive(boolean)
        True or  false value if password matches or not.
    Examples:
        >>> import task_02
        >>> task_02.login('veruca', 2)
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        True
    '''
    positive = False
    attempt = 1

    login_message = 'Please enter your password: '
    error_message = 'Incorrect username or password. You have {0} attempts left'

    while attempt <= maxattempts:
        passauthen = getpass.getpass(login_message)
        promptoutupt = authentication.authenticate(username, passauthen)
        if promptoutupt:
            positive = True
            break
        else:
            print error_message.format(maxattempts - attempt)
            attempt += 1
    return positive
