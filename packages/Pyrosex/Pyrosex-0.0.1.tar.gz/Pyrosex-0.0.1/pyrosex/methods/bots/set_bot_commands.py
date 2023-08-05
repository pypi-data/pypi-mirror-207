from typing import List

import pyrosex
from pyrosex import raw
from pyrosex import types


class SetBotCommands:
    async def set_bot_commands(
        self: "pyrosex.Client",
        commands: List["types.BotCommand"],
        scope: "types.BotCommandScope" = types.BotCommandScopeDefault(),
        language_code: str = "",
    ) -> bool:
        """Set the list of the bot's commands.
        The commands passed will overwrite any command set previously.
        This method can be used by the own bot only.

        Parameters:
            commands (List of :obj:`~pyrosex.types.BotCommand`):
                A list of bot commands.
                At most 100 commands can be specified.

            scope (:obj:`~pyrosex.types.BotCommandScope`, *optional*):
                An object describing the scope of users for which the commands are relevant.
                Defaults to :obj:`~pyrosex.types.BotCommandScopeDefault`.

            language_code (``str``, *optional*):
                A two-letter ISO 639-1 language code.
                If empty, commands will be applied to all users from the given scope, for whose language there are no
                dedicated commands.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                from pyrosex.types import BotCommand

                # Set new commands
                await app.set_bot_commands([
                    BotCommand("start", "Start the bot"),
                    BotCommand("settings", "Bot settings")])
        """

        return await self.invoke(
            raw.functions.bots.SetBotCommands(
                commands=[c.write() for c in commands],
                scope=await scope.write(self),
                lang_code=language_code,
            )
        )
