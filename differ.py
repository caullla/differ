
def get_longest_substring(line_x, line_y):
    x_len = len(line_x)
    y_len = len(line_y)
    counter = [[0]*(y_len + 1) for x in range(x_len + 1)]
    longest = 0
    result = ''
    for i in range(x_len):
        for j in range(y_len):
            if line_x[i] == line_y[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    longest = c
                    result = line_x[i-c+1:i+1]
    return result


def find_matches(old_string, new_string):
    """
    return generator for longest matches
                   'same_prefix_123_same_suffix'
                   'same2prefix_1233_same_suffix'
                                |
                         '3_same_suffix'
              'same_prefix_12'      ''
              'same2prefix_123'     ''
                      |
                  'prefix_12'
            'same_'        ''
            'same2'        '3'
               |
             'same'
            ''     '_'
            ''     '2'

        'same', 'prefix_12', '3_same_suffix'

    """

    longest_match = get_longest_substring(old_string, new_string)
    if longest_match:
        old_left, old_right = old_string.split(longest_match, 1)
        new_left, new_right = new_string.split(longest_match, 1)

        for item in find_matches(old_left, new_left):
            yield item

        yield longest_match

        for item in find_matches(old_right, new_right):
            yield item
    else:
        if old_string:
            yield '({})'.format(old_string)
        if new_string:
            yield '[{}]'.format(new_string)
