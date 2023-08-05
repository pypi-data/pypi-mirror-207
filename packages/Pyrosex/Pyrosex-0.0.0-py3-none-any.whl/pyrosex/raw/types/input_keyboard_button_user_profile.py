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


class InputKeyboardButtonUserProfile(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrosex.raw.base.KeyboardButton`.

    Details:
        - Layer: ``143``
        - ID: ``E988037B``

    Parameters:
        text: ``str``
        user_id: :obj:`InputUser <pyrosex.raw.base.InputUser>`
    """

    __slots__: List[str] = ["text", "user_id"]

    ID = 0xe988037b
    QUALNAME = "types.InputKeyboardButtonUserProfile"

    def __init__(self, *, text: str, user_id: "raw.base.InputUser") -> None:
        self.text = text  # string
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonUserProfile":
        # No flags
        
        text = String.read(b)
        
        user_id = TLObject.read(b)
        
        return InputKeyboardButtonUserProfile(text=text, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(self.user_id.write())
        
        return b.getvalue()
