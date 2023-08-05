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

MessageMedia = Union[raw.types.MessageMediaContact, raw.types.MessageMediaDice, raw.types.MessageMediaDocument, raw.types.MessageMediaEmpty, raw.types.MessageMediaGame, raw.types.MessageMediaGeo, raw.types.MessageMediaGeoLive, raw.types.MessageMediaInvoice, raw.types.MessageMediaPhoto, raw.types.MessageMediaPoll, raw.types.MessageMediaUnsupported, raw.types.MessageMediaVenue, raw.types.MessageMediaWebPage]


# noinspection PyRedeclaration
class MessageMedia:  # type: ignore
    """This base type has 13 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`MessageMediaContact <pyrosex.raw.types.MessageMediaContact>`
            - :obj:`MessageMediaDice <pyrosex.raw.types.MessageMediaDice>`
            - :obj:`MessageMediaDocument <pyrosex.raw.types.MessageMediaDocument>`
            - :obj:`MessageMediaEmpty <pyrosex.raw.types.MessageMediaEmpty>`
            - :obj:`MessageMediaGame <pyrosex.raw.types.MessageMediaGame>`
            - :obj:`MessageMediaGeo <pyrosex.raw.types.MessageMediaGeo>`
            - :obj:`MessageMediaGeoLive <pyrosex.raw.types.MessageMediaGeoLive>`
            - :obj:`MessageMediaInvoice <pyrosex.raw.types.MessageMediaInvoice>`
            - :obj:`MessageMediaPhoto <pyrosex.raw.types.MessageMediaPhoto>`
            - :obj:`MessageMediaPoll <pyrosex.raw.types.MessageMediaPoll>`
            - :obj:`MessageMediaUnsupported <pyrosex.raw.types.MessageMediaUnsupported>`
            - :obj:`MessageMediaVenue <pyrosex.raw.types.MessageMediaVenue>`
            - :obj:`MessageMediaWebPage <pyrosex.raw.types.MessageMediaWebPage>`

    See Also:
        This object can be returned by 3 methods:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetWebPagePreview <pyrosex.raw.functions.messages.GetWebPagePreview>`
            - :obj:`messages.UploadMedia <pyrosex.raw.functions.messages.UploadMedia>`
            - :obj:`messages.UploadImportedMedia <pyrosex.raw.functions.messages.UploadImportedMedia>`
    """

    QUALNAME = "pyrosex.raw.base.MessageMedia"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/message-media")
