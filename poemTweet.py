
from __future__ import print_function
import twitter
import nltk
from operator import itemgetter
from nltk.corpus import wordnet as wn
import random

CONSUMER_KEY = 'tUx3gDmkwV2MIOteqhCPJ8nQL'
CONSUMER_SECRET = 'ceVcWk5sLfjz0np9sF2YlUoJiBT4cB4WmsqrSbi9EHChp3CA8O'
ACCESS_TOKEN = '838614187135942657-oKlOQzBPuX3jOyiwACrgbvRSxZAukMI'
ACCESS_TOKEN_SECRET = 'HBYIG9kvgCr2Tb2SkPFfma0bzkfI9OAimsH3FVcqdF17X'

username = "realDonaldTrump"
tweet_count = 1

# create an API instance
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

# check credentials 
# print(api.VerifyCredentials())

# get and print all friends
# users = api.GetFriends()
# print([u.screen_name for u in users]) 

# get user's statuses
# tweet = api.GetUserTimeline(screen_name=username, count=tweet_count)
# tweet = tweet[0]
# tweet = tweet.text
# print(tweet)

tweet = "Just heard Fake News CNN is doing polls again despite the fact that their election polls were a WAY OFF disaster. Much higher ratings at Fox"

def topWordsCount(statuses):
	badwords = ""

	for s in statuses: 
		badwords += ' %s' % s.text
	# normalize text for cases etc.
	# make badwords an nltk text
	toks = nltk.word_tokenize(badwords)

	wc = {}
	for tok in toks:
		if tok not in wc.keys():
			wc[tok] = 1
		else:
			wc[tok] += 1

	print(sorted(wc.items(), key=itemgetter(1)))

#badText = nltk.Text(toks)


# # make the list of words you're interested in
words_list = ['America', 'sad','tremendous','pathetic']

def lexicalDispersion(wordsList, badText):
	badText.dispersion_plot(words_list)

# This function will build a truly great poem 
# one which will be garbled and 
# incomprehensible but 
# with a deference to words
def tremendousPoem(status):
	tremendousPoem = ""
	tokens = nltk.word_tokenize(status)
	partsOfSpeech = nltk.pos_tag(tokens)

	for ps in partsOfSpeech:
		# if it is a noun or a verb find a better one
		if ps[1] == "JJ" or ps[1] == "VB":
			synonyms = []
			antonyms = []

			for syn in wn.synsets(ps[0]):
				for l in syn.lemmas():
					synonyms.append(l.name())
					if l.antonyms():
						antonyms.append(l.antonyms()[0].name())
	
			if synonyms:
				tremendousPoem = tremendousPoem + " " + (random.choice(synonyms))
			if antonyms: 
				tremendousPoem = tremendousPoem + " " + (random.choice(antonyms))

		#elif ps[1] == "NN" or ps[1] == "NNP":
			#tremendousPoem = tremendousPoem + " " + ps[0]

	tremendousPoem = tremendousPoem[:140]
	tremendousPoem.capitalize()
	return tremendousPoem

# Here is a function meant as education 
# which will define words 
# but keep proper nouns 
# so things still feel disorienting
def educationPoem(status):
	knowledgePoem = ""
	tokens = nltk.word_tokenize(status)
	partsOfSpeech = nltk.pos_tag(tokens)
	
	defineList = []

	for ps in partsOfSpeech: 
		if ps[1] == "JJ" or ps[1] == "VB" or ps[1] == "NN":
			defineList.append(ps[0])
		if ps[1] == "NNP": 
			knowledgePoem = knowledgePoem + " " + ps[0]

	if defineList:
		entropyWord = ""
		while not wn.synsets(entropyWord): 
			entropyWord = random.choice(defineList)
		
		synsEntropy = wn.synsets(entropyWord)
		defEntropy = synsEntropy[0].definition()

		knowledgePoem = knowledgePoem + " " + defEntropy
		knowledgePoem = knowledgePoem[:140]
	
	knowledgePoem.capitalize()
	return knowledgePoem

api.PostUpdate(tremendousPoem(tweet))
api.PostUpdate(educationPoem(tweet))


# syns = wn.synsets('some word')
# print(syns[0].definition())
# print(syns[0].examples())

# synonyms = wn.synsets('marvelous')
# print(synonyms)

# good = wn.synset('good.a.01')
# print(good.lemmas()[0].antonyms())

# tokens = nltk.word_tokenize(status)

# print(tokens)

# TEXT FILES FOR LATER
# does concordance
# text1.similar("monstrous")
# lexical dispersion
# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# for s in statuses:
# 	api.PostUpdate("I'm beans. " + s.text)


