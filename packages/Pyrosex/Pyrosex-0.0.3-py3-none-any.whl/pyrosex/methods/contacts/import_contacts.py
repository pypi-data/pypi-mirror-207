from typing import List

import pyrosex
from pyrosex import raw
from pyrosex import types


class ImportContacts:
    async def import_contacts(
        self: "pyrosex.Client",
        contacts: List["types.InputPhoneContact"]
    ):
        """Import contacts to your Telegram address book.

        Parameters:
            contacts (List of :obj:`~pyrosex.types.InputPhoneContact`):
                The contact list to be added

        Returns:
            :obj:`types.contacts.ImportedContacts`

        Example:
            .. code-block:: python

                from pyrosex.types import InputPhoneContact

                await app.import_contacts([
                    InputPhoneContact("+1-123-456-7890", "Foo"),
                    InputPhoneContact("+1-456-789-0123", "Bar"),
                    InputPhoneContact("+1-789-012-3456", "Baz")])
        """
        imported_contacts = await self.invoke(
            raw.functions.contacts.ImportContacts(
                contacts=contacts
            )
        )

        return imported_contacts
