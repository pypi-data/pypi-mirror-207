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

DocumentAttribute = Union[raw.types.DocumentAttributeAnimated, raw.types.DocumentAttributeAudio, raw.types.DocumentAttributeFilename, raw.types.DocumentAttributeHasStickers, raw.types.DocumentAttributeImageSize, raw.types.DocumentAttributeSticker, raw.types.DocumentAttributeVideo]


# noinspection PyRedeclaration
class DocumentAttribute:  # type: ignore
    """This base type has 7 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`DocumentAttributeAnimated <pyrosex.raw.types.DocumentAttributeAnimated>`
            - :obj:`DocumentAttributeAudio <pyrosex.raw.types.DocumentAttributeAudio>`
            - :obj:`DocumentAttributeFilename <pyrosex.raw.types.DocumentAttributeFilename>`
            - :obj:`DocumentAttributeHasStickers <pyrosex.raw.types.DocumentAttributeHasStickers>`
            - :obj:`DocumentAttributeImageSize <pyrosex.raw.types.DocumentAttributeImageSize>`
            - :obj:`DocumentAttributeSticker <pyrosex.raw.types.DocumentAttributeSticker>`
            - :obj:`DocumentAttributeVideo <pyrosex.raw.types.DocumentAttributeVideo>`
    """

    QUALNAME = "pyrosex.raw.base.DocumentAttribute"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/document-attribute")
