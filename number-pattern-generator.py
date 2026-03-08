def number_pattern(n):
    numbers = ''
    if type(n) == int:
        if n < 1:
            return 'Argument must be an integer greater than 0.'
        else:
            for i in range(1,n+1):
                numbers += f'{i} '
            return numbers.strip()
    else:
        return 'Argument must be an integer value.'

number_pattern(4)