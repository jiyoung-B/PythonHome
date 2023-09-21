import copy
# mutable
# original = [1, 2, 3]
# target = original
# print(original, target)
# original[0] = 1000
# print(original, target)

# immutable
original = [1, 2, 3]
# target = original
target = copy.deepcopy(original)
print(original, target)
original[0] = 1000
print(original, target)