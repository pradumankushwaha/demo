def get_max_str(lst, fallback=''):
    if not lst:
        return fallback

    max_str = lst[0]   # list is not empty

    for x in lst:
        if len(x) > len(max_str):
            max_str = x

    return max_str


print(get_max_str(['Alice', 'Bob', 'Pete']))
# 'Alice'

print(get_max_str(['aaa', 'aaaa', 'aa']))
# 'aaaa'

print(get_max_str(['']))
# ''

print(get_max_str([], fallback='NOOOOOOOOO!!!!!!'))
# NOOOOOOOOO!!!!!!
