# Ontology triples (Subclass, Superclass)
triples = [
    ("Dog", "Animal"),
    ("Cat", "Animal"),
    ("Animal", "LivingBeing"),
    ("Car", "Vehicle"),
    ("Bike", "Vehicle"),
    ("ElectricCar", "Car")
]

# Step 1: Build Knowledge Graph
graph = {}
for subclass, superclass in triples:
    if superclass not in graph:
        graph[superclass] = []
    graph[superclass].append(subclass)

# Step 2: Find all subclasses of a class
def get_all_subclasses(cls):
    subclasses = []
    if cls in graph:
        for sub in graph[cls]:
            subclasses.append(sub)
            subclasses.extend(get_all_subclasses(sub))
    return subclasses

# Step 3: Check if A is a subclass of B
def is_subclass(sub, parent):
    for child, par in triples:
        if child == sub and par == parent:
            return True
        if child == sub:
            return is_subclass(par, parent)
    return False

# ---------------------- OUTPUT TEST ------------------------
print("All subclasses of 'Animal':", get_all_subclasses("Animal"))
print("All subclasses of 'LivingBeing':", get_all_subclasses("LivingBeing"))
print("Is 'Dog' a subclass of 'Animal'? ->", is_subclass("Dog", "Animal"))
print("Is 'ElectricCar' a subclass of 'Vehicle'? ->", is_subclass("ElectricCar", "Vehicle"))
print("Is 'Bike' a subclass of 'Car'? ->", is_subclass("Bike", "Car"))
