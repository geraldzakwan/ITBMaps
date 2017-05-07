def createVertex(upperbackleft_x, upperbackleft_y, upperbackleft_z, upperbackright_x, upperbackright_y, upperbackright_z, upperfrontleft_x, upperfrontleft_y, upperfrontleft_z, upperfrontright_x, upperfrontright_y, upperfrontright_z, underbackleft_x, underbackleft_y, underbackleft_z, underbackright_x, underbackright_y, underbackright_z, underfrontleft_x, underfrontleft_y, underfrontleft_z, underfrontright_x, underfrontright_y, underfrontright_z):
	vertex = []
	#TR1 (left side)
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)
	vertex.append(underfrontleft_x)
	vertex.append(underfrontleft_y)
	vertex.append(underfrontleft_z)
	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)
	
	#TR2 (Backside)
	vertex.append(upperbackright_x)
	vertex.append(upperbackright_y)
	vertex.append(upperbackright_z)
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)
	vertex.append(upperbackleft_x)
	vertex.append(upperbackleft_y)
	vertex.append(upperbackleft_z)
	
	#TR3 (under side)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)
	vertex.append(underbackright_x)
	vertex.append(underbackright_y)
	vertex.append(underbackright_z)
	
	#TR4 (back side)
	vertex.append(upperbackright_x)
	vertex.append(upperbackright_y)
	vertex.append(upperbackright_z)
	vertex.append(underbackright_x)
	vertex.append(underbackright_y)
	vertex.append(underbackright_z)
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)
	
	# TR5 (backside)
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)
	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)
	vertex.append(upperbackleft_x)
	vertex.append(upperbackleft_y)
	vertex.append(upperbackleft_z)
	
	#TR6 (under side)
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)
	vertex.append(underfrontleft_x)
	vertex.append(underfrontleft_y)
	vertex.append(underfrontleft_z)

	#TR7 (front side)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)
	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)
	vertex.append(underfrontleft_x)
	vertex.append(underfrontleft_y)
	vertex.append(underfrontleft_z)
	
	#TR8 (right side)
	vertex.append(upperfrontright_x)
	vertex.append(upperfrontright_y)
	vertex.append(upperfrontright_z)
	vertex.append(underbackright_x)
	vertex.append(underbackright_y)
	vertex.append(underbackright_z)
	vertex.append(upperbackright_x)
	vertex.append(upperbackright_y)
	vertex.append(upperbackright_z)

	#TR9 (right side)
	vertex.append(underbackright_x)
	vertex.append(underbackright_y)
	vertex.append(underbackright_z)
	vertex.append(upperfrontright_x)
	vertex.append(upperfrontright_y)
	vertex.append(upperfrontright_z)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)
	
	#TR10 (upper side)
	vertex.append(upperfrontright_x)
	vertex.append(upperfrontright_y)
	vertex.append(upperfrontright_z)
	vertex.append(upperbackright_x)
	vertex.append(upperbackright_y)
	vertex.append(upperbackright_z)
	vertex.append(upperbackleft_x)
	vertex.append(upperbackleft_y)
	vertex.append(upperbackleft_z)
	
	#TR11 (upper side)
	vertex.append(upperfrontright_x)
	vertex.append(upperfrontright_y)
	vertex.append(upperfrontright_z)
	vertex.append(upperbackleft_x)
	vertex.append(upperbackleft_y)
	vertex.append(upperbackleft_z)
	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)

	#TR12
	vertex.append(upperfrontright_x)
	vertex.append(upperfrontright_y)
	vertex.append(upperfrontright_z)
	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)	

	return vertex

# def createBuilding(underbackleft_x, underbackleft_y, underbackleft_z, underbackright_x, underbackright_y, underbackright_z, underfrontleft_x, underfrontleft_y, underfrontleft_z, underfrontright_x, underfrontright_y, underfrontright_z):
def createBuilding(underbackright_x, underbackright_y, underbackright_z, underbackleft_x, underbackleft_y, underbackleft_z, underfrontleft_x, underfrontleft_y, underfrontleft_z, underfrontright_x, underfrontright_y, underfrontright_z):
	tinggi = 0.5
	upperbackleft_x = underbackleft_x
	upperbackleft_y = underbackleft_y
	upperbackleft_z = underbackleft_z + tinggi

	upperbackright_x = underbackright_x
	upperbackright_y = underbackright_y
	upperbackright_z = underbackright_z + tinggi

	upperfrontright_x = underfrontright_x
	upperfrontright_y = underfrontright_y
	upperfrontright_z = underfrontright_z + tinggi

	upperfrontleft_x = underfrontleft_x
	upperfrontleft_y = underfrontleft_y
	upperfrontleft_z = underfrontleft_z + tinggi

	return createVertex(upperbackleft_x, upperbackleft_y, upperbackleft_z, upperbackright_x, upperbackright_y, upperbackright_z, upperfrontleft_x, upperfrontleft_y, upperfrontleft_z, upperfrontright_x, upperfrontright_y, upperfrontright_z, underbackleft_x, underbackleft_y, underbackleft_z, underbackright_x, underbackright_y, underbackright_z, underfrontleft_x, underfrontleft_y, underfrontleft_z, underfrontright_x, underfrontright_y, underfrontright_z)
