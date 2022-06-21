'''
1i^ + 5j^
1i^ + 5j^  + 8k^
'''

from re import I


class Vec2d:
    def __init__(self,i,j) :
        self.icap=i
        self.jcap=j

    def show(self):
        print(f"{self.icap}i^ + {self.jcap}j^")

class Vec3d(Vec2d):
    def __init__(self, i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def show(self):
        print(f"{self.icap}i^ + {self.jcap}j^ + {self.kcap}k^")

v2=Vec2d(5,6)
v2.show()

v3=Vec3d(2,3,4)
v3.show()
    