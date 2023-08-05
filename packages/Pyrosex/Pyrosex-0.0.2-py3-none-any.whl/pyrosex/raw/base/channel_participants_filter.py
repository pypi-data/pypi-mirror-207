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

ChannelParticipantsFilter = Union[raw.types.ChannelParticipantsAdmins, raw.types.ChannelParticipantsBanned, raw.types.ChannelParticipantsBots, raw.types.ChannelParticipantsContacts, raw.types.ChannelParticipantsKicked, raw.types.ChannelParticipantsMentions, raw.types.ChannelParticipantsRecent, raw.types.ChannelParticipantsSearch]


# noinspection PyRedeclaration
class ChannelParticipantsFilter:  # type: ignore
    """This base type has 8 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`ChannelParticipantsAdmins <pyrosex.raw.types.ChannelParticipantsAdmins>`
            - :obj:`ChannelParticipantsBanned <pyrosex.raw.types.ChannelParticipantsBanned>`
            - :obj:`ChannelParticipantsBots <pyrosex.raw.types.ChannelParticipantsBots>`
            - :obj:`ChannelParticipantsContacts <pyrosex.raw.types.ChannelParticipantsContacts>`
            - :obj:`ChannelParticipantsKicked <pyrosex.raw.types.ChannelParticipantsKicked>`
            - :obj:`ChannelParticipantsMentions <pyrosex.raw.types.ChannelParticipantsMentions>`
            - :obj:`ChannelParticipantsRecent <pyrosex.raw.types.ChannelParticipantsRecent>`
            - :obj:`ChannelParticipantsSearch <pyrosex.raw.types.ChannelParticipantsSearch>`
    """

    QUALNAME = "pyrosex.raw.base.ChannelParticipantsFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/channel-participants-filter")
