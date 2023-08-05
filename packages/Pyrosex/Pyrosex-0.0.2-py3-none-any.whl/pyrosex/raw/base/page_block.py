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

PageBlock = Union[raw.types.PageBlockAnchor, raw.types.PageBlockAudio, raw.types.PageBlockAuthorDate, raw.types.PageBlockBlockquote, raw.types.PageBlockChannel, raw.types.PageBlockCollage, raw.types.PageBlockCover, raw.types.PageBlockDetails, raw.types.PageBlockDivider, raw.types.PageBlockEmbed, raw.types.PageBlockEmbedPost, raw.types.PageBlockFooter, raw.types.PageBlockHeader, raw.types.PageBlockKicker, raw.types.PageBlockList, raw.types.PageBlockMap, raw.types.PageBlockOrderedList, raw.types.PageBlockParagraph, raw.types.PageBlockPhoto, raw.types.PageBlockPreformatted, raw.types.PageBlockPullquote, raw.types.PageBlockRelatedArticles, raw.types.PageBlockSlideshow, raw.types.PageBlockSubheader, raw.types.PageBlockSubtitle, raw.types.PageBlockTable, raw.types.PageBlockTitle, raw.types.PageBlockUnsupported, raw.types.PageBlockVideo]


# noinspection PyRedeclaration
class PageBlock:  # type: ignore
    """This base type has 29 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`PageBlockAnchor <pyrosex.raw.types.PageBlockAnchor>`
            - :obj:`PageBlockAudio <pyrosex.raw.types.PageBlockAudio>`
            - :obj:`PageBlockAuthorDate <pyrosex.raw.types.PageBlockAuthorDate>`
            - :obj:`PageBlockBlockquote <pyrosex.raw.types.PageBlockBlockquote>`
            - :obj:`PageBlockChannel <pyrosex.raw.types.PageBlockChannel>`
            - :obj:`PageBlockCollage <pyrosex.raw.types.PageBlockCollage>`
            - :obj:`PageBlockCover <pyrosex.raw.types.PageBlockCover>`
            - :obj:`PageBlockDetails <pyrosex.raw.types.PageBlockDetails>`
            - :obj:`PageBlockDivider <pyrosex.raw.types.PageBlockDivider>`
            - :obj:`PageBlockEmbed <pyrosex.raw.types.PageBlockEmbed>`
            - :obj:`PageBlockEmbedPost <pyrosex.raw.types.PageBlockEmbedPost>`
            - :obj:`PageBlockFooter <pyrosex.raw.types.PageBlockFooter>`
            - :obj:`PageBlockHeader <pyrosex.raw.types.PageBlockHeader>`
            - :obj:`PageBlockKicker <pyrosex.raw.types.PageBlockKicker>`
            - :obj:`PageBlockList <pyrosex.raw.types.PageBlockList>`
            - :obj:`PageBlockMap <pyrosex.raw.types.PageBlockMap>`
            - :obj:`PageBlockOrderedList <pyrosex.raw.types.PageBlockOrderedList>`
            - :obj:`PageBlockParagraph <pyrosex.raw.types.PageBlockParagraph>`
            - :obj:`PageBlockPhoto <pyrosex.raw.types.PageBlockPhoto>`
            - :obj:`PageBlockPreformatted <pyrosex.raw.types.PageBlockPreformatted>`
            - :obj:`PageBlockPullquote <pyrosex.raw.types.PageBlockPullquote>`
            - :obj:`PageBlockRelatedArticles <pyrosex.raw.types.PageBlockRelatedArticles>`
            - :obj:`PageBlockSlideshow <pyrosex.raw.types.PageBlockSlideshow>`
            - :obj:`PageBlockSubheader <pyrosex.raw.types.PageBlockSubheader>`
            - :obj:`PageBlockSubtitle <pyrosex.raw.types.PageBlockSubtitle>`
            - :obj:`PageBlockTable <pyrosex.raw.types.PageBlockTable>`
            - :obj:`PageBlockTitle <pyrosex.raw.types.PageBlockTitle>`
            - :obj:`PageBlockUnsupported <pyrosex.raw.types.PageBlockUnsupported>`
            - :obj:`PageBlockVideo <pyrosex.raw.types.PageBlockVideo>`
    """

    QUALNAME = "pyrosex.raw.base.PageBlock"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/page-block")
