# -*- coding: utf-8 -*-

from sys import exit

def birds_room():
	print "Hello, You are in BIRDS room NOW."
	print "Here are dozens of birds flying in the room."
	print "You choose to \"chase them away\" or \"give them food\" or \"leave the room\"?" 

	next = raw_input(">  ")

	if "chase" in next:
		dead("Oh no, birds are angry so they attck you together, so you died.")
	elif "food" in next:
		win("Congratulations, you win!")
	elif "leave" in next:
		room_choose()
	else:
		birds_room()

# def fire_room():

def boss_room():
	global winCount
	if (winCount < 3):
		print "Sorry, you can't come into the boss room right now."
		print "You must win the three rooms first!"
	else:
		print "Oh, you are in the Boss room."

def dead(why):
	print why
	exit(0)

def win(why):
	global winCount
	file = open("count.txt", "w")
	file.seek(0)
	file.write(str(winCount+1))
	file.close()
	print why
	print "Then you choose \"continue the game and go to other rooms\" or \"just leave this game\"."

	next = raw_input(">  ")
	if "continue" in next:
		room_choose()
	elif "leave" in next:
		print "Ok, We hope you can come back soon."
		exit(0)
	else:
		win("Input wrong, please make your choice again!")

def room_choose():
	global winCount
	print "There are three mysterious rooms, which one do you wanna come into? "
	print "Please input '1', '2' or '3' or 'boss room'."
	file = open("count.txt", "r+")
	winCount = int(file.read())
	file.close()

	next = raw_input(">  ")

	if next == "1":
		birds_room()
	elif next == "2":
		fire_room()
	elif "boss" in next:
		boss_room()
	else:
		room_choose()

# 询问是否将纪录清零
def start():
	print "Would you want to restart your game(winCount reset to 0)?"
	print "Please input 1(yes) or 2(no)."
	next = raw_input(">  ")

	if next == "1":
		file = open("count.txt", "w")
		file.seek(0)
		file.write('0')
		file.close()
		return
	elif next == "2":
		return
	else:
		start()

print "Welcome to this game"
winCount = 0
start()
room_choose()