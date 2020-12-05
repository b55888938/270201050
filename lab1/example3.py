a = 2
b = 6
c = -20
delta_sqrr = ((b**2) - (4 * a * c)) ** (1/2)
root_1 = (b + delta_sqrr) / (2 * a)
root_2 = (b - delta_sqrr) / (2 * a)
d = "root1={},root2={}"
print(d.format(root_1, root_2))