# leetcode

[![Build Status](https://travis-ci.org/weak-head/leetcode.svg?branch=master)](https://travis-ci.org/weak-head/leetcode)
[![codecov](https://codecov.io/gh/weak-head/leetcode/branch/master/graph/badge.svg)](https://codecov.io/gh/weak-head/leetcode)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fcb957dc188a49459a29aaf9f102df10)](https://www.codacy.com/app/weak-head/leetcode?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=weak-head/leetcode&amp;utm_campaign=Badge_Grade)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Building and testing

```bash
# Setup and activate virtual environment
python3 -m venv venv
. venv/bin/activate

# Install test dependencies and the module
pip install pytest coverage
pip install --editable .

# Run all test cases and generate code coverage
pytest
coverage run -m pytest

# Output the coverage report
coverage report
coverage html
```

### Create skeleton for a new problem and update the readme

```bash
pip install requests argparse termcolor

scripts/touch.py <id> <url>
```

### Regenerate markdown table and verify links

```bash
pip install requests argparse pytablewritter termcolor

scripts/genmd.py --verify
```

## List of Problems
|  #   |                                                                    Title                                                                    |                                   Solution                                    |                                   Test cases                                    |
|-----:|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
|    1 | [Two Sum](https://leetcode.com/problems/two-sum/)                                                                                           | [src](leetcode/p0001_two_sum.py)                                              | [tst](tests/test_p0001_two_sum.py)                                              |
|    2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)                                                                           | [src](leetcode/p0002_add_two_numbers.py)                                      | [tst](tests/test_p0002_add_two_numbers.py)                                      |
|    3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)             | [src](leetcode/p0003_longest_substring_without_repeating_characters.py)       | [tst](tests/test_p0003_longest_substring_without_repeating_characters.py)       |
|    4 | [Median Of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)                                                   | [src](leetcode/p0004_median_of_two_sorted_arrays.py)                          | [tst](tests/test_p0004_median_of_two_sorted_arrays.py)                          |
|    5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)                                               | [src](leetcode/p0005_longest_palindromic_substring.py)                        | [tst](tests/test_p0005_longest_palindromic_substring.py)                        |
|    6 | [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)                                                                       | [src](leetcode/p0006_zigzag_conversion.py)                                    | [tst](tests/test_p0006_zigzag_conversion.py)                                    |
|    7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/)                                                                           | [src](leetcode/p0007_reverse_integer.py)                                      | [tst](tests/test_p0007_reverse_integer.py)                                      |
|    8 | [String To Integer Atoi](https://leetcode.com/problems/string-to-integer-atoi/)                                                             | [src](leetcode/p0008_string_to_integer_atoi.py)                               | [tst](tests/test_p0008_string_to_integer_atoi.py)                               |
|    9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/)                                                                       | [src](leetcode/p0009_palindrome_number.py)                                    | [tst](tests/test_p0009_palindrome_number.py)                                    |
|   10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)                                                   | [src](leetcode/p0010_regular_expression_matching.py)                          | [tst](tests/test_p0010_regular_expression_matching.py)                          |
|   11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)                                                       | [src](leetcode/p0011_container_with_most_water.py)                            | [tst](tests/test_p0011_container_with_most_water.py)                            |
|   12 | [Integer To Roman](https://leetcode.com/problems/integer-to-roman/)                                                                         | [src](leetcode/p0012_integer_to_roman.py)                                     | [tst](tests/test_p0012_integer_to_roman.py)                                     |
|   13 | [Roman To Integer](https://leetcode.com/problems/roman-to-integer/)                                                                         | [src](leetcode/p0013_roman_to_integer.py)                                     | [tst](tests/test_p0013_roman_to_integer.py)                                     |
|   14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)                                                               | [src](leetcode/p0014_longest_common_prefix.py)                                | [tst](tests/test_p0014_longest_common_prefix.py)                                |
|   15 | [3Sum](https://leetcode.com/problems/3sum/)                                                                                                 | [src](leetcode/p0015_3sum.py)                                                 | [tst](tests/test_p0015_3sum.py)                                                 |
|   16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/)                                                                                 | [src](leetcode/p0016_3sum_closest.py)                                         | [tst](tests/test_p0016_3sum_closest.py)                                         |
|   17 | [Letter Combinations Of A Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)                               | [src](leetcode/p0017_letter_combinations_of_a_phone_number.py)                | [tst](tests/test_p0017_letter_combinations_of_a_phone_number.py)                |
|   18 | [4Sum](https://leetcode.com/problems/4sum/)                                                                                                 | [src](leetcode/p0018_4sum.py)                                                 | [tst](tests/test_p0018_4sum.py)                                                 |
|   19 | [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)                                         | [src](leetcode/p0019_remove_nth_node_from_end_of_list.py)                     | [tst](tests/test_p0019_remove_nth_node_from_end_of_list.py)                     |
|   20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)                                                                       | [src](leetcode/p0020_valid_parentheses.py)                                    | [tst](tests/test_p0020_valid_parentheses.py)                                    |
|   21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)                                                             | [src](leetcode/p0021_merge_two_sorted_lists.py)                               | [tst](tests/test_p0021_merge_two_sorted_lists.py)                               |
|   22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)                                                                 | [src](leetcode/p0022_generate_parentheses.py)                                 | [tst](tests/test_p0022_generate_parentheses.py)                                 |
|   23 | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)                                                                 | [src](leetcode/p0023_merge_k_sorted_lists.py)                                 | [tst](tests/test_p0023_merge_k_sorted_lists.py)                                 |
|   24 | [Swap Nodes In Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)                                                                   | [src](leetcode/p0024_swap_nodes_in_pairs.py)                                  | [tst](tests/test_p0024_swap_nodes_in_pairs.py)                                  |
|   25 | [Reverse Nodes In K Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)                                                         | [src](leetcode/p0025_reverse_nodes_in_k_group.py)                             | [tst](tests/test_p0025_reverse_nodes_in_k_group.py)                             |
|   26 | [Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)                                   | [src](leetcode/p0026_remove_duplicates_from_sorted_array.py)                  | [tst](tests/test_p0026_remove_duplicates_from_sorted_array.py)                  |
|   27 | [Remove Element](https://leetcode.com/problems/remove-element/)                                                                             | [src](leetcode/p0027_remove_element.py)                                       | [tst](tests/test_p0027_remove_element.py)                                       |
|   28 | [Implement Strstr](https://leetcode.com/problems/implement-strstr/)                                                                         | [src](leetcode/p0028_implement_strstr.py)                                     | [tst](tests/test_p0028_implement_strstr.py)                                     |
|   29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)                                                                   | [src](leetcode/p0029_divide_two_integers.py)                                  | [tst](tests/test_p0029_divide_two_integers.py)                                  |
|   32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)                                                       | [src](leetcode/p0032_longest_valid_parentheses.py)                            | [tst](tests/test_p0032_longest_valid_parentheses.py)                            |
|   33 | [Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)                                             | [src](leetcode/p0033_search_in_rotated_sorted_array.py)                       | [tst](tests/test_p0033_search_in_rotated_sorted_array.py)                       |
|   35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/)                                                             | [src](leetcode/p0035_search_insert_position.py)                               | [tst](tests/test_p0035_search_insert_position.py)                               |
|  146 | [Lru Cache](https://leetcode.com/problems/lru-cache/)                                                                                       | [src](leetcode/p0146_lru_cache.py)                                            | [tst](tests/test_p0146_lru_cache.py)                                            |
| 1005 | [Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)                           | [src](leetcode/p1005_maximize_sum_of_array_after_k_negations.py)              | [tst](tests/test_p1005_maximize_sum_of_array_after_k_negations.py)              |
| 1006 | [Clumsy Factorial](https://leetcode.com/problems/clumsy-factorial/)                                                                         | [src](leetcode/p1006_clumsy_factorial.py)                                     | [tst](tests/test_p1006_clumsy_factorial.py)                                     |
| 1007 | [Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)                             | [src](leetcode/p1007_minimum_domino_rotations_for_equal_row.py)               | [tst](tests/test_p1007_minimum_domino_rotations_for_equal_row.py)               |
| 1008 | [Construct Binary Search Tree From Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) | [src](leetcode/p1008_construct_binary_search_tree_from_preorder_traversal.py) | [tst](tests/test_p1008_construct_binary_search_tree_from_preorder_traversal.py) |
