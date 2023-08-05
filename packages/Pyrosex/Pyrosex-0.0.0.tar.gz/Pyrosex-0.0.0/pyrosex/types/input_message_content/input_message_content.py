import pyrosex

from ..object import Object

"""- :obj:`~pyrosex.types.InputLocationMessageContent`
    - :obj:`~pyrosex.types.InputVenueMessageContent`
    - :obj:`~pyrosex.types.InputContactMessageContent`"""


class InputMessageContent(Object):
    """Content of a message to be sent as a result of an inline query.

    pyrosex currently supports the following types:

    - :obj:`~pyrosex.types.InputTextMessageContent`
    """

    def __init__(self):
        super().__init__()

    async def write(self, client: "pyrosex.Client", reply_markup):
        raise NotImplementedError
