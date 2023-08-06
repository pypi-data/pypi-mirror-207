"""
TRIdentification python library.
"""

__version__ = "0.0.3"

from TRIdentification.exception import TRIdentificationException
from TRIdentification.service import IdentificationService
from TRIdentification.service.helper import IsValidIdentity, IsFromSyrian

service = IdentificationService()


def TRIdentificationNumberValidator(*args):
    return service('TRIdentificationNumberValidator', *args)


def ForeignTRIdentificationNumberValidator(*args):
    return service('ForeignTRIdentificationNumberValidator', *args)


def OldPersonAndIdentificationCardValidator(*args):
    return service('OldPersonAndIdentificationCardValidator', *args)


def NewPersonAndIdentificationCardValidator(*args):
    return service('NewPersonAndIdentificationCardValidator', *args)


def IdentityClassify(*args):
    return service('IdentityClassify', *args)
