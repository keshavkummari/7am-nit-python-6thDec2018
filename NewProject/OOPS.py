'''
example 1:
class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]


print(py_solution().sub_sets([4, 5, 6]))

Example 2:

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"My name is {self.first_name} {self.last_name}"

    def likes(self, thing):
          return f"{self.first_name} likes {thing}!"

p = Person('Tim', 'Garcia')

p.full_name() # My name is Tim Garcia
p.likes("computers") # Tim likes computers!
'''