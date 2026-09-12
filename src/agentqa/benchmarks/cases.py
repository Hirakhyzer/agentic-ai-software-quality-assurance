from __future__ import annotations

from agentqa.models import BugCase, TestVector


CASES: tuple[BugCase, ...] = (
    BugCase(
        case_id="inclusive_sum_off_by_one",
        issue="sum_to_n should include n itself, but the generated implementation omits the upper boundary.",
        function_name="sum_to_n",
        source="""def sum_to_n(n):
    total = 0
    for value in range(n):
        total += value
    return total
""",
        reference_source="""def sum_to_n(n):
    total = 0
    for value in range(n + 1):
        total += value
    return total
""",
        public_tests=(TestVector(args=(4,), expected=10, name="includes_upper_bound"),),
        hidden_inputs=((0,), (1,), (7,)),
        bug_line=3,
        category="off_by_one",
    ),
    BugCase(
        case_id="mean_wrong_denominator",
        issue="mean returns an inflated result because the denominator is wrong.",
        function_name="mean",
        source="""def mean(values):
    if not values:
        return 0.0
    return sum(values) / (len(values) - 1)
""",
        reference_source="""def mean(values):
    if not values:
        return 0.0
    return sum(values) / len(values)
""",
        public_tests=(TestVector(args=([2.0, 4.0, 6.0],), expected=4.0, name="three_values"),),
        hidden_inputs=(([],), ([3.0],), ([1.0, 3.0],)),
        bug_line=4,
        category="arithmetic",
    ),
    BugCase(
        case_id="index_shift",
        issue="get_item returns the next element rather than the requested index.",
        function_name="get_item",
        source="""def get_item(items, index):
    return items[index + 1]
""",
        reference_source="""def get_item(items, index):
    return items[index]
""",
        public_tests=(TestVector(args=([10, 20, 30], 0), expected=10, name="first_item"),),
        hidden_inputs=((["a", "b", "c"], 1), ([1, 2], 1)),
        bug_line=2,
        category="indexing",
    ),
    BugCase(
        case_id="missing_trim",
        issue="normalize_name should remove surrounding whitespace before lowercasing.",
        function_name="normalize_name",
        source="""def normalize_name(name):
    return name.lower()
""",
        reference_source="""def normalize_name(name):
    return name.strip().lower()
""",
        public_tests=(TestVector(args=("  Ada ",), expected="ada", name="surrounding_spaces"),),
        hidden_inputs=(("BOB",), (" eve  ",), ("",)),
        bug_line=2,
        category="string_normalization",
    ),
    BugCase(
        case_id="zero_denominator_guard",
        issue="safe_ratio should return None only for a zero denominator; negative denominators are valid.",
        function_name="safe_ratio",
        source="""def safe_ratio(numerator, denominator):
    if denominator < 0:
        return None
    return numerator / denominator
""",
        reference_source="""def safe_ratio(numerator, denominator):
    if denominator == 0:
        return None
    return numerator / denominator
""",
        public_tests=(TestVector(args=(5.0, 0.0), expected=None, name="zero_denominator"),),
        hidden_inputs=((6.0, 3.0), (6.0, -3.0), (0.0, -2.0)),
        bug_line=2,
        category="wrong_condition",
    ),
    BugCase(
        case_id="clamp_upper_return",
        issue="clamp should return the configured upper bound when the value exceeds it.",
        function_name="clamp",
        source="""def clamp(value, lower, upper):
    if value < lower:
        return lower
    if value > upper:
        return upper - 1
    return value
""",
        reference_source="""def clamp(value, lower, upper):
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value
""",
        public_tests=(TestVector(args=(20, 0, 10), expected=10, name="above_upper"),),
        hidden_inputs=((-2, 0, 10), (10, 0, 10), (5, 0, 10)),
        bug_line=5,
        category="boundary",
    ),
    BugCase(
        case_id="identity_vs_equality",
        issue="count_matches should use value equality rather than object identity.",
        function_name="count_matches",
        source="""def count_matches(items, target):
    return sum(1 for item in items if item is target)
""",
        reference_source="""def count_matches(items, target):
    return sum(1 for item in items if item == target)
""",
        public_tests=(TestVector(args=([[1], [1]], [1]), expected=2, name="equal_distinct_objects"),),
        hidden_inputs=((["x", "y", "x"], "x"), ([1, 2, 1], 1)),
        bug_line=2,
        category="operator",
    ),
    BugCase(
        case_id="positive_integer_boundary",
        issue="parse_positive_int must reject zero as well as negative values.",
        function_name="parse_positive_int",
        source="""def parse_positive_int(text):
    value = int(text)
    if value < 0:
        return None
    return value
""",
        reference_source="""def parse_positive_int(text):
    value = int(text)
    if value <= 0:
        return None
    return value
""",
        public_tests=(TestVector(args=("0",), expected=None, name="zero_not_positive"),),
        hidden_inputs=(("1",), ("9",), ("-2",)),
        bug_line=3,
        category="boundary",
    ),
)


def get_case(case_id: str) -> BugCase:
    for case in CASES:
        if case.case_id == case_id:
            return case
    raise KeyError(case_id)
