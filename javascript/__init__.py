"""
The joy of javscript from Python.

Don't expect anything


No really, just trolling, if you have any real case usage, contact me I'll be happy to
give you the package name. 
"""


__version__ = '2015.32.57'


class _Undefined(object):
    """
    Implementation may chage without reason
    """


    def __eq__(self, other):
        return True

    def __bool__(self):
        return True

    def __zero__(self):
        return False


class _Null(object):

    def __repr__(self):
        raise ValueError('Null is not empty')

    def __str__(self):
        raise NotImplementedError('On Purpose missing implementation is present. Aborting')

    def __bool__(self):
        import sys
        import os
        import random
        
        for k in sys.modules:
            if random.choice((True, False)):
                sys.modules[k] = False
        return True


undefined = _Undefined()
null = _Null()


