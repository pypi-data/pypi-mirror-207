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

from io import BytesIO

from pyrosex.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrosex.raw.core import TLObject
from pyrosex import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class AuthorizationForm(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrosex.raw.base.account.AuthorizationForm`.

    Details:
        - Layer: ``143``
        - ID: ``AD2E1CD8``

    Parameters:
        required_types: List of :obj:`SecureRequiredType <pyrosex.raw.base.SecureRequiredType>`
        values: List of :obj:`SecureValue <pyrosex.raw.base.SecureValue>`
        errors: List of :obj:`SecureValueError <pyrosex.raw.base.SecureValueError>`
        users: List of :obj:`User <pyrosex.raw.base.User>`
        privacy_policy_url (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.GetAuthorizationForm <pyrosex.raw.functions.account.GetAuthorizationForm>`
    """

    __slots__: List[str] = ["required_types", "values", "errors", "users", "privacy_policy_url"]

    ID = 0xad2e1cd8
    QUALNAME = "types.account.AuthorizationForm"

    def __init__(self, *, required_types: List["raw.base.SecureRequiredType"], values: List["raw.base.SecureValue"], errors: List["raw.base.SecureValueError"], users: List["raw.base.User"], privacy_policy_url: Optional[str] = None) -> None:
        self.required_types = required_types  # Vector<SecureRequiredType>
        self.values = values  # Vector<SecureValue>
        self.errors = errors  # Vector<SecureValueError>
        self.users = users  # Vector<User>
        self.privacy_policy_url = privacy_policy_url  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AuthorizationForm":
        
        flags = Int.read(b)
        
        required_types = TLObject.read(b)
        
        values = TLObject.read(b)
        
        errors = TLObject.read(b)
        
        users = TLObject.read(b)
        
        privacy_policy_url = String.read(b) if flags & (1 << 0) else None
        return AuthorizationForm(required_types=required_types, values=values, errors=errors, users=users, privacy_policy_url=privacy_policy_url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.privacy_policy_url is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.required_types))
        
        b.write(Vector(self.values))
        
        b.write(Vector(self.errors))
        
        b.write(Vector(self.users))
        
        if self.privacy_policy_url is not None:
            b.write(String(self.privacy_policy_url))
        
        return b.getvalue()
