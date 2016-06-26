# -*- coding: utf-8 -*-

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# dict是无序的，想要有序的dict, 可使用collections.OrderedDict
# from collections import OrderedDict
# od = OrderedDict([('Oregon', 'OR'), ('Florida', 'FL')])

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
# items() return a copy of the dictionary's list of (state, abbrev) pairs
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
# get() return the value for key('Texas') if key is in the dictionary
# else default(None), If default is not given, then it defaults to None.
state = states.get('Texas', None)

print 'Oregon' in states

# None, False, '', [], {}, () equals False
if not state:
	print "Sorry, no Texas."

# get a city with a default value
# if 'TX' is not in the dictionary, then return 'Does Not Exist'
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city