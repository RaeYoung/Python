# -*- coding: utf-8 -*-
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
		"创建一个叫%%%的类，是%%%的一种。",
	"class %%%(Object):\n\tdef __init__(self, @@@)":
		"类%%%有一个__init__接受self和@@@作为参数。",
	"class %%%(Object):\n\tdef ***(self, @@@)":
		"类%%%有一个函数名为***，它接受self和@@@作为参数。",
	"*** = %%%()":
		"将***设为类%%%的一个实例。",
	"***.***(@@@)":
		"从***中找到***函数，并使用self和@@@参数调用。",
	"***.*** = '***'":
		"从***中获取***属性，并将其设为'***'"
}

PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST = True

for line in urlopen(WORD_URL).readlines():
	WORDS.append(line.strip())

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	param_names = []
	results = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(", ".join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		for word in class_names:
			result = result.replace("%%%", word, 1)

		for word in other_names:
			result = result.replace("***", word, 1)

		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)
	return results


try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]

			question, answer = convert(snippet, phrase)
			if PHRASES_FIRST:
				answer, question = question, answer

			print question
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer

except EOFError:
	print "\nBye"

