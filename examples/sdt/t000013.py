# -*- coding: utf-8 -*-
def t000013_1():
    """State 0,1"""
    t000013_x0()

def t000013_x0():
    """State 0"""
    while True:
        """State 2"""
        assert not CheckSelfDeath()
        """State 1"""
        def WhilePaused():
            c1_116()
        assert CheckSelfDeath() == 1

