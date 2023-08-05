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

InputPrivacyRule = Union[raw.types.InputPrivacyValueAllowAll, raw.types.InputPrivacyValueAllowChatParticipants, raw.types.InputPrivacyValueAllowContacts, raw.types.InputPrivacyValueAllowUsers, raw.types.InputPrivacyValueDisallowAll, raw.types.InputPrivacyValueDisallowChatParticipants, raw.types.InputPrivacyValueDisallowContacts, raw.types.InputPrivacyValueDisallowUsers]


# noinspection PyRedeclaration
class InputPrivacyRule:  # type: ignore
    """This base type has 8 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputPrivacyValueAllowAll <pyrosex.raw.types.InputPrivacyValueAllowAll>`
            - :obj:`InputPrivacyValueAllowChatParticipants <pyrosex.raw.types.InputPrivacyValueAllowChatParticipants>`
            - :obj:`InputPrivacyValueAllowContacts <pyrosex.raw.types.InputPrivacyValueAllowContacts>`
            - :obj:`InputPrivacyValueAllowUsers <pyrosex.raw.types.InputPrivacyValueAllowUsers>`
            - :obj:`InputPrivacyValueDisallowAll <pyrosex.raw.types.InputPrivacyValueDisallowAll>`
            - :obj:`InputPrivacyValueDisallowChatParticipants <pyrosex.raw.types.InputPrivacyValueDisallowChatParticipants>`
            - :obj:`InputPrivacyValueDisallowContacts <pyrosex.raw.types.InputPrivacyValueDisallowContacts>`
            - :obj:`InputPrivacyValueDisallowUsers <pyrosex.raw.types.InputPrivacyValueDisallowUsers>`
    """

    QUALNAME = "pyrosex.raw.base.InputPrivacyRule"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/input-privacy-rule")
