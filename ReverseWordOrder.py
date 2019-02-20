def reverseWordOrder(str):
    """
    Args:
        {string} str
    Returns:
        {string} The word-reversed string.
    """
    # Write your code here.
    split_string = str.split(' ')
    output_string = ''

    beginning = 0
    end = len(split_string) - 1

    for i in range(beginning, end):
        split_string[end - i] += output_string[i]

   # split_string.join(' ')

    print(output_string)



reverseWordOrder('Hello. this is hi')