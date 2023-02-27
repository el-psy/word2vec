
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
import os
import json
from utils import getlogger

log_config = '../log/log_config.json'
logger = getlogger(log_config)

def wiki_path(wiki_path):
	# print(list(os.walk(wiki_path)))
	res = []
	for root, dirs, files in os.walk(wiki_path):
		for file in files:
			path = os.path.join(root, file)
			
			if(len(res)>=1): break
			res.append(path)
	return res

def load_wiki(path):
	res = []
	with open(path, 'r', encoding='utf-8') as f:
		for line in f.readlines():
			buff = json.loads(line)
			for sen in get_sen(buff['text']):
				res.append(sen)
	return res

def count(sens, save_buff):
	for sen in sens:
		for letter in sen:
			save_buff[letter] = save_buff.get(letter, 0) + 1
	return save_buff

def count_unk(min_count, count_buff):
	letter_trans = {}
	for letter in count_buff.keys():
		if count_buff[letter] < min_count:
			letter_trans[letter] = 'unk'
		else: letter_trans[letter] = letter
	return letter_trans

def sen_unk(sens, letter_trans):
	res = []
	for sen in sens:
		res.append([letter_trans[i] for i in sen])
	return res

def corpus_sen_save(path, sens):
	with open(path, 'a', encoding='utf-8') as f:
		for sen in sens:
			s = ' '.join(sen) + '\n'
			f.write(s)

def get_sen(letters):
	res = []
	# with open(path, 'r', encoding='utf-8') as f:
	# 	data = f.read()
	buff = ''
	for letter in letters:
		buff = buff + letter
		if letter in ['\n', '。','？', '！', '?', '!']:
			buff = buff.replace('\n', '')
			if(len(buff)>0):
				res.append(list(buff))
				
	# print(data)
	return res

def train(path):
	sens = LineSentence(path)
	model = word2vec.Word2Vec(sentences = sens, vector_size = 128, hs = 1, min_count = 5, window = 5, workers = 12, epochs=1)
	# model.train(sens)
	model.wv.save_word2vec_format('word2vec.txt',binary=False)
	# buff = model.similarity('新', '旧')
	# indexer = AnnoyIndexer(model, 2)
	# res = model.wv.most_similar('新', topn = 2, indexer = indexer)
	# print(res)
	# print(model)

def core():
	paths = wiki_path('../wiki_zh')
	logger.info('path length: '+str(len(paths)))
	count_save = {}
	for index, path in enumerate(paths):
		logger.info('count index: '+str(index)+' path: '+path)
		sens = load_wiki(path)
		count_save = count(sens, count_save)
		del(sens)
	with open('count.json', 'w', encoding='utf-8') as f:
		json.dump(count_save, f, indent=4, ensure_ascii=False)
	letter_trans = count_unk(40, count_save)
	for index, path in enumerate(paths):
		logger.info('save index: '+str(index)+' path: '+path)
		sens = load_wiki(path)
		sens = sen_unk(sens, letter_trans)
		corpus_sen_save('./corpus.txt', sens)
		del(sens)

def load(path):
	res = []
	id_2_letter = {}
	letter_2_id = {}
	with open(path, 'r', encoding='utf-8') as f:
		for line in f.readlines():
			buff = line.strip().split(' ')
			if(len(buff) == 2):
				continue
			letter = buff[0]
			vec = buff[1:]
			res.append(vec)
			id_2_letter[len(res)-1] = letter
			letter_2_id[letter] = len(res)-1
	return res, id_2_letter, letter_2_id

if __name__ == '__main__':
	# sens = get_sen('vocab.txt')
	# print(sens)
	# train(sens)
	# core()
	# train('./corpus.txt')

	# res, id_2_letter, letter_2_id = load('./word2vec.txt')
	# print(letter_2_id)
	pass