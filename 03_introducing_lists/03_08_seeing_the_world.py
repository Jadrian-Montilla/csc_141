Places = ["Paris", "Japan", "Buenos Ares", "Hawaii", "Disney World"]

print("List of places:")
print(Places)

print("\n List of places: (organized)")
print(sorted(Places))

print("\n Original list:")
print(Places)

print("\n List of places: (organized backwards)")
print(sorted(Places, reverse=True))

print("\n Original list:")
print(Places)

Places.reverse()
print("\n Reversed list:")
print(Places)

Places.reverse()
print("\n Reversed-Reversed list:")
print(Places)

Places.sort()
print("\n Sorted list:")
print(Places)

Places.sort(reverse=True)
print("\n Reverse-Sorted list:")
print(Places)