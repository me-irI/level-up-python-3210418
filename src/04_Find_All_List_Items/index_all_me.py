def index_all(nested_list, number):
    for item in nested_list:
        if isinstance(item, list):
            index_all(item, number)
        elif item == number:
            print(f"number at {item}")
    return "temp"

# commands used in solution video for reference
if __name__ == '__main__':
    example = [
        [
            [1, 2, 3], 
            2, 
            [1, 3]
        ], 
        [
            1, 2, 3
        ]
              ]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]