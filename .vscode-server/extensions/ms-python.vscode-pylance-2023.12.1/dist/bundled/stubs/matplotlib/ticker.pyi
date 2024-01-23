from .scale import SymmetricalLogTransform
from typing import Any, Callable, Literal, Sequence
from ._typing import *
from .axis import Axis
from functools import partial

__all__ = (
    "TickHelper",
    "Formatter",
    "FixedFormatter",
    "NullFormatter",
    "FuncFormatter",
    "FormatStrFormatter",
    "StrMethodFormatter",
    "ScalarFormatter",
    "LogFormatter",
    "LogFormatterExponent",
    "LogFormatterMathtext",
    "LogFormatterSciNotation",
    "LogitFormatter",
    "EngFormatter",
    "PercentFormatter",
    "Locator",
    "IndexLocator",
    "FixedLocator",
    "NullLocator",
    "LinearLocator",
    "LogLocator",
    "AutoLocator",
    "MultipleLocator",
    "MaxNLocator",
    "AutoMinorLocator",
    "SymmetricalLogLocator",
    "AsinhLocator",
    "LogitLocator",
)

class _DummyAxis:

    dataLim = ...
    viewLim = ...
    def __init__(self, minpos: int = ...) -> None: ...
    def get_view_interval(self): ...
    def set_view_interval(self, vmin: float, vmax: float): ...
    def get_minpos(self): ...
    def get_data_interval(self): ...
    def set_data_interval(self, vmin: float, vmax: float): ...
    def get_tick_space(self): ...

class TickHelper:
    axis = ...
    def set_axis(self, axis: Axis) -> None: ...
    def create_dummy_axis(self, **kwargs) -> None: ...
    def set_view_interval(self, vmin: float, vmax: float): ...
    def set_data_interval(self, vmin: float, vmax: float): ...
    def set_bounds(self, vmin: float, vmax: float): ...

class Formatter(TickHelper):

    locs = ...
    def __call__(self, x, pos=...): ...
    def format_ticks(self, values: Sequence[float]) -> list[str]: ...
    def format_data(self, value) -> str: ...
    def format_data_short(self, value) -> str: ...
    def get_offset(self) -> str: ...
    def set_locs(self, locs: ArrayLike) -> None: ...
    @staticmethod
    def fix_minus(s: str) -> str: ...

class NullFormatter(Formatter):
    def __call__(self, x: float, pos: int = ...): ...

class FixedFormatter(Formatter):
    def __init__(self, seq: Sequence[str]) -> None: ...
    def __call__(self, x: float, pos: int = ...): ...
    def get_offset(self) -> str: ...
    def set_offset_string(self, ofs: str): ...

class FuncFormatter(Formatter):
    def __init__(self, func: Callable | partial) -> None: ...
    def __call__(self, x: float, pos: int = ...): ...
    def get_offset(self) -> str: ...
    def set_offset_string(self, ofs: str): ...

class FormatStrFormatter(Formatter):
    def __init__(self, fmt: str) -> None: ...
    def __call__(self, x: float, pos: int = ...): ...

class StrMethodFormatter(Formatter):
    def __init__(self, fmt: str) -> None: ...
    def __call__(self, x: float, pos: int = ...): ...

class ScalarFormatter(Formatter):
    def __init__(
        self,
        useOffset: bool | float = ...,
        useMathText: bool | None = ...,
        useLocale: bool | None = ...,
    ) -> None: ...
    def get_useOffset(self): ...
    def set_useOffset(self, val: bool | float) -> None: ...
    useOffset = ...
    def get_useLocale(self) -> bool | None: ...
    def set_useLocale(self, val: bool | None): ...
    useLocale = ...
    def get_useMathText(self) -> bool | None: ...
    def set_useMathText(self, val: bool | None) -> None: ...
    useMathText = ...
    def __call__(self, x: float, pos: int = ...) -> str: ...
    def set_scientific(self, bool) -> None: ...
    def set_powerlimits(self, lims: Sequence[int]): ...
    def format_data_short(self, value) -> str: ...
    def format_data(self, value) -> str: ...
    def get_offset(self) -> str: ...
    def set_locs(self, locs: Sequence[float]) -> None: ...

class LogFormatter(Formatter):
    def __init__(
        self,
        base: Sequence[float] = ...,
        labelOnlyBase: bool = False,
        minor_thresholds: Sequence[float] = ...,
        linthresh: None | float = None,
    ) -> None: ...
    def base(self, base): ...
    def label_minor(self, labelOnlyBase: bool): ...
    def set_locs(self, locs=...): ...
    def __call__(self, x: float, pos: int = ...): ...
    def format_data(self, value) -> str: ...
    def format_data_short(self, value) -> str: ...

class LogFormatterExponent(LogFormatter): ...

class LogFormatterMathtext(LogFormatter):
    def __call__(self, x: float, pos: int = ...): ...

class LogFormatterSciNotation(LogFormatterMathtext): ...

class LogitFormatter(Formatter):
    def __init__(
        self,
        *,
        use_overline: bool = False,
        one_half: str = "\\frac{1}{2}",
        minor: bool = False,
        minor_threshold: int = 25,
        minor_number: int = 6
    ) -> None: ...
    def use_overline(self, use_overline: bool = False): ...
    def set_one_half(self, one_half: str = "\\frac{1}{2}"): ...
    def set_minor_threshold(self, minor_threshold: int): ...
    def set_minor_number(self, minor_number: int): ...
    def set_locs(self, locs): ...
    def __call__(self, x: float, pos: int = ...): ...
    def format_data_short(self, value) -> str: ...

