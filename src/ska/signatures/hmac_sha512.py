__title__ = 'ska.signatures.hmac_sha512'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'HMACSHA512Signature',
    )

import hashlib
import hmac

from ska.base import AbstractSignature

class HMACSHA512Signature(AbstractSignature):
    """
    HMAC SHA-512 signature.
    """
    @classmethod
    def make_hash(cls, auth_user, secret_key, valid_until=None, extra={}):
        """
        :param str auth_user:
        :param str secret_key:
        :param float|str valid_until: Unix timestamp, valid until.
        :param dict extra: Additional variables to be added.
        :return str:
        """
        raw_hmac = hmac.new(
            cls.make_secret_key(secret_key),
            cls.get_base(auth_user, valid_until, extra=extra),
            hashlib.sha512
            ).digest()

        return raw_hmac
