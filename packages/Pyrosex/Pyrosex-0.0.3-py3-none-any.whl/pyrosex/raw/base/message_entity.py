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

MessageEntity = Union[raw.types.InputMessageEntityMentionName, raw.types.MessageEntityBankCard, raw.types.MessageEntityBlockquote, raw.types.MessageEntityBold, raw.types.MessageEntityBotCommand, raw.types.MessageEntityCashtag, raw.types.MessageEntityCode, raw.types.MessageEntityEmail, raw.types.MessageEntityHashtag, raw.types.MessageEntityItalic, raw.types.MessageEntityMention, raw.types.MessageEntityMentionName, raw.types.MessageEntityPhone, raw.types.MessageEntityPre, raw.types.MessageEntitySpoiler, raw.types.MessageEntityStrike, raw.types.MessageEntityTextUrl, raw.types.MessageEntityUnderline, raw.types.MessageEntityUnknown, raw.types.MessageEntityUrl]


# noinspection PyRedeclaration
class MessageEntity:  # type: ignore
    """This base type has 20 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputMessageEntityMentionName <pyrosex.raw.types.InputMessageEntityMentionName>`
            - :obj:`MessageEntityBankCard <pyrosex.raw.types.MessageEntityBankCard>`
            - :obj:`MessageEntityBlockquote <pyrosex.raw.types.MessageEntityBlockquote>`
            - :obj:`MessageEntityBold <pyrosex.raw.types.MessageEntityBold>`
            - :obj:`MessageEntityBotCommand <pyrosex.raw.types.MessageEntityBotCommand>`
            - :obj:`MessageEntityCashtag <pyrosex.raw.types.MessageEntityCashtag>`
            - :obj:`MessageEntityCode <pyrosex.raw.types.MessageEntityCode>`
            - :obj:`MessageEntityEmail <pyrosex.raw.types.MessageEntityEmail>`
            - :obj:`MessageEntityHashtag <pyrosex.raw.types.MessageEntityHashtag>`
            - :obj:`MessageEntityItalic <pyrosex.raw.types.MessageEntityItalic>`
            - :obj:`MessageEntityMention <pyrosex.raw.types.MessageEntityMention>`
            - :obj:`MessageEntityMentionName <pyrosex.raw.types.MessageEntityMentionName>`
            - :obj:`MessageEntityPhone <pyrosex.raw.types.MessageEntityPhone>`
            - :obj:`MessageEntityPre <pyrosex.raw.types.MessageEntityPre>`
            - :obj:`MessageEntitySpoiler <pyrosex.raw.types.MessageEntitySpoiler>`
            - :obj:`MessageEntityStrike <pyrosex.raw.types.MessageEntityStrike>`
            - :obj:`MessageEntityTextUrl <pyrosex.raw.types.MessageEntityTextUrl>`
            - :obj:`MessageEntityUnderline <pyrosex.raw.types.MessageEntityUnderline>`
            - :obj:`MessageEntityUnknown <pyrosex.raw.types.MessageEntityUnknown>`
            - :obj:`MessageEntityUrl <pyrosex.raw.types.MessageEntityUrl>`
    """

    QUALNAME = "pyrosex.raw.base.MessageEntity"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/message-entity")
