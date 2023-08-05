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

MessagesFilter = Union[raw.types.InputMessagesFilterChatPhotos, raw.types.InputMessagesFilterContacts, raw.types.InputMessagesFilterDocument, raw.types.InputMessagesFilterEmpty, raw.types.InputMessagesFilterGeo, raw.types.InputMessagesFilterGif, raw.types.InputMessagesFilterMusic, raw.types.InputMessagesFilterMyMentions, raw.types.InputMessagesFilterPhoneCalls, raw.types.InputMessagesFilterPhotoVideo, raw.types.InputMessagesFilterPhotos, raw.types.InputMessagesFilterPinned, raw.types.InputMessagesFilterRoundVideo, raw.types.InputMessagesFilterRoundVoice, raw.types.InputMessagesFilterUrl, raw.types.InputMessagesFilterVideo, raw.types.InputMessagesFilterVoice]


# noinspection PyRedeclaration
class MessagesFilter:  # type: ignore
    """This base type has 17 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputMessagesFilterChatPhotos <pyrosex.raw.types.InputMessagesFilterChatPhotos>`
            - :obj:`InputMessagesFilterContacts <pyrosex.raw.types.InputMessagesFilterContacts>`
            - :obj:`InputMessagesFilterDocument <pyrosex.raw.types.InputMessagesFilterDocument>`
            - :obj:`InputMessagesFilterEmpty <pyrosex.raw.types.InputMessagesFilterEmpty>`
            - :obj:`InputMessagesFilterGeo <pyrosex.raw.types.InputMessagesFilterGeo>`
            - :obj:`InputMessagesFilterGif <pyrosex.raw.types.InputMessagesFilterGif>`
            - :obj:`InputMessagesFilterMusic <pyrosex.raw.types.InputMessagesFilterMusic>`
            - :obj:`InputMessagesFilterMyMentions <pyrosex.raw.types.InputMessagesFilterMyMentions>`
            - :obj:`InputMessagesFilterPhoneCalls <pyrosex.raw.types.InputMessagesFilterPhoneCalls>`
            - :obj:`InputMessagesFilterPhotoVideo <pyrosex.raw.types.InputMessagesFilterPhotoVideo>`
            - :obj:`InputMessagesFilterPhotos <pyrosex.raw.types.InputMessagesFilterPhotos>`
            - :obj:`InputMessagesFilterPinned <pyrosex.raw.types.InputMessagesFilterPinned>`
            - :obj:`InputMessagesFilterRoundVideo <pyrosex.raw.types.InputMessagesFilterRoundVideo>`
            - :obj:`InputMessagesFilterRoundVoice <pyrosex.raw.types.InputMessagesFilterRoundVoice>`
            - :obj:`InputMessagesFilterUrl <pyrosex.raw.types.InputMessagesFilterUrl>`
            - :obj:`InputMessagesFilterVideo <pyrosex.raw.types.InputMessagesFilterVideo>`
            - :obj:`InputMessagesFilterVoice <pyrosex.raw.types.InputMessagesFilterVoice>`
    """

    QUALNAME = "pyrosex.raw.base.MessagesFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/messages-filter")
