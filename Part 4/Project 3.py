# Advance Vector Operations

class Vector2D:
    __slots__ = ['x','y']
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other,Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __mul__(self,scalar):
        if isinstance(scalar,(int,float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self,scalar):
        return self.__mul__(scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other,Vector2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

class VectorManager:
    def __init__(self,initial_vectors = None):
        self.vectors = []
        if initial_vectors:
            for vec in initial_vectors:
                if isinstance(vec,Vector2D):
                    self.vectors.append(vec)
                else:
                    print(f"Warning: {vec} is not a Vector2D, skipped.")
    def display_vectos(self):
        print("---- Vectors in Manager ---" )
        for i,vec in enumerate(self.vectors,start=1):
            print(f"Vector {i}: {vec}")
    
    def total_sum(self):
        if not self.vectors:
            return Vector2D(0,0)
        total = Vector2D(0,0)
        for vec in self.vectors:
            total += vec  # Yahan Vector2D ka __add__ method use hoga
        return total
    def add_vector(self,vec):
        if isinstance(vec,Vector2D):
            self.vectors.append(vec)
            print(f"Added {vec} to manager.")
        else:
            print("Can only add Vector2d Objects.")

v1 = Vector2D(1,2)
v2 = Vector2D(3,4)
# print(v1,v2)
v_sum = v1 + v2
# print(v_sum*67)
# print(45*v_sum)

# print(v1==Vector2D(1,2))

manager = VectorManager((v1,v2,v_sum,Vector2D(5,7),{234,65}))

manager.display_vectos()
manager.add_vector(Vector2D(67,58))
manager.add_vector("sdfsdf")
manager.add_vector(Vector2D(99,78))

manager.display_vectos()

print(manager.total_sum())
