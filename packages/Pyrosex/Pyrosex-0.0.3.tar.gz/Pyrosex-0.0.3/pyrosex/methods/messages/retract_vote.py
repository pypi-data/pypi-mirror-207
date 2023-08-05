from typing import Union

import pyrosex
from pyrosex import raw
from pyrosex import types


class RetractVote:
    async def retract_vote(
        self: "pyrosex.Client",
        chat_id: Union[int, str],
        message_id: int
    ) -> "types.Poll":
        """Retract your vote in a poll.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                Identifier of the original message with the poll.

        Returns:
            :obj:`~pyrosex.types.Poll`: On success, the poll with the retracted vote is returned.

        Example:
            .. code-block:: python

                await app.retract_vote(chat_id, message_id)
        """
        r = await self.invoke(
            raw.functions.messages.SendVote(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                options=[]
            )
        )

        return types.Poll._parse(self, r.updates[0])
