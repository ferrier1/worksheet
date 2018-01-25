
input_ip = [10, 7, 1, 1]
input_mask = [255, 255, 255, 0]


binary_list = []
for oct in input_ip:
    binary = bin(oct+256)[3:]
    binary_list.append(binary)
g = ''.join(binary_list)

print(binary_list)
print(g)
t = int(g, base=2) + 1
u = str(bin(t))[2:]
print(u)

x = 32 - len(str(u))

r = "{}{}".format("0" * x, u)
print(r)


