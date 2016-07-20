# -*- coding: utf-8 -*-
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
		"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

# load up the words from the website
# urlopen 从指定的URL地址获取网页数据然后对其进行分析
for word in urlopen(WORD_URL).readlines():
	# word.strip() 删除字符串开头结尾处的空白符，（包括‘\n','\t','\r',' ')
	WORDS.append(word.strip())

def convert(snippet, phrase):
	# random.sample(seq, n) 从列表seq中选择n个随机且独立的元素返回，原列表不变
	# snippet.count("％％％") 返回snippet字符串“％％％”的个数
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	#  若snippet里有"@@@",则生成1到3个参数
	for i in range(0, snippet.count("@@@")):
		# random.randint(a,b) 生成的随机数n: a<=n<=b
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		# param_names只有一个字符串元素

	for sentence in snippet, phrase:
		# 拷贝sentence
		result = sentence[:]

		# fake class names
		for word in class_names:
			# str.replace(old, new[, max]) max为每次最多替换次数，可选值
			# 返回以new代替old字符串不超过max次的新字符串
			result = result.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		#fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)
	return results

# keep going until they hit CTRL-D
try:
	while True:
		# snippets 为 PHRASES字典返回的所有key组成的列表，之后将其打乱重拍序
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			# question为snippet处理后的结果，answer为phrase处理后的结果
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print question

			raw_input("> ")
			print "ANSWER: %s\n\n" % answer

except EOFError:
	print "\nBye"