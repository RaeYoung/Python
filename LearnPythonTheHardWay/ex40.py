class Song(object):
	def __init__(self, lyrics, singer):
		self.lyrics = lyrics
		self.singer = singer

	def sing_me_a_song(self):
		for line_lyric in self.lyrics:
			print line_lyric

	def add_singer(self, singer):
		if not self.singer:
			self.singer = singer
			print "Adding singer: %s" % self.singer


happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"], "Louis")

bulls_on_parade = Song(["They rally around the family",
	                    "With pockets full of shells"], None)

rainball = Song(["Where is the rainball",
				 "shiny and beautiful rainball"], "Jay Chou")

my_lyrics = ["Hello there", "I love you but you don't know"]
my_singer = "JJ"
love = Song(my_lyrics, my_singer)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

rainball.sing_me_a_song()

love.sing_me_a_song()

bulls_on_parade.add_singer("Lady Gaga")