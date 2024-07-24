data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(args):
    s = 0
    if isinstance(args, str):
        s += len(args)
    elif isinstance(args, (int, float)):
        s += args
    elif isinstance(args, (list, tuple, set)):
        for i in args:
            s += calculate_structure_sum(i)
    elif isinstance(args, dict):
        for key, value in args.items():
            s += calculate_structure_sum(key)
            s += calculate_structure_sum(value)
    return s


result = calculate_structure_sum(data_structure)
print(result)
