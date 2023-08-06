from dataclasses import dataclass
from sklearn.metrics import accuracy_score
import typing as t

from .stat import Sig


@dataclass(frozen=True, eq=True)
class Metric:
    value: t.Union[float, t.Tuple[float, ...]]
    baseline: float
    min_dataset: float
    min_possible: float
    max_possible: float

    def __post_init__(self):
        # TODO: support lower-is-better metrics
        assert (
            self.min_possible <= self.min_dataset <= self.baseline <= self.max_possible
        )
        for val in self.values:
            assert self.__in_range(val=val)

    def __in_range(self, val: float) -> bool:
        return self.min_dataset <= val <= self.max_possible

    @property
    def stat_sig(self) -> Sig:
        # TODO: stat sig better than bl?
        raise NotImplementedError

    @property
    def values(self) -> t.Sequence[float]:
        return (self.value,) if isinstance(self.value, float) else self.value


@dataclass(frozen=True, eq=True)
class AccuracyBinary(Metric):
    min_possible: float = 0
    max_possible: float = 1
    min_dataset: float = 0

    @classmethod
    def from_dataset(
        cls,
        y_true: t.Sequence[bool],
        y_pred: t.Union[
            t.Sequence[bool],
            t.Sequence[t.Sequence[bool]],
        ],
    ) -> "Accuracy":
        n = len(y_true)
        assert n > 0
        p = sum(y_true)
        # TODO: check
        value = (
            cls.__accuracy(y_true=y_true, y_pred=y_pred)
            if isinstance(y_pred[0], bool)
            else tuple(
                cls.__accuracy(
                    y_true=y_true,
                    y_pred=yp,
                )
                for yp in y_pred
            )
        )
        return cls(value=value, baseline=p / n)

    @staticmethod
    def __accuracy(y_true: t.Sequence[bool], y_pred: t.Sequence[bool]) -> float:
        return accuracy_score(
            y_true=y_true,
            y_pred=y_pred,
        )
