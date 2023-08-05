#  Pyrosex - Telegram MTProto API Client Library for Python
#  Copyright (C) 2023-present OTH <https://github.com/OTHFamily>
#
#  This file is part of Pyrosex.
#
#  Pyrosex is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrosex is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrosex.  If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrosex import raw
from pyrosex.raw.core import TLObject

SecureValueType = Union[raw.types.SecureValueTypeAddress, raw.types.SecureValueTypeBankStatement, raw.types.SecureValueTypeDriverLicense, raw.types.SecureValueTypeEmail, raw.types.SecureValueTypeIdentityCard, raw.types.SecureValueTypeInternalPassport, raw.types.SecureValueTypePassport, raw.types.SecureValueTypePassportRegistration, raw.types.SecureValueTypePersonalDetails, raw.types.SecureValueTypePhone, raw.types.SecureValueTypeRentalAgreement, raw.types.SecureValueTypeTemporaryRegistration, raw.types.SecureValueTypeUtilityBill]


# noinspection PyRedeclaration
class SecureValueType:  # type: ignore
    """This base type has 13 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`SecureValueTypeAddress <pyrosex.raw.types.SecureValueTypeAddress>`
            - :obj:`SecureValueTypeBankStatement <pyrosex.raw.types.SecureValueTypeBankStatement>`
            - :obj:`SecureValueTypeDriverLicense <pyrosex.raw.types.SecureValueTypeDriverLicense>`
            - :obj:`SecureValueTypeEmail <pyrosex.raw.types.SecureValueTypeEmail>`
            - :obj:`SecureValueTypeIdentityCard <pyrosex.raw.types.SecureValueTypeIdentityCard>`
            - :obj:`SecureValueTypeInternalPassport <pyrosex.raw.types.SecureValueTypeInternalPassport>`
            - :obj:`SecureValueTypePassport <pyrosex.raw.types.SecureValueTypePassport>`
            - :obj:`SecureValueTypePassportRegistration <pyrosex.raw.types.SecureValueTypePassportRegistration>`
            - :obj:`SecureValueTypePersonalDetails <pyrosex.raw.types.SecureValueTypePersonalDetails>`
            - :obj:`SecureValueTypePhone <pyrosex.raw.types.SecureValueTypePhone>`
            - :obj:`SecureValueTypeRentalAgreement <pyrosex.raw.types.SecureValueTypeRentalAgreement>`
            - :obj:`SecureValueTypeTemporaryRegistration <pyrosex.raw.types.SecureValueTypeTemporaryRegistration>`
            - :obj:`SecureValueTypeUtilityBill <pyrosex.raw.types.SecureValueTypeUtilityBill>`
    """

    QUALNAME = "pyrosex.raw.base.SecureValueType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/secure-value-type")
