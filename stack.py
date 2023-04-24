
class Stack():
    def __init__(self):
        self.array = []

    def peek(self):
        if self.array:
            return self.array[-1]
        else:
            print('Stack Empty')
    
    def push(self, value):
        if value:
            self.array.append(value)
        else:
            print( 'Invalid Input')

    def pop(self):
        if self.array:
            poped_data = self.array.pop()
            return poped_data
        else:
            print('stack empty')

    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])



if __name__ == "__main__":
    
    my_stack = Stack()
    my_stack.push("Andrei's")
    my_stack.push("Courses")
    my_stack.push("Are")
    my_stack.push("Awesome")
    my_stack.print_stack()
    #Awesome
    #Are
    #Courses
    #Andrei's

    my_stack.pop()
    my_stack.pop()
    my_stack.print_stack()
    #Courses
    #Andrei's

    print(my_stack.peek())
    #Courses

    print(my_stack.__dict__)
    #{'array': ["Andrei's", 'Courses']}

    a = [1,2,3,4,5]
    print(a.popleft())


