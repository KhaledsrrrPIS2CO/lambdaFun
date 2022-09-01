# write af unction to calculate the value of 3X +1

def f(x):
    return 3 * x + 1


print(f(2))

# now we use Lambda

lambda x: 3 * x + 1

g = lambda x: 3 * x + 1
print(g(2))


def f(x):
    return 3 * x + 1


print(f(2))

k = lambda x: 3 * x + 1
print(k(2))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("Kahled", "AlGHaiSh"))
