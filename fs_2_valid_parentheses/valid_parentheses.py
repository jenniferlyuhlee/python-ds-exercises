def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count_open=0
    count_close=0
    for p in parens:
        if parens[0] == ')':
            return False
        elif p == '(':
            count_open+=1
        elif p == ')':
            count_close+=1
    
    return count_open == count_close