# collecting user food data

# asking about food material
print("What would you like to eat tonight? I can help you out.")
print("But first of all, what do you have on the fridge?")

foodMaterial = str(input(" "))
foodMaterial = foodMaterial.replace(',', '').replace('.','').split()
with open('material.txt', 'w') as f:
	f.write('{}'.format(foodMaterial))

# asking about herbs
print("Second, what kind of herbs do you have in the kitchen?")

herbsMaterial = str(input(" "))
herbsMaterial = herbsMaterial.replace(',', '').replace('.','').split()
with open('herbs.txt', 'w') as f:
	f.write('{}'.format(herbsMaterial))

# asking about sauce
print("Last thing, what kind of sauce in your cupboard?")

sauceMaterial = str(input(" "))
sauceMaterial = sauceMaterial.replace(',', '').replace('.','').split()
with open('sauce.txt', 'w') as f:
	f.write('{}'.format(sauceMaterial))

print("So you have them all in the kitchen. Superb!")
