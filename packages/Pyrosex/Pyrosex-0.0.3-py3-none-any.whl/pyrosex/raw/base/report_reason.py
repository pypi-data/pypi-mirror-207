#  Pyrosex - Telegram MTProto API Client Library for Python
#  Copyright (C) 2023-present OTH <https://github.com/OTHFamily>
#
#  This file is part of Pyrosex.
#
#  Pyrosex is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrosex is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrosex.  If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrosex import raw
from pyrosex.raw.core import TLObject

ReportReason = Union[raw.types.InputReportReasonChildAbuse, raw.types.InputReportReasonCopyright, raw.types.InputReportReasonFake, raw.types.InputReportReasonGeoIrrelevant, raw.types.InputReportReasonIllegalDrugs, raw.types.InputReportReasonOther, raw.types.InputReportReasonPersonalDetails, raw.types.InputReportReasonPornography, raw.types.InputReportReasonSpam, raw.types.InputReportReasonViolence]


# noinspection PyRedeclaration
class ReportReason:  # type: ignore
    """This base type has 10 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`InputReportReasonChildAbuse <pyrosex.raw.types.InputReportReasonChildAbuse>`
            - :obj:`InputReportReasonCopyright <pyrosex.raw.types.InputReportReasonCopyright>`
            - :obj:`InputReportReasonFake <pyrosex.raw.types.InputReportReasonFake>`
            - :obj:`InputReportReasonGeoIrrelevant <pyrosex.raw.types.InputReportReasonGeoIrrelevant>`
            - :obj:`InputReportReasonIllegalDrugs <pyrosex.raw.types.InputReportReasonIllegalDrugs>`
            - :obj:`InputReportReasonOther <pyrosex.raw.types.InputReportReasonOther>`
            - :obj:`InputReportReasonPersonalDetails <pyrosex.raw.types.InputReportReasonPersonalDetails>`
            - :obj:`InputReportReasonPornography <pyrosex.raw.types.InputReportReasonPornography>`
            - :obj:`InputReportReasonSpam <pyrosex.raw.types.InputReportReasonSpam>`
            - :obj:`InputReportReasonViolence <pyrosex.raw.types.InputReportReasonViolence>`
    """

    QUALNAME = "pyrosex.raw.base.ReportReason"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrosex.org/telegram/base/report-reason")
