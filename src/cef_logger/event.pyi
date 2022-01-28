from logging import Handler
from typing import Any, Dict, Tuple, Union, final

from .fields import Fields


class Event:
    # Mandatory fields
    Version: int
    DeviceVendor: str
    DeviceProduct: str
    DeviceVersion: str
    DeviceEventClassID: Union[int, str]
    Name: str
    Severity: Union[int, str]

    # Extensions fields
    act: str
    app: str

    c6a1: str
    c6a1Label: str
    c6a2: str
    c6a2Label: str
    c6a3: str
    c6a3Label: str
    c6a4: str
    c6a4Label: str

    cfp1: float
    cfp1Label: str
    cfp2: float
    cfp2Label: str
    cfp3: float
    cfp3Label: str
    cfp4: float
    cfp4Label: str

    cn1: int
    cn1Label: str
    cn2: int
    cn2Label: str
    cn3: int
    cn3Label: str

    cnt: int

    cs1: str
    cs1Label: str
    cs2: str
    cs2Label: str
    cs3: str
    cs3Label: str
    cs4: str
    cs4Label: str
    cs5: str
    cs5Label: str
    cs6: str
    cs6Label: str

    destinationDnsDomain: str
    destinationServiceName: str
    destinationTranslatedAddress: str
    destinationTranslatedPort: int

    deviceCustomDate1: Union[int, float, str]
    deviceCustomDate1Label: str
    deviceCustomDate2: Union[int, float, str]
    deviceCustomDate2Label: str

    deviceDirection: int
    deviceDnsDomain: str
    deviceExternalId: str
    deviceFacility: str
    deviceInboundInterface: str
    deviceNtDomain: str
    deviceOutboundInterface: str
    devicePayloadId: str
    deviceProcessName: str
    deviceTranslatedAddress: str

    dhost: str
    dmac: str
    dntdom: str
    dpid: int
    dpriv: int
    dproc: str
    dpt: int
    dst: str
    dtz: str
    duid: str
    duser: str
    dvc: str
    dvchost: str
    dvcmac: str
    dvcpid: int
    end: Union[int, float, str]
    externalId: str

    fileCreateTime: Union[int, float, str]
    fileHash: str
    fileId: str
    fileModificationTime: Union[int, float, str]
    filePath: str
    filePermission: str
    fileType: str

    flexDate1: Union[int, float, str]
    flexDate1Label: str
    flexString1: str
    flexString1Label: str
    flexString2: str
    flexString2Label: str

    fname: str
    fsize: int
    in_: int
    msg: str

    oldFileCreateTime: Union[int, float, str]
    oldFileHash: str
    oldFileId: str
    oldFileModificationTime: Union[int, float, str]
    oldFileName: str
    oldFilePath: str
    oldFilePermission: str
    oldFileSize: int
    oldFileType: str

    out: int
    outcome: str
    proto: str
    reason: str
    request: str
    requestClientApplication: str
    requestContext: str
    requestCookies: str
    requestMethod: str
    rt: Union[int, float, str]

    shost: str
    smac: str
    sntdom: str
    sourceDnsDomain: str
    sourceServiceName: str
    sourceTranslatedAddress: str
    sourceTranslatedPort: int

    spid: int
    spriv: str
    sproc: str
    spt: int
    src: str
    start: Union[int, float, str]
    suid: str
    suser: str
    type: int

    # non field cls attributes
    __fields__: Dict
    SYSLOG_HEADER: bool
    EMITTERS: Tuple[Handler]

    # instance attributes
    fields: Fields

    @final
    def __init__(self) -> None: ...

    @final
    def __call__(self, **fields: Any) -> None: ...

    def __repr__(self) -> str: ...

    @final
    def emit(self, record: str) -> None: ...
