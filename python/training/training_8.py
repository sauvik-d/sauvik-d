name = "Sauvik Dutta"
# using in operator to check a string contains a substring or not
print("Sauvik" in name)
# dealing with complex numbers
num = complex(2, 5)
print(num.real, num.imag)
print(num)
print(round(5.49, 1))
# enums
from enum import Enum
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE.value)

