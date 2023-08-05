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

Authorization = Union[raw.types.auth.Authorization, raw.types.auth.AuthorizationSignUpRequired]


# noinspection PyRedeclaration
class Authorization:  # type: ignore
    """This base type has 2 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`auth.Authorization <pyrosex.raw.types.auth.Authorization>`
            - :obj:`auth.AuthorizationSignUpRequired <pyrosex.raw.types.auth.AuthorizationSignUpRequired>`

    See Also:
        This object can be returned by 6 methods:

        .. hlist::
            :columns: 2

            - :obj:`auth.SignUp <pyrosex.raw.functions.auth.SignUp>`
            - :obj:`auth.SignIn <pyrosex.raw.functions.auth.SignIn>`
            - :obj:`auth.ImportAuthorization <pyrosex.raw.functions.auth.ImportAuthorization>`
            - :obj:`auth.ImportBotAuthorization <pyrosex.raw.functions.auth.ImportBotAuthorization>`
            - :obj:`auth.CheckPassword <pyrosex.raw.functions.auth.CheckPassword>`
            - :obj:`auth.RecoverPassword <pyrosex.raw.functions.auth.RecoverPassword>`
    """

    QUALNAME = "pyrosex.raw.base.auth.Authorization"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/authorization")
