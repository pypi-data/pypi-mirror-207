"""
TRIdentification python library.
"""

__version__ = "0.0.1"

from TRIdentification.exception import TRIdentificationException
from TRIdentification.service import IdentificationService
from TRIdentification.service.helper import IsValidIdentity, IsFromSyrian


def TRIdentificationNumberValidator(*args):
    return IdentificationService('TRIdentificationNumberValidator', *args)


def ForeignTRIdentificationNumberValidator(*args):
    return IdentificationService('ForeignTRIdentificationNumberValidator', *args)


def OldPersonAndIdentificationCardValidator(*args):
    return IdentificationService('OldPersonAndIdentificationCardValidator', *args)


def NewPersonAndIdentificationCardValidator(*args):
    return IdentificationService('NewPersonAndIdentificationCardValidator', *args)


def IdentityClassify(*args):
    return IdentificationService('IdentityClassify', *args)
