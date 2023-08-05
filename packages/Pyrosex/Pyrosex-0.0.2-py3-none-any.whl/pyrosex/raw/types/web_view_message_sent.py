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


class WebViewMessageSent(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrosex.raw.base.WebViewMessageSent`.

    Details:
        - Layer: ``143``
        - ID: ``C94511C``

    Parameters:
        msg_id (optional): :obj:`InputBotInlineMessageID <pyrosex.raw.base.InputBotInlineMessageID>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.SendWebViewResultMessage <pyrosex.raw.functions.messages.SendWebViewResultMessage>`
    """

    __slots__: List[str] = ["msg_id"]

    ID = 0xc94511c
    QUALNAME = "types.WebViewMessageSent"

    def __init__(self, *, msg_id: "raw.base.InputBotInlineMessageID" = None) -> None:
        self.msg_id = msg_id  # flags.0?InputBotInlineMessageID

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebViewMessageSent":
        
        flags = Int.read(b)
        
        msg_id = TLObject.read(b) if flags & (1 << 0) else None
        
        return WebViewMessageSent(msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.msg_id is not None else 0
        b.write(Int(flags))
        
        if self.msg_id is not None:
            b.write(self.msg_id.write())
        
        return b.getvalue()
