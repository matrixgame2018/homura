import pytest
import torch

from homura.utils.containers import Map, TensorTuple


def test_map():
    map = Map(a=1, b=2)
    map["c"] = 3
    for k, v in map.items():
        assert map[k] == getattr(map, k)

    for k in ["update", "key", "items", "value", "clear", "copy", "get", "pop"]:
        with pytest.raises(KeyError):
            setattr(map, k, 1)


def test_tensortuple():
    a = torch.randn(3, 3), torch.randn(3, 3)
    t = TensorTuple(a)
    assert t[0].dtype == torch.float32

    assert t.to(torch.int32)[0].dtype == torch.int32
