#!/usr/bin/env python3
import re
import pandas as pd
import numpy as np
import string
import pickle
from src.utils import get_tokenized_sentences
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from src.feature_extraction import FeatureExtractor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_validate
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
import argparse
import spacy

class TextComplexityClassifier(object):
	"""
	Trains a classifier for reading leveels in stories and  returns metrics of the text complexity.
	"""

	def __init__(self):
		nlp = spacy.load("en_core_web_sm")
		self.feature_extractor = FeatureExtractor(nlp)
		self.vectoriser =  DictVectorizer()

	def parse_args(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('--language', default='english', type=str)
		args = parser.parse_args()
		print("args are ---", args)
		return args

	def data_from_args(self, args):
		if 'english' == args.language:
			train_file = pd.read_csv("./data/english.csv")
		elif 'hindi' == args.language:
			train_file = pd.read_csv("./data/hindi.csv")
		elif "telugu" == args.language:
			train_file = pd.read_csv("./data/telugu.csv")

		return train_file

	def train(self, args):

		print("started.......")

		#Collecting training data
		train_file = self.data_from_args(args)

		#Collecting the content to be trained
		train_datas = train_file['content']

		#Preparing Train arget labels for classification
		labels = LabelEncoder()
		train_target = labels.fit_transform(train_file['reading_level_updated'].values.astype('U'))

		#featurising		
		featurised_train = self.clean_and_featurise(train_datas, args.language)

		#Defining classification model
		clf = RandomForestClassifier(n_estimators=300, max_depth=4, random_state=0, class_weight="balanced")

		#Scores to be calculated 
		scoring = ['precision_macro', 'recall_macro', 'accuracy', 'f1_macro']

		#5 fold cross validation
		scores = cross_validate(clf, featurised_train, train_target, scoring=scoring, cv=5)


		clf.fit(featurised_train, train_target)

		#Printing the average scores after 5-fold cross validation
		score_metrics = ['test_precision_macro', 'test_precision_micro', 'test_recall_macro', 'test_accuracy', 'test_f1_macro', 'test_f1_micro',  'test_recall_micro']

		for score in scores:
			if score in score_metrics:
				print(score + ": ", np.mean(scores[score]))

		#Printing important features
		feat_labels = ["text_length", "average_number_of_characters_per_word", "average_number_of_words_per_sentence", "number_of_verb_phrases", "number_of_noun_phrases", "number_of_pronouns", "number_of_discourse_markers"]
		
		for feature in zip(feat_labels, clf.feature_importances_):
			print(feature)


		#Saving the model
		#file = open(self.output_filename,'wb')
		#pickle.dump(clf,file)
		#file.close()

	def clean_and_featurise(self, dataFrame, language):
		"""
		Tokenises and get the features as a dictionary.
		"""
		texts = dataFrame.tolist()
		feature_list = []
		for id, text in enumerate(texts):
			sentences = get_tokenized_sentences(text, language)
			surface_features_of_text = self.feature_extractor.featurise(sentences, language)
			feature_list.append(surface_features_of_text)
		return self.vectoriser.fit_transform(feature_list)


if __name__ == "__main__":
        trainer = TextComplexityClassifier()
        args = trainer.parse_args()
        trainer.train(args)
        