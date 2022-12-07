#!python3

class example:
    var1 = 0
    var2 = 0
    total = 0

    def run(self):
        print(f"var1 is {self.var1}")
        print(f"var2 is {self.var2}")
    
    def sum(self):
        self.total = self.var1 + self.var2
        return self.total
    
    def setVar(self,variable,value):
        if variable == 1:
            self.var1 = value
        elif variable == 2:
            self.var2 = value

    def __init__(self,a=5,b=4):
        print('object instantiated\n')
        self.var1 = a
        self.var2 = b
    
    def __del__(self):
        print("object destructing")
        print('thank you')

if __name__ == "__main__":
    app = example()

    print(f"app.sum() returns {app.sum()}")
    print(f"value of app.total is {app.total}")

    print("\n----------\n")
    app.setVar(1,3)
    app.setVar(2,4)    
    
    print(f"app.sum() returns {app.sum()}")
    print(f"value of app.total is {app.total}")
