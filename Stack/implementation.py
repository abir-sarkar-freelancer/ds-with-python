class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        return f"{data} pushed to the stack"
    
    def is_empty(self):
        return self.stack == list()
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
        
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    
    def get_stack(self):
        return self.stack
      
      
if __name__ == "__main__":
    # simple application
    # reversing string
    def rev_string_stack(input_string:str) -> str:
        new_stack = Stack()
        for char in input_string:
            new_stack.push(char)
        rev_string_output = ""
        while not new_stack.is_empty():
            rev_string_output += new_stack.pop()
        
    return rev_string_output

    rev_string_stack("Abir")
