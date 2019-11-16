import numpy as np 
from nltk.corpus import stopwords
import re
import scipy
import random


def load_model():
	with open('static/glove.6B.50d.txt') as f:
		content=f.readlines()
	model={}
	for line in content:
		splitLine=line.split()
		word=splitLine[0]
		embedding = np.array([float(val) for val in splitLine[1:]])
		model[word]=embedding

	return model


def preprocess(text):
	# keep only words
    letters_only_text = re.sub("[^a-zA-Z]", " ", text)

    # convert to lower case and split 
    words = letters_only_text.lower().split()

    # remove stopwords
    stopword_set = set(stopwords.words("english"))
    cleaned_words = list(set([w for w in words if w not in stopword_set]))

    return cleaned_words


def cosine_distance_between_two_words(word1, word2):
    return (1- scipy.spatial.distance.cosine(model[word1], model[word2]))


def cosine_distance_wordembedding_method(s1, s2,model):
    vector_1 = np.mean([model[word] for word in preprocess(s1)],axis=0)
    vector_2 = np.mean([model[word] for word in preprocess(s2)],axis=0)
    cosine = scipy.spatial.distance.cosine(vector_1, vector_2)
    #print('Our two sentences are similar to',round((1-cosine)*100,2),'%')
    return round((1-cosine)*100,2)


def load_def(ques_no):
	with open('static/Def/ques_no_'+ str(ques_no) +'.txt') as file:
		content=file.readlines()
	#with open('../static/Def/ques_no_'+ str(ques_no) + '_wrong' +'.txt') as file:
#		content_wrong=file.readlines()

	return content

def correctness(ans,ques_no,pc):
	model = load_model()
	content = load_def(ques_no)

	sum_avg_correct=0
	for ss in content:
		#print(content)
		temp=cosine_distance_wordembedding_method(ss,ans,model)
		if temp>=95:
			if pc>2:
				return temp-(pc-2)*5
			else:
				return temp
		sum_avg_correct+=temp

	sum_avg_correct/=len(content)

	if pc>2:
		pc-=2
	if sum_avg_correct>=80:
		return int(sum_avg_correct)-pc*3
	elif sum_avg_correct<50:
		return 0
	else:
		return 50 + random.randint(0,30) - pc*2




