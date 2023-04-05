def reverse_string(string):
    try:
      if string is None or len(string) < 2 or not(isinstance(string, str)):
        return "Invalid input"
      else:
        return ''.join(reversed(string))
    except TypeError:
        return "Invalid input"

def reverse_string(string):
    backwards = []
    for i in range(len(string)-1, -1, -1):
       backwards.append(string[i])
    return ''.join(backwards)

def reverse_string(string):
    string = list(string)
    string.reverse()
    return ''.join(string)


#A smarter way to do this , can be taking a pair of elements from either end of the string and swapping them
#We have start at both the ends and continue swapping pairs till the middle of the string
#This way we can avoid having to create a new array and save on space complexity while keeping time complexity at O(n)

def swap(string, a, b): #Function which swaps two characters of a string
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)

def smarter_reverse(string):
    for i in range(len(string)//2):
        string = swap(string, i, len(string)-i-1)
    return string


if __name__ == '__main__':
    string = 'My name is Andrei'
    # string = 3
    print(reverse_string(string))
    print(smarter_reverse(string))