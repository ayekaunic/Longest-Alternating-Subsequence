# Longest-Alternating-Subsequence
This script returns the longest possible subsequence of the input array where each element is different than the one preceding it.

To achieve this, the function first initializes an empty **output** list and a variable **x** set to **None**. It then loops over each element in the input array and checks whether the current element is not equal to the previous element (stored in **x**). If the current element is not equal to the previous element, it is appended to the **output** list and **x** is updated to the current element. If the current element is equal to the previous element, the loop continues to the next element.

Finally, the function returns the resulting **output** list, which contains the longest alternating subsequence of the input array. The last few lines of the code define an example input array, pass it to the **longest_alternating_subsequence** function, and print the resulting output. In this case, the output should be [0, 1, 0, 1, 0].
