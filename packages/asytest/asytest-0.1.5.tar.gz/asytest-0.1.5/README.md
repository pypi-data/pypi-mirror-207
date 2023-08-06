# test execution framework for async test

# how it workks

All tests functions must begin with 'test_' prefix.
Framework executes all test functions in one asyncio event_loop cuncurrently, which means that your tests should be independent with share-nothing design.

# running example tests

    pip install asytest
    python -m asytest tests