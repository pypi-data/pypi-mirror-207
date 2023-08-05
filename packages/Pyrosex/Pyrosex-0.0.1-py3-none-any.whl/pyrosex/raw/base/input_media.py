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

InputMedia = Union[raw.types.InputMediaContact, raw.types.InputMediaDice, raw.types.InputMediaDocument, raw.types.InputMediaDocumentExternal, raw.types.InputMediaEmpty, raw.types.InputMediaGame, raw.types.InputMediaGeoLive, raw.types.InputMediaGeoPoint, raw.types.InputMediaInvoice, raw.types.InputMediaPhoto, raw.types.InputMediaPhotoExternal, raw.types.InputMediaPoll, raw.types.InputMediaUploadedDocument, raw.types.InputMediaUploadedPhoto, raw.types.InputMediaVenue]


# noinspection PyRedeclaration
class InputMedia:  # type: ignore
    """This base type has 15 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputMediaContact <pyrosex.raw.types.InputMediaContact>`
            - :obj:`InputMediaDice <pyrosex.raw.types.InputMediaDice>`
            - :obj:`InputMediaDocument <pyrosex.raw.types.InputMediaDocument>`
            - :obj:`InputMediaDocumentExternal <pyrosex.raw.types.InputMediaDocumentExternal>`
            - :obj:`InputMediaEmpty <pyrosex.raw.types.InputMediaEmpty>`
            - :obj:`InputMediaGame <pyrosex.raw.types.InputMediaGame>`
            - :obj:`InputMediaGeoLive <pyrosex.raw.types.InputMediaGeoLive>`
            - :obj:`InputMediaGeoPoint <pyrosex.raw.types.InputMediaGeoPoint>`
            - :obj:`InputMediaInvoice <pyrosex.raw.types.InputMediaInvoice>`
            - :obj:`InputMediaPhoto <pyrosex.raw.types.InputMediaPhoto>`
            - :obj:`InputMediaPhotoExternal <pyrosex.raw.types.InputMediaPhotoExternal>`
            - :obj:`InputMediaPoll <pyrosex.raw.types.InputMediaPoll>`
            - :obj:`InputMediaUploadedDocument <pyrosex.raw.types.InputMediaUploadedDocument>`
            - :obj:`InputMediaUploadedPhoto <pyrosex.raw.types.InputMediaUploadedPhoto>`
            - :obj:`InputMediaVenue <pyrosex.raw.types.InputMediaVenue>`
    """

    QUALNAME = "pyrosex.raw.base.InputMedia"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/input-media")
