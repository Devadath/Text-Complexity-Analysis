#!/usr/bin/env python3

class SyntacticFeatureExtractor(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.nlp = arg
		self.english_pronouns = ["I", "you", "he", "she", "it", "they", "me", "you", "him", "her", "it", "my", "mine", "your", "yours", "his", "her", "hers", "its", "who", "whom", "whose", "what", "which", "another", "each", "everything", "nobody", "either", "someone", "who", "whom", "whose", "that", "which", "myself", "yourself", "himself", "herself", "itself", "this", "that"]
		self.hindi_pronouns = ["मैं ", "हम", "तू ", "तुम", "आप ", "आप", "यह", "ये", "वह ", "वे ", "मुझे", " मुझको", "हमें", "हमको", "तुझे", "तुझको", "तुम्हें", "तुमको", "आपको", "आपको", "इसे", " इसको", "इन्हें", "इनको", "उसे उसको", "उन्हें उनको", "मेरा", "मेरी", "हमारा", "हमारी ", "तेरा", "तेरी", "तुम्हारा", "तुम्हारी", "आपका", "आपकी", "आपका", "आपकी", "इसका", "इसकी", "इनका ", "इनकी ", "उसका ", "उसकी ", "उनका ", "उनकी"]
		self.telugu_pronouns = ["అతని", "అతనికి", "అతను", "అతన్ని", "అది", "అదే", "అవి", "అందరమూ", "అందరికీ", "అందరినీ", "అందరూ", "అందరం", "ఆమె", "ఆమెకి", "ఆమెకు", "ఆమెను", "ఆయన", "ఆయనకి", "ఆయనకు", "ఆయనా", "ఆయన్ని", "ఆవిడ", "ఆవిడకు", "ఇక్కడినుంచి", "ఇడుగోనండి", "ఇతను", "ఇతనే", "ఇతనేనా", "ఇది", "ఇదీ", "ఇదంతా", "ఇద్దరూ", "ఇవి", "ఈమె", "ఎక్కడికి", "ఎప్పుడోయ్", "ఎవడు", "ఎవణ్ణి", "ఎవతె", "ఎవరి", "ఎవరికి", "ఎవరికీ", "ఎవరితోనో", "ఎవరిదగ్గిరికి", "ఎవరిదో", "ఎవరిని", "ఎవరినీ", "ఎవరినో", "ఎవరు", "ఎవరూ", "ఎవరెవరు", "ఎవరైతే", "ఎవరో", "ఎంత", "ఎంతో", "ఎందరో", "ఎందుకయ్యా", "ఎందుకో", "ఏడీ", "ఏది", "ఏదీ", "ఏదో", "ఏమర్రా", "ఏమి", "ఏమిటి", "ఏమిటో", "ఏమిటండి", "ఏమీ", "ఏమో", "ఏమండి", "ఏమండీ", "ఏమండోయ్", "ఏరీ", "ఏవి", "ఏవీ", "ఏవైతే", "ఏం", "ఒక్కర్తినీ", "ఒరేయ్", "ఒసేయ్", "కొన్ని", "కొందరు", "చిన్నవాడివి", "తన", "తనది", "తాను", "దాని", "దానితో", "దాంట్లో", "దేని", "దేనికి", "దేనిని", "నన్ను", "నా", "నాకు", "నాకంటే", "నాతో", "నాతోనే", "నాది", "నాదే", "నాలాగా", "నావైపు", "నిన్ను", "నీ", "నీకు", "నీతో", "నీవు", "నువ్వు", "నువ్వూ", "నేనన్నా", "నేనా", "నేను", "నేనూ", "నేనే", "నేనో", "పెద్దది", "పెద్దవాడు", "మన", "మనకు", "మనకేం", "మనము", "మనం", "మమ్మల్ని", "మా", "మాకా", "మాకు", "మాకూ", "మావాడు", "మావాళ్ళు", "మిమ్మలని", "మిమ్మల్ని", "మీ", "మీloo", "మీకా", "మీకు", "మీతో", "మీరన్నా", "మీరా", "మీరు", "మీరూ", "మీరో", "మేము", "మేం", "మంచివాడు", "రాము", "వాటి", "వాడా", "వాడి", "వాడికి", "వాడికీ", "వాడితో", "వాడివి", "వాడు", "వాడుగా", "వాడే", "వాడేటలే", "వాణ్ణి", "వారి", "వారిది", "వారిని", "వారు", "వాళ్ళ", "వాళ్ళకి", "వాళ్ళకు", "వాళ్ళకూ", "వాళ్ళది", "వాళ్ళని", "వాళ్ళను", "వాళ్ళము", "వాళ్ళలో", "వాళ్ళు", "వాళ్ళం", "వీటిలో", "వీడు", "వీరు", "వీళ్ళు"]
		self.english_conjunctions = ["and", "nor", "but", "or", "yet", "so", "though", "although", "even though", "while", "if", "only if", "unless", "until", "provided that", "assuming that", "even if", "in case", "lest", "than", "rather than", "whether", "as much as", "whereas", "after", "as long as", "as soon as", "before", "by the time", "now that", "once", "since", "till", "until", "when", "whenever", "while", "because", "since", "so that", "in order", "why", "that", "what", "whatever", "which", "whichever", "as though", "as if", "wherever", "also", "besides", "furthermore", "likewise", "moreover", "however", "nevertheless", "nonetheless", "still", "conversely", "instead", "otherwise", "rather", "accordingly", "consequently", "hence", "meanwhile", "then", "therefore", "thus"]
		self.hindi_conjunctions = ["अगर", "अतः", "अथवा", "अन्यथा", "अर्थात", "अलबत्ता", "एवं", "और", "औऱ", "कि", "किंतु", "क्योंकि", "चूंकि", "चूँकि", "जबकि", "जैसा", "जैसे", "जो", "तथा", "ताकि", "तो", "पर", "परंतु", "बल्कि", "बशर्ते", "बहरहाल", "मगर", "यदि", "यद्यपि", "या", "यानि", "यानी", "लिहाजा", "लिहाज़ा", "लेकिन", "व", "वरना", "वर्ना", "हालांकि", "हालाँकि"]
		self.telugu_conjunctions = ["అని", "అనే", "అన్న", "అయితే", "అంటే", "అంతమట్టుకు", "కాకుండా", "కాని", "కాబట్టి", "కొద్దీ", "గనుక", "గాని", "గానీ", "తరువాత", "దాకా", "నుంచి", "బట్టి", "మధ్య", "ముందు", "వెంటనే"]
	

	def get_discourse_and_cohesive_features(self, text, language):
		number_of_pronouns, number_of_conjunctions = 0, 0
		if language == 'english':
			for conjunct in self.english_conjunctions:
				if conjunct in text:
					number_of_conjunctions+=1
			for pronoun in self.english_pronouns:
				if pronoun in text:
					number_of_pronouns+=1
			return number_of_pronouns, number_of_conjunctions

		if language == 'hindi':
			for conjunct in self.hindi_conjunctions:
				if conjunct in text:
					number_of_conjunctions+=1
			for pronoun in self.hindi_pronouns:
				if pronoun in text:
					number_of_pronouns+=1
			return number_of_pronouns, number_of_conjunctions

		if language == 'telugu':
			for conjunct in self.telugu_conjunctions:
				if conjunct in text:
					number_of_conjunctions+=1
			for pronoun in self.telugu_pronouns:
				if pronoun in text:
					number_of_pronouns+=1
			return number_of_pronouns, number_of_conjunctions


	def get_syntactic_and_discourse_features_for_english(self, texts, language):
		number_of_nps, number_of_vps, number_of_pronouns, number_of_conjunctions = 0, 0, 0, 0
		for text in texts:
			if language == 'english':
				doc = self.nlp(text)
				nps = self.get_nps(doc, 'N')
				number_of_nps+=len(list(nps))
				vps = self.get_nps(doc, 'V')
				number_of_vps+=len(list(vps))

			pron, conj = self.get_discourse_and_cohesive_features(text, language)
			number_of_pronouns+=pron
			number_of_conjunctions+=conj

		return number_of_nps, number_of_vps, number_of_pronouns, number_of_conjunctions

	def get_nps(self, doc, tag):
		np_labels = ["nsubj", "nsubjpass", "dobj", "iobj", "pobj"]
		vp_labels = ["aux", "advmod"]

		for word in doc:
			if tag == 'N':
				if word.dep_ in np_labels:
					yield word.subtree
			else:
				if word.dep_ in vp_labels:
					yield word.subtree

	def get_phrases(self, generator):
		nps, np  = [], ""
		for phrases in generator:
			for phrase in phrases:
				np = np+phrase.text+" "
			nps.append(np)
			np = ""
		return nps

if __name__ == '__main__':
	
	sfc = SyntacticFeatureExtractor(nlp)
	nps, vps = sfc.get_syntactic_features_for_english(["A nice story about this silent and always present friend , the wind does a lot of things without anybody \'s notice !", "he came home"])
	print(nps, vps)
