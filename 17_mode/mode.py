def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    #code logic learned from:
    #https://www.nobledesktop.com/learn/python/mode-in-python

    mode_dict = {}
    for num in nums:
        if num in mode_dict:
            mode_dict[num] += 1
        else:
            mode_dict[num] = 1
    
    for num, count in mode_dict.items():
        if count == max(mode_dict.values()):
            return num