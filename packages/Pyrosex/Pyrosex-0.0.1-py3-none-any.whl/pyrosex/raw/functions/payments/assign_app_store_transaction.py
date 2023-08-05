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


class AssignAppStoreTransaction(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``143``
        - ID: ``FEC13C6``

    Parameters:
        transaction_id: ``str``
        receipt: ``bytes``
        restore (optional): ``bool``

    Returns:
        :obj:`Updates <pyrosex.raw.base.Updates>`
    """

    __slots__: List[str] = ["transaction_id", "receipt", "restore"]

    ID = 0xfec13c6
    QUALNAME = "functions.payments.AssignAppStoreTransaction"

    def __init__(self, *, transaction_id: str, receipt: bytes, restore: Optional[bool] = None) -> None:
        self.transaction_id = transaction_id  # string
        self.receipt = receipt  # bytes
        self.restore = restore  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AssignAppStoreTransaction":
        
        flags = Int.read(b)
        
        restore = True if flags & (1 << 0) else False
        transaction_id = String.read(b)
        
        receipt = Bytes.read(b)
        
        return AssignAppStoreTransaction(transaction_id=transaction_id, receipt=receipt, restore=restore)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.restore else 0
        b.write(Int(flags))
        
        b.write(String(self.transaction_id))
        
        b.write(Bytes(self.receipt))
        
        return b.getvalue()
