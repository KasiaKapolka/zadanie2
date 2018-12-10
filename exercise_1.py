#!/usr/bin/env python3

class Cosmetics:
    pass

cosmetics = Cosmetics()

print(cosmetics)
print(isinstance(cosmetics, Cosmetics))
print(isinstance(cosmetics, object))

class For_face(Cosmetics):
    pass

for_face = For_face()

print(for_face)
print(isinstance(for_face, Cosmetics))
print(isinstance(for_face, For_face))
print(isinstance(for_face, object))

class Powder(For_face):
    pass

powder = Powder()

print(powder)
print(isinstance(powder,For_face))
print(isinstance(powder,Powder))
print(isinstance(powder,object))

print(isinstance(powder, For_face))
print(isinstance(for_face,Powder))