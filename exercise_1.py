#!/usr/bin/env python3

class Cosmetic:
    pass

cosmetic = Cosmetic()

print(cosmetic)
print(isinstance(cosmetic, Cosmetic))
print(isinstance(cosmetic, object))

class ForFace(Cosmetic):
    pass

forface = ForFace
print(forface)
print(isinstance(forface, Cosmetic))
print(isinstance(forface, ForFace))
print(isinstance(forface, object))

class Powder(ForFace):
    pass

powder = Powder()

print(powder)
print(isinstance(powder,ForFace))
print(isinstance(powder,Powder))
print(isinstance(powder,object))

print(isinstance(powder, ForFace))
print(isinstance(forface,Powder))