def longest_alternating_subsequence(input_array):
    output = []
    x = None
    for i in range(len(input_array)):
        if input_array[i] != x:
            output.append(input_array[i])
            x = input_array[i]
        else: continue
    return output

example_array = [0, 1, 0, 0, 0, 1, 0]
print(longest_alternating_subsequence(example_array))