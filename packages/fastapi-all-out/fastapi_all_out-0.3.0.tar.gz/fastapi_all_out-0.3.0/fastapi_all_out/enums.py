from enum import Enum


class TempCodeTriggers(Enum):
    EmailActivation = 'EA'
    EmailChange = 'EC'
    PasswordReset = 'PR'


class JWTTokenTypes(Enum):
    access = 'access'
    refresh = 'refresh'
