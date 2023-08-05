import os

import pandas as pd
import pytest

from ghs import GHS


@pytest.fixture
async def ghs() -> GHS:
    return GHS(os.environ["GITHUB_REPOSITORY"])


def test_create(ghs: GHS, df: pd.DataFrame) -> None:
    ghs.create("b.csv", df)


def test_get(ghs: GHS, df: pd.DataFrame) -> None:
    rv = ghs.get("b.csv")
    assert rv.equals(df.reset_index())


async def test_update(ghs: GHS, df: pd.DataFrame) -> None:
    ghs.update("b.csv", df)


def test_delete(ghs: GHS) -> None:
    ghs.delete("b.csv")


async def test_objects(ghs: GHS) -> None:
    rv = ghs.objects()
    assert rv
