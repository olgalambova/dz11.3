def is_even(num: int) -> bool:
    num = str(num)
    if num [-1] == '0' or num[-1] == '2' or num[-1] == '4' or num[-1] == '6' or num[-1] == '8':
        return True
    else:
        return False




assert is_even(2494563894038**2) == True, 'Test1'
#assert is_even(1056897**2) == False, 'Test2'
#assert is_even(24945638940387**3) == False, 'Test3'
