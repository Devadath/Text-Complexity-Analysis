#!/usr/bin/env python3

from src.surface_features_extraction import SurfaceFeatureExractor
from src.syntactic_feature_extraction import SyntacticFeatureExtractor

class FeatureExtractor(object):
	
	def __init__(self, arg):
		self.nlp = arg
		self.surf_feats = SurfaceFeatureExractor()
		self.synt_features = SyntacticFeatureExtractor(self.nlp)

	def featurise(self, texts, language):
		features_of_text = self.surf_feats.get_surface_features(texts)
		np, vp, pron, conj  = self.synt_features.get_syntactic_and_discourse_features_for_english(texts, language)
		features_of_text["number_of_noun_phrases"] = np
		features_of_text["number_of_verb_phrases"] = vp
		features_of_text["number_of_pronouns"] = pron
		features_of_text["number_of_discourse_markers"] = conj
		return features_of_text	







