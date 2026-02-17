n = int(input("Enter number of weights: "))
weights = [0] * n

for i in range(n):
    weights[i] = int(input("Enter the weight: "))

invalid = []
very_light = []
Normal_load = []
heavy_load = []
overload = []

full_name = "RAGHUPATRUNI_ASHRIT"

L = 0
for ch in full_name:
    if ch != " ":
        L = L + 1

PLI = L % 3
total_valid = 0

for i in weights:
    if i < 0:
        invalid = invalid + [i]
    elif i < 6:
        very_light = very_light + [i]
        total_valid = total_valid + 1
    elif i < 26:
        Normal_load = Normal_load + [i]
        total_valid = total_valid + 1
    elif i < 61:
        heavy_load = heavy_load + [i]
        total_valid = total_valid + 1
    else:
        overload = overload + [i]
        total_valid = total_valid + 1

affected = 0

if PLI == 0:
    for item in overload:
        invalid = invalid + [item]
        affected = affected + 1
    overload = []
elif PLI == 1:
    for item in very_light:
        affected = affected + 1
    very_light = []
elif PLI == 2:
    for item in very_light:
        affected = affected + 1
    for item in overload:
        affected = affected + 1
    very_light = []
    overload = []

print("\nFull Name Length (L):", L)
print("PLI:", PLI)
print("\nInvalid Entries:", invalid)
print("Very Light:", very_light)
print("Normal Load:", Normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)
print("\nTotal valid weights:", total_valid)
print("Items affected by PLI rule:", affected)