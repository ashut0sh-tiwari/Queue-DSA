"""Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty)."""
from collections import deque #import deque from collections

class MyStack: #initialise class

    def __init__(self): #contructor method
        self.q = deque() #initialising deque
        

    def push(self, x): #push method
        self.q.append(x) #use append method to push elements from the right
        

    def pop(self): #pop method
        
        for i in range(len(self.q)-1): #iterating every element and pop them from the left as queue is FILO and push them to the from the right side as we are using them as a stack and stack is LIFO
            self.push(self.q.popleft())
        return self.q.popleft() #then remove the left element as it is the last element of the stack
        

    def top(self): #return the last element of the stack
        return self.q[-1]
        

    def empty(self): #return true if queue is empty
        return len(self.q)==0