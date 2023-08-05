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

SendMessageAction = Union[raw.types.SendMessageCancelAction, raw.types.SendMessageChooseContactAction, raw.types.SendMessageChooseStickerAction, raw.types.SendMessageEmojiInteraction, raw.types.SendMessageEmojiInteractionSeen, raw.types.SendMessageGamePlayAction, raw.types.SendMessageGeoLocationAction, raw.types.SendMessageHistoryImportAction, raw.types.SendMessageRecordAudioAction, raw.types.SendMessageRecordRoundAction, raw.types.SendMessageRecordVideoAction, raw.types.SendMessageTypingAction, raw.types.SendMessageUploadAudioAction, raw.types.SendMessageUploadDocumentAction, raw.types.SendMessageUploadPhotoAction, raw.types.SendMessageUploadRoundAction, raw.types.SendMessageUploadVideoAction, raw.types.SpeakingInGroupCallAction]


# noinspection PyRedeclaration
class SendMessageAction:  # type: ignore
    """This base type has 18 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`SendMessageCancelAction <pyrosex.raw.types.SendMessageCancelAction>`
            - :obj:`SendMessageChooseContactAction <pyrosex.raw.types.SendMessageChooseContactAction>`
            - :obj:`SendMessageChooseStickerAction <pyrosex.raw.types.SendMessageChooseStickerAction>`
            - :obj:`SendMessageEmojiInteraction <pyrosex.raw.types.SendMessageEmojiInteraction>`
            - :obj:`SendMessageEmojiInteractionSeen <pyrosex.raw.types.SendMessageEmojiInteractionSeen>`
            - :obj:`SendMessageGamePlayAction <pyrosex.raw.types.SendMessageGamePlayAction>`
            - :obj:`SendMessageGeoLocationAction <pyrosex.raw.types.SendMessageGeoLocationAction>`
            - :obj:`SendMessageHistoryImportAction <pyrosex.raw.types.SendMessageHistoryImportAction>`
            - :obj:`SendMessageRecordAudioAction <pyrosex.raw.types.SendMessageRecordAudioAction>`
            - :obj:`SendMessageRecordRoundAction <pyrosex.raw.types.SendMessageRecordRoundAction>`
            - :obj:`SendMessageRecordVideoAction <pyrosex.raw.types.SendMessageRecordVideoAction>`
            - :obj:`SendMessageTypingAction <pyrosex.raw.types.SendMessageTypingAction>`
            - :obj:`SendMessageUploadAudioAction <pyrosex.raw.types.SendMessageUploadAudioAction>`
            - :obj:`SendMessageUploadDocumentAction <pyrosex.raw.types.SendMessageUploadDocumentAction>`
            - :obj:`SendMessageUploadPhotoAction <pyrosex.raw.types.SendMessageUploadPhotoAction>`
            - :obj:`SendMessageUploadRoundAction <pyrosex.raw.types.SendMessageUploadRoundAction>`
            - :obj:`SendMessageUploadVideoAction <pyrosex.raw.types.SendMessageUploadVideoAction>`
            - :obj:`SpeakingInGroupCallAction <pyrosex.raw.types.SpeakingInGroupCallAction>`
    """

    QUALNAME = "pyrosex.raw.base.SendMessageAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/send-message-action")
