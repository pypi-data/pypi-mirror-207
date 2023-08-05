import os

import pandas as pd
import pytest

from ghs import AsyncGHS


@pytest.fixture
async def ghs() -> AsyncGHS:
    async with AsyncGHS(os.environ["GITHUB_REPOSITORY"]) as ghs:
        yield ghs


async def test_create(ghs: AsyncGHS, df: pd.DataFrame) -> None:
    await ghs.create("a.csv", df)


async def test_get(ghs: AsyncGHS, df: pd.DataFrame) -> None:
    rv = await ghs.get("a.csv")
    assert rv.equals(df)


async def test_update(ghs: AsyncGHS, df: pd.DataFrame) -> None:
    await ghs.update("a.csv", df)


async def test_delete(ghs: AsyncGHS) -> None:
    await ghs.delete("a.csv")


async def test_objects(ghs: AsyncGHS) -> None:
    rv = await ghs.objects()
    assert rv
