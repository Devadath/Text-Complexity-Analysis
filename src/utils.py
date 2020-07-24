#!/usr/bin/env python3


from polyglot_tokenizer import Tokenizer

def get_sentences(list_of_tokens):
	sentences = []
	for word_list in list_of_tokens:
		if (" ".join(word_list) != ""):
			sentences.append(" ".join(word_list))
	return sentences


def get_tokenized_sentences(text, language):
	lang = ""

	if language == "english":	lang = "en"
	if language == "hindi":	lang = "hi"
	if language == "telugu":	lang = "te"

	tk = Tokenizer(lang=lang, split_sen=True)

	tokens = tk.tokenize(text)

	return get_sentences(tokens)




