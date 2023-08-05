import logging
from typing import List

import pyrosex
from pyrosex import raw
from pyrosex import types

log = logging.getLogger(__name__)


class GetContacts:
    async def get_contacts(
        self: "pyrosex.Client"
    ) -> List["types.User"]:
        """Get contacts from your Telegram address book.

        Returns:
            List of :obj:`~pyrosex.types.User`: On success, a list of users is returned.

        Example:
            .. code-block:: python

                contacts = await app.get_contacts()
                print(contacts)
        """
        contacts = await self.invoke(raw.functions.contacts.GetContacts(hash=0))
        return types.List(types.User._parse(self, user) for user in contacts.users)
