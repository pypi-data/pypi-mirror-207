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

KeyboardButton = Union[raw.types.InputKeyboardButtonUrlAuth, raw.types.InputKeyboardButtonUserProfile, raw.types.KeyboardButton, raw.types.KeyboardButtonBuy, raw.types.KeyboardButtonCallback, raw.types.KeyboardButtonGame, raw.types.KeyboardButtonRequestGeoLocation, raw.types.KeyboardButtonRequestPhone, raw.types.KeyboardButtonRequestPoll, raw.types.KeyboardButtonSimpleWebView, raw.types.KeyboardButtonSwitchInline, raw.types.KeyboardButtonUrl, raw.types.KeyboardButtonUrlAuth, raw.types.KeyboardButtonUserProfile, raw.types.KeyboardButtonWebView]


# noinspection PyRedeclaration
class KeyboardButton:  # type: ignore
    """This base type has 15 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputKeyboardButtonUrlAuth <pyrosex.raw.types.InputKeyboardButtonUrlAuth>`
            - :obj:`InputKeyboardButtonUserProfile <pyrosex.raw.types.InputKeyboardButtonUserProfile>`
            - :obj:`KeyboardButton <pyrosex.raw.types.KeyboardButton>`
            - :obj:`KeyboardButtonBuy <pyrosex.raw.types.KeyboardButtonBuy>`
            - :obj:`KeyboardButtonCallback <pyrosex.raw.types.KeyboardButtonCallback>`
            - :obj:`KeyboardButtonGame <pyrosex.raw.types.KeyboardButtonGame>`
            - :obj:`KeyboardButtonRequestGeoLocation <pyrosex.raw.types.KeyboardButtonRequestGeoLocation>`
            - :obj:`KeyboardButtonRequestPhone <pyrosex.raw.types.KeyboardButtonRequestPhone>`
            - :obj:`KeyboardButtonRequestPoll <pyrosex.raw.types.KeyboardButtonRequestPoll>`
            - :obj:`KeyboardButtonSimpleWebView <pyrosex.raw.types.KeyboardButtonSimpleWebView>`
            - :obj:`KeyboardButtonSwitchInline <pyrosex.raw.types.KeyboardButtonSwitchInline>`
            - :obj:`KeyboardButtonUrl <pyrosex.raw.types.KeyboardButtonUrl>`
            - :obj:`KeyboardButtonUrlAuth <pyrosex.raw.types.KeyboardButtonUrlAuth>`
            - :obj:`KeyboardButtonUserProfile <pyrosex.raw.types.KeyboardButtonUserProfile>`
            - :obj:`KeyboardButtonWebView <pyrosex.raw.types.KeyboardButtonWebView>`
    """

    QUALNAME = "pyrosex.raw.base.KeyboardButton"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/keyboard-button")