class EngFormatter(Formatter):

    ENG_PREFIXES = ...
    def __init__(
        self,
        unit: str = "",
        places: int | None = None,
        sep: str = " ",
        *,
        usetex: bool = ...,
        useMathText: bool = ...
    ) -> None: ...
    def get_usetex(self) -> bool: ...
    def set_usetex(self, val: bool) -> None: ...

    usetex = ...
    def get_useMathText(self) -> bool: ...
    def set_useMathText(self, val: bool) -> None: ...

    useMathText = ...
    def __call__(self, x: float, pos: int = ...): ...
    def format_eng(self, num) -> str: ...

class PercentFormatter(Formatter):
    def __init__(
        self,
        xmax: float = ...,
        decimals: None | int = ...,
        symbol: str | None = ...,
        is_latex: bool = ...,
    ) -> None: ...
    def __call__(self, x: float, pos: int = ...): ...
    def format_pct(self, x, display_range) -> str: ...
    def convert_to_pct(self, x): ...
    @property
    def symbol(self) -> str: ...
    @symbol.setter
    def symbol(self, symbol: str): ...

class Locator(TickHelper):

    MAXTICKS = ...
    def tick_values(self, vmin: float, vmax: float): ...
    def set_params(self, **kwargs): ...
    def __call__(self): ...
    def raise_if_exceeds(self, locs): ...
    def nonsingular(self, v0: float, v1: float) -> tuple[float, float]: ...
    def view_limits(self, vmin: float, vmax: float): ...

class IndexLocator(Locator):
    def __init__(self, base: float, offset: float) -> None: ...
    def set_params(self, base: float = ..., offset: float = ...): ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...

class FixedLocator(Locator):
    def __init__(self, locs, nbins: int | None = ...) -> None: ...
    def set_params(self, nbins: int | None = ...): ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...

class NullLocator(Locator):
    def __call__(self) -> list: ...
    def tick_values(self, vmin: float, vmax: float) -> list: ...

class LinearLocator(Locator):
    def __init__(self, numticks: int = ..., presets: dict = ...) -> None: ...
    @property
    def numticks(self): ...
    @numticks.setter
    def numticks(self, numticks: int): ...
    def set_params(self, numticks: int = ..., presets: dict = ...): ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, vmin: float, vmax: float): ...

class MultipleLocator(Locator):
    def __init__(self, base: float = ...) -> None: ...
    def set_params(self, base: float): ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, dmin: float, dmax: float): ...

def scale_range(
    vmin: float, vmax: float, n: int = ..., threshold: int = ...
) -> tuple[float, int]: ...

class _Edge_integer:
    def __init__(self, step: float, offset: float) -> None: ...
    def closeto(self, ms, edge): ...
    def le(self, x: float) -> float: ...
    def ge(self, x: float) -> float: ...

class MaxNLocator(Locator):

    default_params = ...
    def __init__(self, nbins: int | Literal["auto"] = 10, **kwargs) -> None: ...
    def set_params(self, **kwargs) -> None: ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, dmin: float, dmax: float) -> tuple[float, float]: ...

def is_decade(x, base=..., *, rtol=...): ...
def is_close_to_int(x, *, atol=...): ...

class LogLocator(Locator):
    def __init__(
        self,
        base: float = ...,
        subs: None | str | Sequence[float] = ...,
        numdecs: int = ...,
        numticks: None | int = ...,
    ) -> None: ...
    def set_params(
        self,
        base: float = ...,
        subs: None | str | Sequence[float] = ...,
        numdecs: int = ...,
        numtick: None | int = ...,
    ): ...
    def base(self, base: float) -> None: ...
    def subs(self, subs: None | str | Sequence[float]) -> None: ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, vmin: float, vmax: float): ...
    def nonsingular(self, vmin: float, vmax: float) -> tuple[float, float]: ...

class SymmetricalLogLocator(Locator):
    def __init__(
        self,
        transform: SymmetricalLogTransform = ...,
        subs: Sequence[float] = ...,
        linthresh: float = ...,
        base: float = ...,
    ) -> None: ...
    def set_params(self, subs: Sequence[float] = ..., numticks: int | None = ...): ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, vmin: float, vmax: float): ...

class AsinhLocator(Locator):
    def __init__(
        self,
        linear_width: float,
        numticks: int = 11,
        symthresh: float = 0.2,
        base: int = 10,
        subs: Sequence[int] = ...,
    ) -> None: ...
    def set_params(
        self,
        numticks: int = ...,
        symthresh: float = ...,
        base: int = ...,
        subs: Sequence[int] = ...,
    ): ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...

class LogitLocator(MaxNLocator):
    def __init__(
        self, minor: bool = ..., *, nbins: int | Literal["auto"] = ...
    ) -> None: ...
    def set_params(self, minor: None = ..., **kwargs) -> None: ...
    @property
    def minor(self): ...
    @minor.setter
    def minor(self, value): ...
    def tick_values(self, vmin: float, vmax: float): ...
    def nonsingular(self, vmin: float, vmax: float) -> tuple[float, float]: ...

class AutoLocator(MaxNLocator):
    def __init__(self) -> None: ...

class AutoMinorLocator(Locator):
    def __init__(self, n: int | None = ...) -> None: ...
    def __call__(self) -> list: ...
    def tick_values(self, vmin: float, vmax: float): ...
