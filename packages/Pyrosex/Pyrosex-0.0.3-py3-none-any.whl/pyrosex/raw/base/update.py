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

Update = Union[raw.types.UpdateAttachMenuBots, raw.types.UpdateBotCallbackQuery, raw.types.UpdateBotChatInviteRequester, raw.types.UpdateBotCommands, raw.types.UpdateBotInlineQuery, raw.types.UpdateBotInlineSend, raw.types.UpdateBotMenuButton, raw.types.UpdateBotPrecheckoutQuery, raw.types.UpdateBotShippingQuery, raw.types.UpdateBotStopped, raw.types.UpdateBotWebhookJSON, raw.types.UpdateBotWebhookJSONQuery, raw.types.UpdateChannel, raw.types.UpdateChannelAvailableMessages, raw.types.UpdateChannelMessageForwards, raw.types.UpdateChannelMessageViews, raw.types.UpdateChannelParticipant, raw.types.UpdateChannelReadMessagesContents, raw.types.UpdateChannelTooLong, raw.types.UpdateChannelUserTyping, raw.types.UpdateChannelWebPage, raw.types.UpdateChat, raw.types.UpdateChatDefaultBannedRights, raw.types.UpdateChatParticipant, raw.types.UpdateChatParticipantAdd, raw.types.UpdateChatParticipantAdmin, raw.types.UpdateChatParticipantDelete, raw.types.UpdateChatParticipants, raw.types.UpdateChatUserTyping, raw.types.UpdateConfig, raw.types.UpdateContactsReset, raw.types.UpdateDcOptions, raw.types.UpdateDeleteChannelMessages, raw.types.UpdateDeleteMessages, raw.types.UpdateDeleteScheduledMessages, raw.types.UpdateDialogFilter, raw.types.UpdateDialogFilterOrder, raw.types.UpdateDialogFilters, raw.types.UpdateDialogPinned, raw.types.UpdateDialogUnreadMark, raw.types.UpdateDraftMessage, raw.types.UpdateEditChannelMessage, raw.types.UpdateEditMessage, raw.types.UpdateEncryptedChatTyping, raw.types.UpdateEncryptedMessagesRead, raw.types.UpdateEncryption, raw.types.UpdateFavedStickers, raw.types.UpdateFolderPeers, raw.types.UpdateGeoLiveViewed, raw.types.UpdateGroupCall, raw.types.UpdateGroupCallConnection, raw.types.UpdateGroupCallParticipants, raw.types.UpdateInlineBotCallbackQuery, raw.types.UpdateLangPack, raw.types.UpdateLangPackTooLong, raw.types.UpdateLoginToken, raw.types.UpdateMessageID, raw.types.UpdateMessagePoll, raw.types.UpdateMessagePollVote, raw.types.UpdateMessageReactions, raw.types.UpdateNewChannelMessage, raw.types.UpdateNewEncryptedMessage, raw.types.UpdateNewMessage, raw.types.UpdateNewScheduledMessage, raw.types.UpdateNewStickerSet, raw.types.UpdateNotifySettings, raw.types.UpdatePeerBlocked, raw.types.UpdatePeerHistoryTTL, raw.types.UpdatePeerLocated, raw.types.UpdatePeerSettings, raw.types.UpdatePendingJoinRequests, raw.types.UpdatePhoneCall, raw.types.UpdatePhoneCallSignalingData, raw.types.UpdatePinnedChannelMessages, raw.types.UpdatePinnedDialogs, raw.types.UpdatePinnedMessages, raw.types.UpdatePrivacy, raw.types.UpdatePtsChanged, raw.types.UpdateReadChannelDiscussionInbox, raw.types.UpdateReadChannelDiscussionOutbox, raw.types.UpdateReadChannelInbox, raw.types.UpdateReadChannelOutbox, raw.types.UpdateReadFeaturedStickers, raw.types.UpdateReadHistoryInbox, raw.types.UpdateReadHistoryOutbox, raw.types.UpdateReadMessagesContents, raw.types.UpdateRecentStickers, raw.types.UpdateSavedGifs, raw.types.UpdateSavedRingtones, raw.types.UpdateServiceNotification, raw.types.UpdateStickerSets, raw.types.UpdateStickerSetsOrder, raw.types.UpdateTheme, raw.types.UpdateTranscribedAudio, raw.types.UpdateUserName, raw.types.UpdateUserPhone, raw.types.UpdateUserPhoto, raw.types.UpdateUserStatus, raw.types.UpdateUserTyping, raw.types.UpdateWebPage, raw.types.UpdateWebViewResultSent]


