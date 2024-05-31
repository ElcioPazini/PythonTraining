# -*- coding:utf-8 -*-
import random
# Here we provide the flower options that we want (in my case, I also inserted my keyboard number related to them)
flowerNames = ["Cherry sap(1)", "Rose(2)", "Pink bush(3)", "Yellow flower(4)", "White flower(5)", "Lily of the valley (6)", "Blue flower (7)", "Pink flower (8)"]

# This method return randoms flowers based on the number of tiles in our flowerbed
# The "repeatFlowers" parameter is used to determine whether repeated flowers should be included or not in the same flowerbed
def getAllFlowersRandomized(numberOfTiles, repeatFlowers):
	count = 0
	selectedFlowers = []

	for count in range(numberOfTiles):
		selectedFlower = getSingleRandomFlowerName()
		while (selectedFlower in selectedFlowers and not repeatFlowers):
			selectedFlower = getSingleRandomFlowerName()

		selectedFlowers.append(selectedFlower)
		count = count + 1

	return selectedFlowers

# This method just retrieve a random object of our flowers list
def getSingleRandomFlowerName():
	return flowerNames[random.randint(0,7)];


print(getAllFlowersRandomized(3, False))
