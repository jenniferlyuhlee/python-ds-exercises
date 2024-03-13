def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return freq(num1) == freq(num2)


def freq (num):
    freq_dict={}
    for digit in str(num):
        freq_dict[digit]=freq_dict.get(digit,0) + 1
    return freq_dict