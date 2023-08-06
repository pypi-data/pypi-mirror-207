from src.asytest import asytest

def test_runs_succesfully_for_file():
    test_result: asytest.TestSuiteResult = asytest.run_tests("example_tests/test_dummy.py", 10)
    assert len(test_result.test_results) == 4

def test_runs_succesfully_for_folder():
    test_result: asytest.TestSuiteResult = asytest.run_tests("example_tests/", 10)
    assert len(test_result.test_results) == 12

def test_runs_all_tests_parrallel():
    test_result: asytest.TestSuiteResult = asytest.run_tests("example_tests/test_dummy.py", 10)
    assert_approx_equal(test_result.exec_time, 1.0, tolerance=0.1)

def test_create_correct_test_suite_report():
    test_result: asytest.TestSuiteResult = asytest.run_tests("example_tests/test_dummy.py", 10)

    assert test_result.count_num_failed() == 2
    assert test_result.count_num_passed() == 2
    assert_approx_equal(test_result.exec_time, 1.0, tolerance=0.1)

    test_dic = {t.name: t for t in test_result.test_results}
    assert test_dic['test_that_succeeds'].status == asytest.TestStatus.SUCCESS
    assert test_dic['test_with_a_very_long_name_that_succeeds'].status == asytest.TestStatus.SUCCESS
    assert test_dic['test_that_fails_with_assert'].status == asytest.TestStatus.FAILED
    assert test_dic['test_that_fails_with_error'].status == asytest.TestStatus.ERROR

def test_limit_number_of_concurrent_tests():
    test_result: asytest.TestSuiteResult = asytest.run_tests("example_tests/test_concurrent.py", 2)
    assert len(test_result.test_results) == 8
    assert test_result.count_num_failed() == 0
    assert test_result.count_num_passed() == 8
    assert test_result.exec_time > 4 and test_result.exec_time < 5

def assert_approx_equal(actual: float, expected: float, tolerance: float = 0.001):
    assert abs(actual - expected) < tolerance, f"{actual} not approximately equal {expected}"