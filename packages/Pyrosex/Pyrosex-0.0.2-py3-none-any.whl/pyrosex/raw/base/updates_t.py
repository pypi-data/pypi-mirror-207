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

Updates = Union[raw.types.UpdateShort, raw.types.UpdateShortChatMessage, raw.types.UpdateShortMessage, raw.types.UpdateShortSentMessage, raw.types.Updates, raw.types.UpdatesCombined, raw.types.UpdatesTooLong]


# noinspection PyRedeclaration
class Updates:  # type: ignore
    """This base type has 7 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`UpdateShort <pyrosex.raw.types.UpdateShort>`
            - :obj:`UpdateShortChatMessage <pyrosex.raw.types.UpdateShortChatMessage>`
            - :obj:`UpdateShortMessage <pyrosex.raw.types.UpdateShortMessage>`
            - :obj:`UpdateShortSentMessage <pyrosex.raw.types.UpdateShortSentMessage>`
            - :obj:`Updates <pyrosex.raw.types.Updates>`
            - :obj:`UpdatesCombined <pyrosex.raw.types.UpdatesCombined>`
            - :obj:`UpdatesTooLong <pyrosex.raw.types.UpdatesTooLong>`

    See Also:
        This object can be returned by 77 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.GetNotifyExceptions <pyrosex.raw.functions.account.GetNotifyExceptions>`
            - :obj:`contacts.DeleteContacts <pyrosex.raw.functions.contacts.DeleteContacts>`
            - :obj:`contacts.AddContact <pyrosex.raw.functions.contacts.AddContact>`
            - :obj:`contacts.AcceptContact <pyrosex.raw.functions.contacts.AcceptContact>`
            - :obj:`contacts.GetLocated <pyrosex.raw.functions.contacts.GetLocated>`
            - :obj:`contacts.BlockFromReplies <pyrosex.raw.functions.contacts.BlockFromReplies>`
            - :obj:`messages.SendMessage <pyrosex.raw.functions.messages.SendMessage>`
            - :obj:`messages.SendMedia <pyrosex.raw.functions.messages.SendMedia>`
            - :obj:`messages.ForwardMessages <pyrosex.raw.functions.messages.ForwardMessages>`
            - :obj:`messages.EditChatTitle <pyrosex.raw.functions.messages.EditChatTitle>`
            - :obj:`messages.EditChatPhoto <pyrosex.raw.functions.messages.EditChatPhoto>`
            - :obj:`messages.AddChatUser <pyrosex.raw.functions.messages.AddChatUser>`
            - :obj:`messages.DeleteChatUser <pyrosex.raw.functions.messages.DeleteChatUser>`
            - :obj:`messages.CreateChat <pyrosex.raw.functions.messages.CreateChat>`
            - :obj:`messages.ImportChatInvite <pyrosex.raw.functions.messages.ImportChatInvite>`
            - :obj:`messages.StartBot <pyrosex.raw.functions.messages.StartBot>`
            - :obj:`messages.MigrateChat <pyrosex.raw.functions.messages.MigrateChat>`
            - :obj:`messages.SendInlineBotResult <pyrosex.raw.functions.messages.SendInlineBotResult>`
            - :obj:`messages.EditMessage <pyrosex.raw.functions.messages.EditMessage>`
            - :obj:`messages.GetAllDrafts <pyrosex.raw.functions.messages.GetAllDrafts>`
            - :obj:`messages.SetGameScore <pyrosex.raw.functions.messages.SetGameScore>`
            - :obj:`messages.SendScreenshotNotification <pyrosex.raw.functions.messages.SendScreenshotNotification>`
            - :obj:`messages.SendMultiMedia <pyrosex.raw.functions.messages.SendMultiMedia>`
            - :obj:`messages.UpdatePinnedMessage <pyrosex.raw.functions.messages.UpdatePinnedMessage>`
            - :obj:`messages.SendVote <pyrosex.raw.functions.messages.SendVote>`
            - :obj:`messages.GetPollResults <pyrosex.raw.functions.messages.GetPollResults>`
            - :obj:`messages.EditChatDefaultBannedRights <pyrosex.raw.functions.messages.EditChatDefaultBannedRights>`
            - :obj:`messages.SendScheduledMessages <pyrosex.raw.functions.messages.SendScheduledMessages>`
            - :obj:`messages.DeleteScheduledMessages <pyrosex.raw.functions.messages.DeleteScheduledMessages>`
            - :obj:`messages.SetHistoryTTL <pyrosex.raw.functions.messages.SetHistoryTTL>`
            - :obj:`messages.SetChatTheme <pyrosex.raw.functions.messages.SetChatTheme>`
            - :obj:`messages.HideChatJoinRequest <pyrosex.raw.functions.messages.HideChatJoinRequest>`
            - :obj:`messages.HideAllChatJoinRequests <pyrosex.raw.functions.messages.HideAllChatJoinRequests>`
            - :obj:`messages.ToggleNoForwards <pyrosex.raw.functions.messages.ToggleNoForwards>`
            - :obj:`messages.SendReaction <pyrosex.raw.functions.messages.SendReaction>`
            - :obj:`messages.GetMessagesReactions <pyrosex.raw.functions.messages.GetMessagesReactions>`
            - :obj:`messages.SetChatAvailableReactions <pyrosex.raw.functions.messages.SetChatAvailableReactions>`
            - :obj:`messages.SendWebViewData <pyrosex.raw.functions.messages.SendWebViewData>`
            - :obj:`help.GetAppChangelog <pyrosex.raw.functions.help.GetAppChangelog>`
            - :obj:`channels.CreateChannel <pyrosex.raw.functions.channels.CreateChannel>`
            - :obj:`channels.EditAdmin <pyrosex.raw.functions.channels.EditAdmin>`
            - :obj:`channels.EditTitle <pyrosex.raw.functions.channels.EditTitle>`
            - :obj:`channels.EditPhoto <pyrosex.raw.functions.channels.EditPhoto>`
            - :obj:`channels.JoinChannel <pyrosex.raw.functions.channels.JoinChannel>`
            - :obj:`channels.LeaveChannel <pyrosex.raw.functions.channels.LeaveChannel>`
            - :obj:`channels.InviteToChannel <pyrosex.raw.functions.channels.InviteToChannel>`
            - :obj:`channels.DeleteChannel <pyrosex.raw.functions.channels.DeleteChannel>`
            - :obj:`channels.ToggleSignatures <pyrosex.raw.functions.channels.ToggleSignatures>`
            - :obj:`channels.EditBanned <pyrosex.raw.functions.channels.EditBanned>`
            - :obj:`channels.DeleteHistory <pyrosex.raw.functions.channels.DeleteHistory>`
            - :obj:`channels.TogglePreHistoryHidden <pyrosex.raw.functions.channels.TogglePreHistoryHidden>`
            - :obj:`channels.EditCreator <pyrosex.raw.functions.channels.EditCreator>`
            - :obj:`channels.ToggleSlowMode <pyrosex.raw.functions.channels.ToggleSlowMode>`
            - :obj:`channels.ConvertToGigagroup <pyrosex.raw.functions.channels.ConvertToGigagroup>`
            - :obj:`channels.ToggleJoinToSend <pyrosex.raw.functions.channels.ToggleJoinToSend>`
            - :obj:`channels.ToggleJoinRequest <pyrosex.raw.functions.channels.ToggleJoinRequest>`
            - :obj:`payments.AssignAppStoreTransaction <pyrosex.raw.functions.payments.AssignAppStoreTransaction>`
            - :obj:`payments.AssignPlayMarketTransaction <pyrosex.raw.functions.payments.AssignPlayMarketTransaction>`
            - :obj:`payments.RestorePlayMarketReceipt <pyrosex.raw.functions.payments.RestorePlayMarketReceipt>`
            - :obj:`payments.RequestRecurringPayment <pyrosex.raw.functions.payments.RequestRecurringPayment>`
            - :obj:`phone.DiscardCall <pyrosex.raw.functions.phone.DiscardCall>`
            - :obj:`phone.SetCallRating <pyrosex.raw.functions.phone.SetCallRating>`
            - :obj:`phone.CreateGroupCall <pyrosex.raw.functions.phone.CreateGroupCall>`
            - :obj:`phone.JoinGroupCall <pyrosex.raw.functions.phone.JoinGroupCall>`
            - :obj:`phone.LeaveGroupCall <pyrosex.raw.functions.phone.LeaveGroupCall>`
            - :obj:`phone.InviteToGroupCall <pyrosex.raw.functions.phone.InviteToGroupCall>`
            - :obj:`phone.DiscardGroupCall <pyrosex.raw.functions.phone.DiscardGroupCall>`
            - :obj:`phone.ToggleGroupCallSettings <pyrosex.raw.functions.phone.ToggleGroupCallSettings>`
            - :obj:`phone.ToggleGroupCallRecord <pyrosex.raw.functions.phone.ToggleGroupCallRecord>`
            - :obj:`phone.EditGroupCallParticipant <pyrosex.raw.functions.phone.EditGroupCallParticipant>`
            - :obj:`phone.EditGroupCallTitle <pyrosex.raw.functions.phone.EditGroupCallTitle>`
            - :obj:`phone.ToggleGroupCallStartSubscription <pyrosex.raw.functions.phone.ToggleGroupCallStartSubscription>`
            - :obj:`phone.StartScheduledGroupCall <pyrosex.raw.functions.phone.StartScheduledGroupCall>`
            - :obj:`phone.JoinGroupCallPresentation <pyrosex.raw.functions.phone.JoinGroupCallPresentation>`
            - :obj:`phone.LeaveGroupCallPresentation <pyrosex.raw.functions.phone.LeaveGroupCallPresentation>`
            - :obj:`folders.EditPeerFolders <pyrosex.raw.functions.folders.EditPeerFolders>`
            - :obj:`folders.DeleteFolder <pyrosex.raw.functions.folders.DeleteFolder>`
    """

    QUALNAME = "pyrosex.raw.base.Updates"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/updates")
