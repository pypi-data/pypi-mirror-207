from typing import List

from ..messages_and_media import MessageEntity
from ..object import Object


class InputMedia(Object):
    """Content of a media message to be sent.

    It should be one of:

    - :obj:`~pyrosex.types.InputMediaAnimation`
    - :obj:`~pyrosex.types.InputMediaDocument`
    - :obj:`~pyrosex.types.InputMediaAudio`
    - :obj:`~pyrosex.types.InputMediaPhoto`
    - :obj:`~pyrosex.types.InputMediaVideo`
    """

    def __init__(
        self,
        media: str,
        caption: str = "",
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None
    ):
        super().__init__()

        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
