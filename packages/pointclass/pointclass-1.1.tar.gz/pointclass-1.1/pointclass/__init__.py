import math
class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def show(self):
        return self.x
        return self.y
    def __add__(self,p):
        return(self.x+p.x,self.y+p.y)
    def __sub__(self,p):
        return(self.x-p.x,self.y-p.y)
    def __mult__(self,p):
        return(self.x * p.x,self.y * p.y)
    def __eq__(self,p):
         return(self.x==p.x,self.y==p.y)
    def __repro__():
        return "point(self.x,self.y)"
    def distance(p1,p2):
        return math.hypot(p2.x-p1.x,p2.y-p1.y)
    def copy():
        print("from pulp import*")
        print("model=LpProblem(sense=LpMaximize)")
        print("x=LpVariable(name='x',lowBound=0)")
        print("y=LpVariable(name='y',lowBound=0)")
        print("model+=(4*x+6*y<=24)")
        print("model+=(5*x+75*y<=15)")
        print("model+=150*x+75*y")
        print("model.solve()")
        print("model.objective.value()")
        print("x.value()") 
        print("y.value()")
        print("copy")