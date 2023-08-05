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

TopPeerCategory = Union[raw.types.TopPeerCategoryBotsInline, raw.types.TopPeerCategoryBotsPM, raw.types.TopPeerCategoryChannels, raw.types.TopPeerCategoryCorrespondents, raw.types.TopPeerCategoryForwardChats, raw.types.TopPeerCategoryForwardUsers, raw.types.TopPeerCategoryGroups, raw.types.TopPeerCategoryPhoneCalls]


# noinspection PyRedeclaration
class TopPeerCategory:  # type: ignore
    """This base type has 8 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`TopPeerCategoryBotsInline <pyrosex.raw.types.TopPeerCategoryBotsInline>`
            - :obj:`TopPeerCategoryBotsPM <pyrosex.raw.types.TopPeerCategoryBotsPM>`
            - :obj:`TopPeerCategoryChannels <pyrosex.raw.types.TopPeerCategoryChannels>`
            - :obj:`TopPeerCategoryCorrespondents <pyrosex.raw.types.TopPeerCategoryCorrespondents>`
            - :obj:`TopPeerCategoryForwardChats <pyrosex.raw.types.TopPeerCategoryForwardChats>`
            - :obj:`TopPeerCategoryForwardUsers <pyrosex.raw.types.TopPeerCategoryForwardUsers>`
            - :obj:`TopPeerCategoryGroups <pyrosex.raw.types.TopPeerCategoryGroups>`
            - :obj:`TopPeerCategoryPhoneCalls <pyrosex.raw.types.TopPeerCategoryPhoneCalls>`
    """

    QUALNAME = "pyrosex.raw.base.TopPeerCategory"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/top-peer-category")
