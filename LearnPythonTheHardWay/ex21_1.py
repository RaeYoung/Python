def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age, %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

result1 = divide(iq, 2)
result2 = multiply(weight, result1)
result3 = subtract(height, result2)
result4 = add(age, result3)

print "That becomes: ", result4

print "What's the result of [5 + (5 * 11 - 31) / (12 / 3)]?"

result = add(5, divide(subtract(multiply(5, 11), 31), divide(12, 4)))

print "Here's the result: ", result
