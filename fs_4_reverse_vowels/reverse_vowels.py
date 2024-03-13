def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    char_list = []
    for char in s:
        if char in 'aeiouAEIOU':
            char_list.append(char)
    
    new_str_letters =[]
    i=1
    
    for char in s:
        if char in 'aeiouAEIOU':
            new_str_letters.append(char_list[-i])
            i+=1
        else:
            new_str_letters.append(char)
    
    return "".join(new_str_letters)

