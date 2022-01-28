from typing import Any, Dict, Final, final


class Fields:

    # cls attributes
    BASE_HEADER_TPL: Final[str]
    EXTENSIONS_TPL: Final[str]

    # instance attributes
    mandatory: Dict
    extensions: Dict
    custom: Dict

    _syslog_flag: bool

    @final
    def __init__(self, syslog_flag: bool = ..., **fields: Any) -> None: ...

    @final
    @property
    def all(self) -> Dict: ...

    def render(self) -> str: ...

    @final
    def validate(self) -> None: ...

    def render_syslog_header(self) -> str: ...
    def render_base_header(self) -> str: ...
    def render_extensions(self) -> str: ...

    @final
    def _escape_base_fields(self, **fields: Any) -> Dict: ...
    @final
    def _escape_extensions_fields(self, **fields: Any) -> Dict: ...

    @final
    def _replace_none_with_empty(self, **fields: Any) -> Dict: ...
    @final
    def _calculate_dynamic_fields(self, **fields: Any) -> Dict: ...
