from uuid import uuid4

import pyrosex
from pyrosex import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~pyrosex.types.InlineQueryResultCachedAudio`
    - :obj:`~pyrosex.types.InlineQueryResultCachedDocument`
    - :obj:`~pyrosex.types.InlineQueryResultCachedAnimation`
    - :obj:`~pyrosex.types.InlineQueryResultCachedPhoto`
    - :obj:`~pyrosex.types.InlineQueryResultCachedSticker`
    - :obj:`~pyrosex.types.InlineQueryResultCachedVideo`
    - :obj:`~pyrosex.types.InlineQueryResultCachedVoice`
    - :obj:`~pyrosex.types.InlineQueryResultArticle`
    - :obj:`~pyrosex.types.InlineQueryResultAudio`
    - :obj:`~pyrosex.types.InlineQueryResultContact`
    - :obj:`~pyrosex.types.InlineQueryResultDocument`
    - :obj:`~pyrosex.types.InlineQueryResultAnimation`
    - :obj:`~pyrosex.types.InlineQueryResultLocation`
    - :obj:`~pyrosex.types.InlineQueryResultPhoto`
    - :obj:`~pyrosex.types.InlineQueryResultVenue`
    - :obj:`~pyrosex.types.InlineQueryResultVideo`
    - :obj:`~pyrosex.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "pyrosex.Client"):
        pass
