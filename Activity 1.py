#Python program to overload the equality
#And less than operators

class A:
    def __init__(self,a):
        self.a = a  
    def __lt__(self,other):
        if (self.a<other.a):
            return "Object 1 is lesser than object 2."
        else:
            return "Object 2 is lesser than object 1."

def __eq__(self,other):
    if (self.a == other.a):
        return "Both are equal."
    else:
        return "Not equal values."

object1 = A(2)
object2 = A(3)
print("Passed Values: ", object1.a, object2.a)
print(object1 < object2)

object3 = A(4)
object4 = A(4)
print("Passed Values: ", object3.a, object4.a)
print(object3 == object4)
