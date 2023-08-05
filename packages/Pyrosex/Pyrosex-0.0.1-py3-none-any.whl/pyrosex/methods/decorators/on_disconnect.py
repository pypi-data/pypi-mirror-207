from typing import Callable

import pyrosex


class OnDisconnect:
    def on_disconnect(self=None) -> Callable:
        """Decorator for handling disconnections.

        This does the same thing as :meth:`~pyrosex.Client.add_handler` using the
        :obj:`~pyrosex.handlers.DisconnectHandler`.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrosex.Client):
                self.add_handler(pyrosex.handlers.DisconnectHandler(func))

            return func

        return decorator
