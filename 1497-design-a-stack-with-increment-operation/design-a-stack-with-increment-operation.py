class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize 
        self.top = -1
        self.a = [0]* maxSize 
    

    def push(self, x: int) -> None:
        if not (self.top >= self.maxSize - 1):
            self.top += 1
            self.a[self.top] = x
            
        
            

    def pop(self) -> int:
        if  (self.top < 0 ):
           return -1 
        else : 
            popped = self.a[self.top]
            self.top -= 1
            return popped 


    def increment(self, k: int, val: int) -> None:
        
            for i in range(0,min(k , self.top + 1)):
                self.a[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)