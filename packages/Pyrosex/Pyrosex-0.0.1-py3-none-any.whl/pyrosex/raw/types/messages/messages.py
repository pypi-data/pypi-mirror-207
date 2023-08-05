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


class Messages(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrosex.raw.base.messages.Messages`.

    Details:
        - Layer: ``143``
        - ID: ``8C718E87``

    Parameters:
        messages: List of :obj:`Message <pyrosex.raw.base.Message>`
        chats: List of :obj:`Chat <pyrosex.raw.base.Chat>`
        users: List of :obj:`User <pyrosex.raw.base.User>`

    See Also:
        This object can be returned by 13 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetMessages <pyrosex.raw.functions.messages.GetMessages>`
            - :obj:`messages.GetHistory <pyrosex.raw.functions.messages.GetHistory>`
            - :obj:`messages.Search <pyrosex.raw.functions.messages.Search>`
            - :obj:`messages.SearchGlobal <pyrosex.raw.functions.messages.SearchGlobal>`
            - :obj:`messages.GetUnreadMentions <pyrosex.raw.functions.messages.GetUnreadMentions>`
            - :obj:`messages.GetRecentLocations <pyrosex.raw.functions.messages.GetRecentLocations>`
            - :obj:`messages.GetScheduledHistory <pyrosex.raw.functions.messages.GetScheduledHistory>`
            - :obj:`messages.GetScheduledMessages <pyrosex.raw.functions.messages.GetScheduledMessages>`
            - :obj:`messages.GetReplies <pyrosex.raw.functions.messages.GetReplies>`
            - :obj:`messages.GetUnreadReactions <pyrosex.raw.functions.messages.GetUnreadReactions>`
            - :obj:`messages.SearchSentMedia <pyrosex.raw.functions.messages.SearchSentMedia>`
            - :obj:`channels.GetMessages <pyrosex.raw.functions.channels.GetMessages>`
            - :obj:`stats.GetMessagePublicForwards <pyrosex.raw.functions.stats.GetMessagePublicForwards>`
    """

    __slots__: List[str] = ["messages", "chats", "users"]

    ID = 0x8c718e87
    QUALNAME = "types.messages.Messages"

    def __init__(self, *, messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Messages":
        # No flags
        
        messages = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return Messages(messages=messages, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
