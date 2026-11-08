n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

People = []
for i in range(n):
    person = Person(name[i], address[i], region[i])
    People.append(person)

name.sort()
target = name[-1]

for p in People:
    if p.name == target:
        print(f'name {p.name}')
        print(f'addr {p.address}')
        print(f'city {p.region}')



