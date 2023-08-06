import asyncio

async def util_function():
    print("util")

async def test_that_succeeds():
    await asyncio.sleep(1)

async def test_with_a_very_long_name_that_succeeds():
    await asyncio.sleep(1)

async def test_that_fails_with_assert():
    await asyncio.sleep(1)
    assert False

async def test_that_fails_with_error():
    await asyncio.sleep(1)
    x = []
    print(x.length)