# noinspection PyRedeclaration
class Update:  # type: ignore
    """This base type has 101 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`UpdateAttachMenuBots <pyrosex.raw.types.UpdateAttachMenuBots>`
            - :obj:`UpdateBotCallbackQuery <pyrosex.raw.types.UpdateBotCallbackQuery>`
            - :obj:`UpdateBotChatInviteRequester <pyrosex.raw.types.UpdateBotChatInviteRequester>`
            - :obj:`UpdateBotCommands <pyrosex.raw.types.UpdateBotCommands>`
            - :obj:`UpdateBotInlineQuery <pyrosex.raw.types.UpdateBotInlineQuery>`
            - :obj:`UpdateBotInlineSend <pyrosex.raw.types.UpdateBotInlineSend>`
            - :obj:`UpdateBotMenuButton <pyrosex.raw.types.UpdateBotMenuButton>`
            - :obj:`UpdateBotPrecheckoutQuery <pyrosex.raw.types.UpdateBotPrecheckoutQuery>`
            - :obj:`UpdateBotShippingQuery <pyrosex.raw.types.UpdateBotShippingQuery>`
            - :obj:`UpdateBotStopped <pyrosex.raw.types.UpdateBotStopped>`
            - :obj:`UpdateBotWebhookJSON <pyrosex.raw.types.UpdateBotWebhookJSON>`
            - :obj:`UpdateBotWebhookJSONQuery <pyrosex.raw.types.UpdateBotWebhookJSONQuery>`
            - :obj:`UpdateChannel <pyrosex.raw.types.UpdateChannel>`
            - :obj:`UpdateChannelAvailableMessages <pyrosex.raw.types.UpdateChannelAvailableMessages>`
            - :obj:`UpdateChannelMessageForwards <pyrosex.raw.types.UpdateChannelMessageForwards>`
            - :obj:`UpdateChannelMessageViews <pyrosex.raw.types.UpdateChannelMessageViews>`
            - :obj:`UpdateChannelParticipant <pyrosex.raw.types.UpdateChannelParticipant>`
            - :obj:`UpdateChannelReadMessagesContents <pyrosex.raw.types.UpdateChannelReadMessagesContents>`
            - :obj:`UpdateChannelTooLong <pyrosex.raw.types.UpdateChannelTooLong>`
            - :obj:`UpdateChannelUserTyping <pyrosex.raw.types.UpdateChannelUserTyping>`
            - :obj:`UpdateChannelWebPage <pyrosex.raw.types.UpdateChannelWebPage>`
            - :obj:`UpdateChat <pyrosex.raw.types.UpdateChat>`
            - :obj:`UpdateChatDefaultBannedRights <pyrosex.raw.types.UpdateChatDefaultBannedRights>`
            - :obj:`UpdateChatParticipant <pyrosex.raw.types.UpdateChatParticipant>`
            - :obj:`UpdateChatParticipantAdd <pyrosex.raw.types.UpdateChatParticipantAdd>`
            - :obj:`UpdateChatParticipantAdmin <pyrosex.raw.types.UpdateChatParticipantAdmin>`
            - :obj:`UpdateChatParticipantDelete <pyrosex.raw.types.UpdateChatParticipantDelete>`
            - :obj:`UpdateChatParticipants <pyrosex.raw.types.UpdateChatParticipants>`
            - :obj:`UpdateChatUserTyping <pyrosex.raw.types.UpdateChatUserTyping>`
            - :obj:`UpdateConfig <pyrosex.raw.types.UpdateConfig>`
            - :obj:`UpdateContactsReset <pyrosex.raw.types.UpdateContactsReset>`
            - :obj:`UpdateDcOptions <pyrosex.raw.types.UpdateDcOptions>`
            - :obj:`UpdateDeleteChannelMessages <pyrosex.raw.types.UpdateDeleteChannelMessages>`
            - :obj:`UpdateDeleteMessages <pyrosex.raw.types.UpdateDeleteMessages>`
            - :obj:`UpdateDeleteScheduledMessages <pyrosex.raw.types.UpdateDeleteScheduledMessages>`
            - :obj:`UpdateDialogFilter <pyrosex.raw.types.UpdateDialogFilter>`
            - :obj:`UpdateDialogFilterOrder <pyrosex.raw.types.UpdateDialogFilterOrder>`
            - :obj:`UpdateDialogFilters <pyrosex.raw.types.UpdateDialogFilters>`
            - :obj:`UpdateDialogPinned <pyrosex.raw.types.UpdateDialogPinned>`
            - :obj:`UpdateDialogUnreadMark <pyrosex.raw.types.UpdateDialogUnreadMark>`
            - :obj:`UpdateDraftMessage <pyrosex.raw.types.UpdateDraftMessage>`
            - :obj:`UpdateEditChannelMessage <pyrosex.raw.types.UpdateEditChannelMessage>`
            - :obj:`UpdateEditMessage <pyrosex.raw.types.UpdateEditMessage>`
            - :obj:`UpdateEncryptedChatTyping <pyrosex.raw.types.UpdateEncryptedChatTyping>`
            - :obj:`UpdateEncryptedMessagesRead <pyrosex.raw.types.UpdateEncryptedMessagesRead>`
            - :obj:`UpdateEncryption <pyrosex.raw.types.UpdateEncryption>`
            - :obj:`UpdateFavedStickers <pyrosex.raw.types.UpdateFavedStickers>`
            - :obj:`UpdateFolderPeers <pyrosex.raw.types.UpdateFolderPeers>`
            - :obj:`UpdateGeoLiveViewed <pyrosex.raw.types.UpdateGeoLiveViewed>`
            - :obj:`UpdateGroupCall <pyrosex.raw.types.UpdateGroupCall>`
            - :obj:`UpdateGroupCallConnection <pyrosex.raw.types.UpdateGroupCallConnection>`
            - :obj:`UpdateGroupCallParticipants <pyrosex.raw.types.UpdateGroupCallParticipants>`
            - :obj:`UpdateInlineBotCallbackQuery <pyrosex.raw.types.UpdateInlineBotCallbackQuery>`
            - :obj:`UpdateLangPack <pyrosex.raw.types.UpdateLangPack>`
            - :obj:`UpdateLangPackTooLong <pyrosex.raw.types.UpdateLangPackTooLong>`
            - :obj:`UpdateLoginToken <pyrosex.raw.types.UpdateLoginToken>`
            - :obj:`UpdateMessageID <pyrosex.raw.types.UpdateMessageID>`
            - :obj:`UpdateMessagePoll <pyrosex.raw.types.UpdateMessagePoll>`
            - :obj:`UpdateMessagePollVote <pyrosex.raw.types.UpdateMessagePollVote>`
            - :obj:`UpdateMessageReactions <pyrosex.raw.types.UpdateMessageReactions>`
            - :obj:`UpdateNewChannelMessage <pyrosex.raw.types.UpdateNewChannelMessage>`
            - :obj:`UpdateNewEncryptedMessage <pyrosex.raw.types.UpdateNewEncryptedMessage>`
            - :obj:`UpdateNewMessage <pyrosex.raw.types.UpdateNewMessage>`
            - :obj:`UpdateNewScheduledMessage <pyrosex.raw.types.UpdateNewScheduledMessage>`
            - :obj:`UpdateNewStickerSet <pyrosex.raw.types.UpdateNewStickerSet>`
            - :obj:`UpdateNotifySettings <pyrosex.raw.types.UpdateNotifySettings>`
            - :obj:`UpdatePeerBlocked <pyrosex.raw.types.UpdatePeerBlocked>`
            - :obj:`UpdatePeerHistoryTTL <pyrosex.raw.types.UpdatePeerHistoryTTL>`
            - :obj:`UpdatePeerLocated <pyrosex.raw.types.UpdatePeerLocated>`
            - :obj:`UpdatePeerSettings <pyrosex.raw.types.UpdatePeerSettings>`
            - :obj:`UpdatePendingJoinRequests <pyrosex.raw.types.UpdatePendingJoinRequests>`
            - :obj:`UpdatePhoneCall <pyrosex.raw.types.UpdatePhoneCall>`
            - :obj:`UpdatePhoneCallSignalingData <pyrosex.raw.types.UpdatePhoneCallSignalingData>`
            - :obj:`UpdatePinnedChannelMessages <pyrosex.raw.types.UpdatePinnedChannelMessages>`
            - :obj:`UpdatePinnedDialogs <pyrosex.raw.types.UpdatePinnedDialogs>`
            - :obj:`UpdatePinnedMessages <pyrosex.raw.types.UpdatePinnedMessages>`
            - :obj:`UpdatePrivacy <pyrosex.raw.types.UpdatePrivacy>`
            - :obj:`UpdatePtsChanged <pyrosex.raw.types.UpdatePtsChanged>`
            - :obj:`UpdateReadChannelDiscussionInbox <pyrosex.raw.types.UpdateReadChannelDiscussionInbox>`
            - :obj:`UpdateReadChannelDiscussionOutbox <pyrosex.raw.types.UpdateReadChannelDiscussionOutbox>`
            - :obj:`UpdateReadChannelInbox <pyrosex.raw.types.UpdateReadChannelInbox>`
            - :obj:`UpdateReadChannelOutbox <pyrosex.raw.types.UpdateReadChannelOutbox>`
            - :obj:`UpdateReadFeaturedStickers <pyrosex.raw.types.UpdateReadFeaturedStickers>`
            - :obj:`UpdateReadHistoryInbox <pyrosex.raw.types.UpdateReadHistoryInbox>`
            - :obj:`UpdateReadHistoryOutbox <pyrosex.raw.types.UpdateReadHistoryOutbox>`
            - :obj:`UpdateReadMessagesContents <pyrosex.raw.types.UpdateReadMessagesContents>`
            - :obj:`UpdateRecentStickers <pyrosex.raw.types.UpdateRecentStickers>`
            - :obj:`UpdateSavedGifs <pyrosex.raw.types.UpdateSavedGifs>`
            - :obj:`UpdateSavedRingtones <pyrosex.raw.types.UpdateSavedRingtones>`
            - :obj:`UpdateServiceNotification <pyrosex.raw.types.UpdateServiceNotification>`
            - :obj:`UpdateStickerSets <pyrosex.raw.types.UpdateStickerSets>`
            - :obj:`UpdateStickerSetsOrder <pyrosex.raw.types.UpdateStickerSetsOrder>`
            - :obj:`UpdateTheme <pyrosex.raw.types.UpdateTheme>`
            - :obj:`UpdateTranscribedAudio <pyrosex.raw.types.UpdateTranscribedAudio>`
            - :obj:`UpdateUserName <pyrosex.raw.types.UpdateUserName>`
            - :obj:`UpdateUserPhone <pyrosex.raw.types.UpdateUserPhone>`
            - :obj:`UpdateUserPhoto <pyrosex.raw.types.UpdateUserPhoto>`
            - :obj:`UpdateUserStatus <pyrosex.raw.types.UpdateUserStatus>`
            - :obj:`UpdateUserTyping <pyrosex.raw.types.UpdateUserTyping>`
            - :obj:`UpdateWebPage <pyrosex.raw.types.UpdateWebPage>`
            - :obj:`UpdateWebViewResultSent <pyrosex.raw.types.UpdateWebViewResultSent>`
    """

    QUALNAME = "pyrosex.raw.base.Update"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/update")
