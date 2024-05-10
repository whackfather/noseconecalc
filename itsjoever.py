# Nosecone Calculator
# v0.1
# Written by Roman Rodriguez

from math import *

shape = input("Enter shape name: ")
rad_o = float(input("Enter radius (INCHES ONLY): "))
lng_o = rad_o * 10
length = 0

if shape == "conic" or shape == "cn":
	print("0,0")
	while True:
		length += 0.1
		if length > lng_o:
			break
		radius = ((length * rad_o) / lng_o)
		print(str(round(length, 3)) + "," + str(round(radius, 3)))
elif shape == "parabolic" or shape == "pb":
	k = float(input("K-value: "))
	print("0,0")
	while True:
		length += 0.1
		if length > lng_o:
			break
		radius = rad_o * (((2 * (length / lng_o)) - (k * ((length / lng_o) ** 2))) / (2 - k))
		print(str(round(length, 3)) + "," + str(round(radius, 5)))
elif shape == "haack" or shape == "hs":
	series_type = input("C-value (vk, lv, tng): ")
	if series_type == "vk":
		c = 0
	elif series_type == "lv":
		c = 1 / 3
	elif series_type == "tng":
		c = 2 / 3
	print("0,0")
	while True:
		length += 0.1
		if length > lng_o:
			break
		theta = acos(1 - ((2 * length) / lng_o))
		radius = (rad_o / sqrt(pi)) * (sqrt(theta - ((sin(2 * theta)) / 2) + (c * ((sin(theta)) ** 3))))
		print(str(round(length, 3)) + "," + str(round(radius, 5)))
elif shape == "power" or shape == "ps":
	n = float(input("N-value: "))
	print("0,0")
	while True:
		length += 0.1
		if length > lng_o:
			break
		radius = rad_o * ((length / lng_o) ** n)
		print(str(round(length, 3)) + "," + str(round(radius, 5)))
