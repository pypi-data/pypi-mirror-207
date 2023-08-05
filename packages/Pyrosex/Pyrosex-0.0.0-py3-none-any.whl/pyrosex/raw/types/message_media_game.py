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


class MessageMediaGame(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrosex.raw.base.MessageMedia`.

    Details:
        - Layer: ``143``
        - ID: ``FDB19008``

    Parameters:
        game: :obj:`Game <pyrosex.raw.base.Game>`

    See Also:
        This object can be returned by 3 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetWebPagePreview <pyrosex.raw.functions.messages.GetWebPagePreview>`
            - :obj:`messages.UploadMedia <pyrosex.raw.functions.messages.UploadMedia>`
            - :obj:`messages.UploadImportedMedia <pyrosex.raw.functions.messages.UploadImportedMedia>`
    """

    __slots__: List[str] = ["game"]

    ID = 0xfdb19008
    QUALNAME = "types.MessageMediaGame"

    def __init__(self, *, game: "raw.base.Game") -> None:
        self.game = game  # Game

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGame":
        # No flags
        
        game = TLObject.read(b)
        
        return MessageMediaGame(game=game)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.game.write())
        
        return b.getvalue()
