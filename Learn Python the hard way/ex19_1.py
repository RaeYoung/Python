def students(female, male):
	print "Here are %d girls, %d boys in our school" % (female, male)

girls = raw_input("How many girls? ")
boys = raw_input("How many boys? ")
students(int(girls), int(boys))

students(300, 200)

girls_now = 200
boys_now = 300
newStudents_girl = 50
newStudents_boy = 80
students(girls_now + newStudents_girl, boys_now + newStudents_boy)

students(200 + 180, 500 + 200)