from typing import Callable

import pyrosex
from pyrosex.filters import Filter


class OnDeletedMessages:
    def on_deleted_messages(
        self=None,
        filters=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling deleted messages.

        This does the same thing as :meth:`~pyrosex.Client.add_handler` using the
        :obj:`~pyrosex.handlers.DeletedMessagesHandler`.

        Parameters:
            filters (:obj:`~pyrosex.filters`, *optional*):
                Pass one or more filters to allow only a subset of messages to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrosex.Client):
                self.add_handler(pyrosex.handlers.DeletedMessagesHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrosex.handlers.DeletedMessagesHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator
