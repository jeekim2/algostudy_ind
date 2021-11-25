inp = input().split()
A = int(inp[0])
B = int(inp[1])

class calc:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    def subtract(self):
        result = self.first - self.second
        return result
    def multiple(self):
        result = self.first * self.second
        return result
    def divide(self):
        result = int(self.first/self.second)
        return result
    def rest(self):
        result = self.first%self.second
        return result
            
var_class= calc()
var_class.setdata(A,B)
print(var_class.add())
print(var_class.subtract())
print(var_class.multiple())
print(var_class.divide())
print(var_class.rest())    
        
    