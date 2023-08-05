from typing import Union

import pyrosex
from pyrosex import raw
from pyrosex import types


class GetChatInviteLink:
    async def get_chat_invite_link(
        self: "pyrosex.Client",
        chat_id: Union[int, str],
        invite_link: str,
    ) -> "types.ChatInviteLink":
        """Get detailed information about a chat invite link.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            invite_link (str):
                The invite link.

        Returns:
            :obj:`~pyrosex.types.ChatInviteLink`: On success, the invite link is returned.
        """
        r = await self.invoke(
            raw.functions.messages.GetExportedChatInvite(
                peer=await self.resolve_peer(chat_id),
                link=invite_link
            )
        )

        users = {i.id: i for i in r.users}

        return types.ChatInviteLink._parse(self, r.invite, users)
