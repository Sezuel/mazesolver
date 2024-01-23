def word_count_memo(document, memos):
    print(f"Memos already has information:{str(bool(memos))}")
    if documents in memos:
        return memos[document], memos
    memos[document] = word_count(document)
    return memos[document], memos

def word_count(document):
    count = len(document.split())
    return count

run_cases = [
    (
        "Doc 1: In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cachedresult when the same inputs occur again.",
        36,
    ),
    (
        "Doc 1: A very small document.",
        6,
    ),
    (
        "This number is intentionally wrong to test that previous memoization is working!",
        9000,
    ),
]

submit_cases = run_cases + [
    ("", 0),
    (
        "Doc 1: In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cachedresult when the same inputs occur again.",
        36,
    ),
    (
        "Doc 1: A very small document.",
        6,
    ),
    (
        "This number is intentionally wrong to test that previous memoization is working!",
        9000,
    ),
]


def test(memos, input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Document: {input1}")
    print(f"Expecting: {expected_output}")
    try:
        result, memos = word_count_memo(input1, memos)
    except Exception as e:
        result, memos = e, {}
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    test_cases = submit_cases
    if "__RUN__" in globals():
        test_cases = run_cases
    passed = 0
    failed = 0
    memos = {}
    for test_case in test_cases:
        correct = test(memos, *test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


main()
