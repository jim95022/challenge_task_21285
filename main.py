
# Test examples
STRING_EXAMPLE = '_On__my___home_world_'
STRING_EXAMPLE1 = ''
STRING_EXAMPLE2 = '_'
STRING_EXAMPLE3 = '_On__my___home_world_____'
STRING_EXAMPLE4 = 'On_my_home_world'
STRING_EXAMPLE5 = '_____'
STRING_EXAMPLE6 = '____________On__my___home_world_'


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
    shifted_gaps = 0

    for index in range(len(row)):
        if row[index] == '_' and was_gap:
            row = row[index] + row[:index] + row[index + 1:]
            shifted_gaps += 1

        was_gap = row[index] == '_'

    if len(row) > 0 and row[-1] == '_':
        row = row[:-1]

    return row[shifted_gaps:]


if __name__ == '__main__':
    assert remove_spaces(STRING_EXAMPLE) == test_removed_spaces(STRING_EXAMPLE)
    assert remove_spaces(STRING_EXAMPLE1) == test_removed_spaces(STRING_EXAMPLE1)
    assert remove_spaces(STRING_EXAMPLE2) == test_removed_spaces(STRING_EXAMPLE2)
    assert remove_spaces(STRING_EXAMPLE3) == test_removed_spaces(STRING_EXAMPLE3)
    assert remove_spaces(STRING_EXAMPLE4) == test_removed_spaces(STRING_EXAMPLE4)
    assert remove_spaces(STRING_EXAMPLE5) == test_removed_spaces(STRING_EXAMPLE5)
    assert remove_spaces(STRING_EXAMPLE6) == test_removed_spaces(STRING_EXAMPLE6)

