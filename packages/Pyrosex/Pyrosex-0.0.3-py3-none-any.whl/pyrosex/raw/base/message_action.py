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

MessageAction = Union[raw.types.MessageActionBotAllowed, raw.types.MessageActionChannelCreate, raw.types.MessageActionChannelMigrateFrom, raw.types.MessageActionChatAddUser, raw.types.MessageActionChatCreate, raw.types.MessageActionChatDeletePhoto, raw.types.MessageActionChatDeleteUser, raw.types.MessageActionChatEditPhoto, raw.types.MessageActionChatEditTitle, raw.types.MessageActionChatJoinedByLink, raw.types.MessageActionChatJoinedByRequest, raw.types.MessageActionChatMigrateTo, raw.types.MessageActionContactSignUp, raw.types.MessageActionCustomAction, raw.types.MessageActionEmpty, raw.types.MessageActionGameScore, raw.types.MessageActionGeoProximityReached, raw.types.MessageActionGroupCall, raw.types.MessageActionGroupCallScheduled, raw.types.MessageActionHistoryClear, raw.types.MessageActionInviteToGroupCall, raw.types.MessageActionPaymentSent, raw.types.MessageActionPaymentSentMe, raw.types.MessageActionPhoneCall, raw.types.MessageActionPinMessage, raw.types.MessageActionScreenshotTaken, raw.types.MessageActionSecureValuesSent, raw.types.MessageActionSecureValuesSentMe, raw.types.MessageActionSetChatTheme, raw.types.MessageActionSetMessagesTTL, raw.types.MessageActionWebViewDataSent, raw.types.MessageActionWebViewDataSentMe]


# noinspection PyRedeclaration
class MessageAction:  # type: ignore
    """This base type has 32 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`MessageActionBotAllowed <pyrosex.raw.types.MessageActionBotAllowed>`
            - :obj:`MessageActionChannelCreate <pyrosex.raw.types.MessageActionChannelCreate>`
            - :obj:`MessageActionChannelMigrateFrom <pyrosex.raw.types.MessageActionChannelMigrateFrom>`
            - :obj:`MessageActionChatAddUser <pyrosex.raw.types.MessageActionChatAddUser>`
            - :obj:`MessageActionChatCreate <pyrosex.raw.types.MessageActionChatCreate>`
            - :obj:`MessageActionChatDeletePhoto <pyrosex.raw.types.MessageActionChatDeletePhoto>`
            - :obj:`MessageActionChatDeleteUser <pyrosex.raw.types.MessageActionChatDeleteUser>`
            - :obj:`MessageActionChatEditPhoto <pyrosex.raw.types.MessageActionChatEditPhoto>`
            - :obj:`MessageActionChatEditTitle <pyrosex.raw.types.MessageActionChatEditTitle>`
            - :obj:`MessageActionChatJoinedByLink <pyrosex.raw.types.MessageActionChatJoinedByLink>`
            - :obj:`MessageActionChatJoinedByRequest <pyrosex.raw.types.MessageActionChatJoinedByRequest>`
            - :obj:`MessageActionChatMigrateTo <pyrosex.raw.types.MessageActionChatMigrateTo>`
            - :obj:`MessageActionContactSignUp <pyrosex.raw.types.MessageActionContactSignUp>`
            - :obj:`MessageActionCustomAction <pyrosex.raw.types.MessageActionCustomAction>`
            - :obj:`MessageActionEmpty <pyrosex.raw.types.MessageActionEmpty>`
            - :obj:`MessageActionGameScore <pyrosex.raw.types.MessageActionGameScore>`
            - :obj:`MessageActionGeoProximityReached <pyrosex.raw.types.MessageActionGeoProximityReached>`
            - :obj:`MessageActionGroupCall <pyrosex.raw.types.MessageActionGroupCall>`
            - :obj:`MessageActionGroupCallScheduled <pyrosex.raw.types.MessageActionGroupCallScheduled>`
            - :obj:`MessageActionHistoryClear <pyrosex.raw.types.MessageActionHistoryClear>`
            - :obj:`MessageActionInviteToGroupCall <pyrosex.raw.types.MessageActionInviteToGroupCall>`
            - :obj:`MessageActionPaymentSent <pyrosex.raw.types.MessageActionPaymentSent>`
            - :obj:`MessageActionPaymentSentMe <pyrosex.raw.types.MessageActionPaymentSentMe>`
            - :obj:`MessageActionPhoneCall <pyrosex.raw.types.MessageActionPhoneCall>`
            - :obj:`MessageActionPinMessage <pyrosex.raw.types.MessageActionPinMessage>`
            - :obj:`MessageActionScreenshotTaken <pyrosex.raw.types.MessageActionScreenshotTaken>`
            - :obj:`MessageActionSecureValuesSent <pyrosex.raw.types.MessageActionSecureValuesSent>`
            - :obj:`MessageActionSecureValuesSentMe <pyrosex.raw.types.MessageActionSecureValuesSentMe>`
            - :obj:`MessageActionSetChatTheme <pyrosex.raw.types.MessageActionSetChatTheme>`
            - :obj:`MessageActionSetMessagesTTL <pyrosex.raw.types.MessageActionSetMessagesTTL>`
            - :obj:`MessageActionWebViewDataSent <pyrosex.raw.types.MessageActionWebViewDataSent>`
            - :obj:`MessageActionWebViewDataSentMe <pyrosex.raw.types.MessageActionWebViewDataSentMe>`
    """

    QUALNAME = "pyrosex.raw.base.MessageAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/message-action")
