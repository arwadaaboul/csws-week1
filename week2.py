names = ['Arwa', 'Reem', 'May', 'Basma', 'Omar', 'Achraf', 'Mohammad']
# 3-1

for y in range(6):
    print(names[y])


#3-2

for x in range(6):
    print(f"Hello, {names[x]}")

# 3-8

locations = ['Dubai', 'New York', 'Liverpool', 'Amman', 'Paris']

print(locations)
#alpahbetical order
print(sorted(locations))
#
locations.sort(reverse=True)
print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort()
print(locations)

# 3-10


print(len(locations))

locations.append("London")
print(locations)

locations.insert(2, "Manchester")
print(locations)

del locations[1]
print(locations)

locations.remove("Manchester")
print(locations)

locations.pop(3)
print(locations)

