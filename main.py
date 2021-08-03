import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

# Test examples
EXAMPLES = [
    '_On__my___home_world_',
    '',
    '_',
    '_On__my___home_world_____',
    'On_my_home_world',
    '_____',
    '____________On__my___home_world_',
]


def test_removed_spaces(row: str) -> str:
    """
    test function
    :param row:
     str - row where spaces must be removed
    :return:
     str - row with removed spaces
    """
    return '_'.join([word for word in row.split('_') if len(word) > 0])


def remove_spaces(row: str) -> str:
    was_gap = True
    index = 0
    len_of_row = len(row)

    while index < len_of_row:

        if row[-1] == '_':
            row = row[:-1]
            len_of_row -= 1

        elif row[index] == '_' and was_gap:
            row = row[:index] + row[index + 1:]
            len_of_row -= 1
            was_gap = True

        elif row[index] != '_':
            index += 1
            was_gap = False

        else:
            index += 1
            was_gap = True

    return row


def check_answer(string_example: str) -> None:
    logger.info(f"Input: \"{string_example}\"")

    answer = remove_spaces(string_example)
    row_with_removed_spaces = test_removed_spaces(string_example)

    try:
        assert row_with_removed_spaces == answer
        logger.info(f"Output: \"{answer}\"")
    except AssertionError:
        logger.error(f"Failed: \"{row_with_removed_spaces}\" != \"{answer}\"")


if __name__ == '__main__':
    for example in EXAMPLES:
        check_answer(example)
