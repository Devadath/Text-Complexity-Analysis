#!/usr/bin/env python3

import string

class SurfaceFeatureExractor():
	"""docstring for ClassName"""
	def __init__(self):
		pass


	def get_surface_features(self, sentences):

		total_number_of_chars, total_number_of_words,  total_number_of_sentences = 0, 0, len(sentences)

		surface_features = {}

		for sentence in sentences:

			words = sentence.split(" ")
			for word in words:
				if word in string.punctuation or word == "।":
					continue

				total_number_of_chars+=len(word)
				total_number_of_words+=1

		#print(surface_features, "started")
		surface_features["text_length"] = float(total_number_of_words)
		surface_features["average_number_of_characters_per_word"] = float(total_number_of_chars/total_number_of_words)
		surface_features["average_number_of_words_per_sentence"] =  float(total_number_of_words/total_number_of_sentences)
		#print(surface_features, "ended")
		return surface_features

if __name__ == '__main__':
	n = SurfaceFeatureExractor()

