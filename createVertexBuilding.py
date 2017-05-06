def createVertex(upperbackleft_x, upperbackleft_y, upperbackleft_z, upperbackright_x, upperbackright_y, upperbackright_z, upperfrontleft_x, upperfrontleft_y, upperfrontleft_z, upperfrontright_x, upperfrontright_y, upperfrontright_z, underbackleft_x, underbackleft_y, underbackleft_z, underbackright_x, underbackright_y, underbackright_z, underfrontleft_x, underfrontleft_y, underfrontleft_z, underfrontright_x, underfrontright_y, underfrontright_z):
	vertex = []
	# Left Side
	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)
	vertex.append(upperbackleft_x)
	vertex.append(upperbackleft_y)
	vertex.append(upperbackleft_z)
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)

	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)
	vertex.append(underfrontleft_x)
	vertex.append(underfrontleft_y)
	vertex.append(underfrontleft_z)

	# Front Side
	vertex.append(upperfrontright_x)
	vertex.append(upperfrontright_y)
	vertex.append(upperfrontright_z)
	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)
	vertex.append(underfrontleft_x)
	vertex.append(underfrontleft_y)
	vertex.append(underfrontleft_z)

	vertex.append(upperfrontright_x)
	vertex.append(upperfrontright_y)
	vertex.append(upperfrontright_z)
	vertex.append(underfrontleft_x)
	vertex.append(underfrontleft_y)
	vertex.append(underfrontleft_z)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)

	# Right Side
	vertex.append(upperbackright_x)
	vertex.append(upperbackright_y)
	vertex.append(upperbackright_z)
	vertex.append(upperfrontright_x)
	vertex.append(upperfrontright_y)
	vertex.append(upperfrontright_z)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)

	vertex.append(upperbackright_x)
	vertex.append(upperbackright_y)
	vertex.append(upperbackright_z)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)
	vertex.append(underbackright_x)
	vertex.append(underbackright_y)
	vertex.append(underbackright_z)

	# Back Side
	vertex.append(upperbackleft_x)
	vertex.append(upperbackleft_y)
	vertex.append(upperbackleft_z)
	vertex.append(upperbackright_x)
	vertex.append(upperbackright_y)
	vertex.append(upperbackright_z)
	vertex.append(underbackright_x)
	vertex.append(underbackright_y)
	vertex.append(underbackright_z)

	vertex.append(upperbackleft_x)
	vertex.append(upperbackleft_y)
	vertex.append(upperbackleft_z)
	vertex.append(underbackright_x)
	vertex.append(underbackright_y)
	vertex.append(underbackright_z)
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)

	# Upper Side
	vertex.append(upperbackright_x)
	vertex.append(upperbackright_y)
	vertex.append(upperbackright_z)
	vertex.append(upperbackleft_x)
	vertex.append(upperbackleft_y)
	vertex.append(upperbackleft_z)
	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)

	vertex.append(upperbackright_x)
	vertex.append(upperbackright_y)
	vertex.append(upperbackright_z)
	vertex.append(upperfrontleft_x)
	vertex.append(upperfrontleft_y)
	vertex.append(upperfrontleft_z)
	vertex.append(upperfrontright_x)
	vertex.append(upperfrontright_y)
	vertex.append(upperfrontright_z)

	# Under Side
	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)
	vertex.append(underbackright_x)
	vertex.append(underbackright_y)
	vertex.append(underbackright_z)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)

	vertex.append(underbackleft_x)
	vertex.append(underbackleft_y)
	vertex.append(underbackleft_z)
	vertex.append(underfrontright_x)
	vertex.append(underfrontright_y)
	vertex.append(underfrontright_z)
	vertex.append(underfrontleft_x)
	vertex.append(underfrontleft_y)
	vertex.append(underfrontleft_z)

	return vertex

def createBuilding(underbackleft_x, underbackleft_y, underbackleft_z, underbackright_x, underbackright_y, underbackright_z, underfrontleft_x, underfrontleft_y, underfrontleft_z, underfrontright_x, underfrontright_y, underfrontright_z)
	tinggi = 5
	upperbackleft_x = underbackleft_x[2] + tinggi
	upperbackleft_y = underbackleft_y[2] + tinggi
	upperbackleft_z = underbackleft_z[2] + tinggi

	upperbackright_x = underbackright_x[2] + tinggi
	upperbackright_y = underbackright_y[2] + tinggi
	upperbackright_z = underbackright_z[2] + tinggi

	upperfrontright_x = underfrontright_x[2] + tinggi
	upperfrontright_y = underfrontright_y[2] + tinggi
	upperfrontright_z = underfrontright_z[2] + tinggi

	upperfrontleft_x = underfront_left_x[2] + tinggi
	upperfrontleft_y = underfront_left_y[2] + tinggi
	upperfrontleft_z = underfront_left_z[2] + tinggi

	return createVertex(upperbackleft_x, upperbackleft_y, upperbackleft_z, upperbackright_x, upperbackright_y, upperbackright_z, upperfrontleft_x, upperfrontleft_y, upperfrontleft_z, upperfrontright_x, upperfrontright_y, upperfrontright_z, underbackleft_x, underbackleft_y, underbackleft_z, underbackright_x, underbackright_y, underbackright_z, underfrontleft_x, underfrontleft_y, underfrontleft_z, underfrontright_x, underfrontright_y, underfrontright_z)
