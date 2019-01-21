# collecting user food data

# asking about food material
def foodMaterial():
	print("What would you like to eat tonight? I can help you out.")
	print("But first of all, what do you have on the fridge?")

	foodMaterial = str(input(" "))

	# remove characters and numbers 
	characters = "1234567890$'\\'!@#$%^&*()[]'|?></,.:;"''
	for elem in foodMaterial:
		if elem in characters:
			foodMaterial = foodMaterial.replace(elem, '')

	# split input
	foodMaterial = foodMaterial.split()
	# and write it to text files
	with open('material.txt', 'w') as f:
		f.write('{}'.format(foodMaterial))

# asking about herbs
def herbsMaterial():
	print("Second, what kind of herbs do you have in the kitchen?")

	herbsMaterial = str(input(" "))

	characters = "1234567890$'\\'!@#$%^&*()[]'|?></,.:;"''
	for elem in herbsMaterial:
		if elem in characters:
			herbsMaterial = herbsMaterial.replace(elem, '')

	herbsMaterial = herbsMaterial.split()
	with open('herbs.txt', 'w') as f:
		f.write('{}'.format(herbsMaterial))

# asking about sauce
def sauceMaterial():
	print("Last thing, what kind of sauce in your cupboard?")

	sauceMaterial = str(input(" "))

	characters = "1234567890$'\\'!@#$%^&*()[]'|?></,.:;"''
	for elem in sauceMaterial:
		if elem in characters:
			sauceMaterial = sauceMaterial.replace(elem, '')

	sauceMaterial = sauceMaterial.split()
	with open('sauce.txt', 'w') as f:
		f.write('{}'.format(sauceMaterial))


def foodInformation():
	print("So you have them all in the kitchen. Superb!")

	# read file from the food material
	materialText = open(("material.txt"), "r")
	herbsText = open(("herbs.txt"), "r")
	sauceText = open(("sauce.txt"), "r")

	print(materialText.read())
	print(herbsText.read())
	print(sauceText.read())


foodMaterial()
herbsMaterial()
sauceMaterial()
foodInformation()


