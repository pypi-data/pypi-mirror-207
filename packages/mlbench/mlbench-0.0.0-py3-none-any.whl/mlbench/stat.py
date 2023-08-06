from dataclasses import dataclass
import typing as t


@dataclass(frozen=True, eq=True)
class Sig:
    value: t.Union[float, t.Tuple[float, ...]]
    baseline: float

    @property
    def values(self) -> t.Tuple[float, ...]:
        pass

    @property
    def is_stat_sig(self) -> bool:
        pass

    @property
    def mean(self) -> bool:
        pass

    @property
    def confidence_interval(self) -> ...:
        pass
