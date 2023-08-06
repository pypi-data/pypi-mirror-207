from .asytest import parse_args, run_tests


if __name__ == "__main__":
    args = parse_args()
    test_suite_result = run_tests(args.resource, args.max_concurrent)
    if test_suite_result.count_num_failed() > 0:
        exit(1)