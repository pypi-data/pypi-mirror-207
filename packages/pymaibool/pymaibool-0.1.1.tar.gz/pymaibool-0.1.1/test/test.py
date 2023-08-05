from pymaibool import pBool

b = pBool(0.5)
# fix it
b.fix()

for i in range(10):
    print(b)
    if i == 4:
        print("unfix")
        b.unfix()