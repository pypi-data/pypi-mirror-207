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


class Support(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrosex.raw.base.help.Support`.

    Details:
        - Layer: ``143``
        - ID: ``17C6B5F6``

    Parameters:
        phone_number: ``str``
        user: :obj:`User <pyrosex.raw.base.User>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`help.GetSupport <pyrosex.raw.functions.help.GetSupport>`
    """

    __slots__: List[str] = ["phone_number", "user"]

    ID = 0x17c6b5f6
    QUALNAME = "types.help.Support"

    def __init__(self, *, phone_number: str, user: "raw.base.User") -> None:
        self.phone_number = phone_number  # string
        self.user = user  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Support":
        # No flags
        
        phone_number = String.read(b)
        
        user = TLObject.read(b)
        
        return Support(phone_number=phone_number, user=user)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone_number))
        
        b.write(self.user.write())
        
        return b.getvalue()
