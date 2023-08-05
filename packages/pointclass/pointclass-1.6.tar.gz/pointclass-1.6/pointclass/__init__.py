def lpp2():
        print("from pulp import*")
        print("model=LpProblem(sense=LpMaximize)")
        print("x=LpVariable(name='x',lowBound=0)")
        print("y=LpVariable(name='y',lowBound=0)")
        print("model+=(4*x+6*y<=24)")
        print("model+=(5*x+75*y<=15)")
        print("model")
        print("model+=150*x+75*y")
        print("model.solve()")
        print("model.objective.value()")
        print("x.value()") 
        print("y.value()")
        print("copy")
def lpp1():
       print("from scipy.optimize import linprog")
       print("objfn=[-4,-1]")
       print("lhs=[[1,1],[3,1]]")
       print("rhs=[50,90]")
       print("opt=linprog(c=objfn,A_ub=lhs,b_ub=rhs,method='revised simplex')")
       print("print(opt)")
def combinet():
      print("from sympy import*")
      print("a=Point(7,-2)")
      print("b=Point(6,2)")
      print("seg=Segment(a,b)")
      print("s1=seg.rotate(pi)")
      print("rotation about origin an angle")
      print("s2=s1.scale(7)")#scaling in x-co-ordinate by 7 units
      print("s3=s2.scale(-4,-4)")#uniform scaling by -4 units
      #reflection through axis 
      print("x,y=s3.points")
      print("m=Matrix([[1,0,0],[0,-1,0],[0,0,1]]) ")
      print("x_new=x.transform(m)")
      print("y_new=y.transform(m)")
      print("print(Segment(x_new,y_new))")
      print("")
def meshgrid():
     print("from mpl_toolkits import mplot3d")
     print("import numpy as np")
     print("from pylab import*")
     print("def f(x,y):")
     print("  return np.sin(x+y)")
     print("x=np.linspace(-2*pi,2*pi,30)")
     print("y=np.linspace(-2*pi,2*pi,30)")
     print("x,y=np.meshgrid(x,y)")
     print("z=f(x,y)")
     print("ax=axes(projection='3d')")
     print("ax.contour3D(x,y,z,50)")
     print("xlabel('x')")
     print("ylabel('y')")
     print("title('contour3d')")
     print("legend()")
     print("show()")
def wireframe():
     print("from mpl_toolkits import mplot3d")
     print("import numpy as np")
     print("from pylab import*")
     print("def f(x,y):")
     print("  return np.sin(x)+np.cos(x)")
     print("x=np.linspace(-5,5,30)")
     print("y=np.linspace(-5,5,30)")
     print("x,y=np.meshgrid(x,y)")
     print("z=f(x,y)")
     print("ax=axes(projection='3d')")
     print("ax.plot_wireframe(x,y,z,rstride=2,cstride=2)")
     print("xlabel('x')")
     print("ylabel('y')")
     print("title('$z=sin(x)+cos(x)$')")
     print("legend()")
     print("show()")
def parabola():
     print("from mpl_toolkits import mplot3d")
     print("import numpy as np")
     print("from pylab import*")
     print("def f(x,y):")
     print("  return x**2+y**2")
     print("x=np.linspace(-5,5,30)")
     print("y=np.linspace(-5,5,30)")
     print("x,y=np.meshgrid(x,y)")
     print("z=f(x,y)")
     print("ax=axes(projection='3d')")
     print("ax.plot_surface(x,y,z)")
     print("xlabel('x')")
     print("ylabel('y')")
     print("title('3d parabola')")
     print("legend()")
     print("show()")




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
    