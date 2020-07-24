#!/usr/bin/env python3


import string
import re

class CleanMyData():
	"""Cleans the data by removing junk characters and words"""
	def __init__(self):
		pass

	def get_cleaned_data(self, data, language):
		if data == '<MISSING>':
			return data

		new_data = ""
		if language != 'english':
			data = re.sub("[a-zA-Z]+\-[a-zA-Z]+\s?", "", data)

		print(data, "****")	

		data = data.replace("&nbsp;", "")
		for char in list(data):

			if char in string.punctuation or char in [" ", "\n"]:
				new_data = new_data+char
			else:
				if language == "English":
					if ord(char) < 128:
						new_data = new_data + char
				if language == "Hindi":
					if ord(char) >= 2304 and ord(char) <= 2431:
						new_data = new_data+char

				if language == "Telugu":
					if ord(char) >= 3072 and ord(char) <= 3199:
						new_data = new_data+char

			continue

		new_data = re.sub("[\n|\r|\t|\f]+|^ ", "\n", new_data)
		new_data = re.sub(' +', ' ', new_data) 

		return self.clean_puncts(new_data)

	def clean_puncts(self, text):
		new_data = []
		for line in text.split("\n"):
			if not line.translate(str.maketrans('', '', string.punctuation)).isspace():
				new_data.append(line)
		return "\n".join(new_data)



if __name__ == '__main__':
	k = CleanData()
	# m =  SurfaceFeatureExractor()
	# n =  SyntacticFeatureExtractor()
	#text = "Kitchenvadoekdiscl ClothesT-hemp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kortbroek&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; das &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Kouse &nbsp; &nbsp;&nbsp; Baadjie&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Nagklere&nbsp;&nbsp;&nbsp; onderklereT-shirt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; shorts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tie&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; socks&nbsp;&nbsp;&nbsp;&nbsp; jacket&nbsp;&nbsp;&nbsp; pajamasisikipha&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ibhulukhwe&nbsp;&nbsp;&nbsp; iqhina﻿&nbsp;&nbsp;&nbsp; iikawusi&nbsp; ibhatyi&nbsp;&nbsp; ipijama ClothesT-hemp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kortbroek&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; das &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Kouse &nbsp; &nbsp;&nbsp; Baadjie&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NagklereT-shirt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; shorts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tie&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; socks&nbsp;&nbsp;&nbsp;&nbsp; jacket isikipha&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ibhulukhwe&nbsp;&nbsp;&nbsp; iqhina﻿&nbsp;&nbsp;&nbsp; iikawusi&nbsp; ibhatyi ClothesT-hemp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kortbroek&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; das &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Kouse &nbsp; &nbsp;&nbsp; Baadjie&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T-shirt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; shorts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tie&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; socks&nbsp;&nbsp;&nbsp;&nbsp; jacketisikipha&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ibhulukhwe&nbsp;&nbsp;&nbsp; iqhina﻿&nbsp;&nbsp;&nbsp; iikawusi ClothesT-hemp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kortbroek&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; das &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Kouse &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T-shirt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; shorts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tie&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; socksisikipha&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ibhulukhwe&nbsp;&nbsp;&nbsp; iqhina﻿&nbsp;&nbsp;&nbsp; iikawusi Lippe&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; maag&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Been&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GesigLips&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Stomach&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Leg&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; faceImilebe&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; isisu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Umlenze ClothesT-hemp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Kortbroek&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; das&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T-shirt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; shorts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tieisikipha&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ibhulukhwe&nbsp;&nbsp;&nbsp; iqhina  ClothesT-hemp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; KortbroekT-shirtisikipha माँ आयीं। बोलीं, “लो पत्थर को मार दिया।”  हिरण का बच्चा बोला, “इसे मत मारो। वरना, यह भी रोने लगेगा।” माँ हँस दीं। वह भी हँसने लगा। "
	text = """\n\n\t\n\t\n\t\n\t\n\n\n\n\n\t\n\t\n\t\n\t\n\n\n\nKallu stood frowning up at a huge poster stuck on the wall of the school compound.\n\n\n\n\n\n\n“Madan\nMurari Dev Maharaj is here!” he read out aloud. “Astrologer,\nmaster of horoscopes, tantra expert…” He turned to his best\nfriend Damu who was standing beside him and asked, “What’s a\nkundalini?”\n\n \n\n“I’m not too sure…” Damu scratched his ear, “something that goes up and down the spine…”“And what does that do?”“Generates some sort of electricity.”“Kya baat! He could solve our power-cut problem then,” Kallu grinned.\n\n\n\n“Right! We’ll all use the kundalini to start the water pump in the fields,” Damu laughed.By then, they had been joined by Kallu’s younger brother Shabbo. “Madan Murari Dev Maharaj,” he read the big letters under the picture of a fat man with a beard and a bright red turban. “Long name!”\n\n\n\n“Of course he has a long name,” Damu replied. “Look at all the things he can do – astrology, horoscopes, numbers, face reading, palmistry…”\n\n \n\n\t\n\t\n\t\n\t\n\n\nAs they walked away, Shabbo who had got four out of ten in the last maths test, asked thoughtfully, “Do you think he could predict the questions in tomorrow’s class test?”\n\n \n\nSoon the news of the astrologer had spread across Khajuria village. According to Damu’s grandmother Moti Dadi, Murari Dev had to just look into your eyes and say a mantra and he instantly knew everything about you – your past, present, future were all transferred to his mind like magic.\n\n \n\n\t\n\t\n\t\n\t\n\n\n“You mean now he knows that you borrowed a shawl from Billo Chachi and never returned it?” Damu’s sister Saru asked with a grin.\n\n\n\n“Don’t be silly, that is not important!” Moti Dadi waved a dismissive hand.“It is important to Billo Chachi,” Saru’s friend Munia commented and that made Moti Dadi so angry that she shooed both the girls out of her room.\n\n\n\nSo Kallu and his gang decided it was time to check out ‘Madan Murari Dev Maharaj, World Renowned Astrologer– Palmist–Tantra Expert–Futurologist–Numerologist.’ The gang included Kallu and Damu who were both in class nine. &nbsp;\n\n \n\n\t\n\t\n\t\n\t\n\n\n\n\nSaru and Munia were in class eight and Shabbo who was the youngest was in the seventh. In the school register, Kallu was Kallan, Damu was Damodar, Munia was Munira, Saru was Saraswati and Shabbo was Shabbir, but even their school principal, Masterji often forgot their real names. \n\n\t\n\t\n\t\n\t\n\n\n\n\n\t\n\t\n\t\n\t\n\n\n\n\nThe gang headed out the same evening. The astrologer was a guest at the home of Raghu Singh, the village sarpanch, and on the way to his house, they had to go past the Hanuman temple and there they saw a very strange sight.\n\nThe temple priest Lattu Mishra was sitting\nhunched up outside, his chin resting on his knees, looking sadly out\ninto space. Lattu was usually a cheerful man who greeted people with\na smile. Masterji had chosen him to play Bharat in the village\nRamleela because of his kind face and gentle smile.\n\n“Lattu\nBhaiya,” Munia ran up and asked anxiously, “what’s the matter?\nAre you ill?”\n\nLattu\nshook his head gloomily and then nodded to \nthe temple behind\nhim, “See the temple? It’s Tuesday and it is empty.”\n\n \n\n\t\n\t\n\t\n\t\n\n\n\n\n\t\n\t\n\t\n\t\n\n\n\n\nThey looked at the deserted temple in surprise. Usually on Tuesdays, people would stream in all day. It would echo with the chanting of mantras and the ringing of bells and Lattu would be busy before the altar, doing puja and arti to Hanumanji.\n\n“To\nRaghu Singh’s house, where else? Since the day that astrologer\nfellow has started his business, no one has time for Hanumanji\nanymore.”\n\n“Have\nyou seen him?”\n\n“Of\ncourse I have! I know everything about him. He used to have a mithai\nshop in town at one time and his name was Murari Lal. Everyone called\nhim Mota Murari because he was so fat. Then suddenly he grew a&nbsp;beard\nand became this Madan-whatever-Maharaj. He’s just learnt some magic\ntricks and is fooling the whole village.” \n\n\t\n\t\n\t\n\t\n\n\n\n\n\t\n\t\n\t\n\t\n\n\n“I’d read in the papers,” Kallan said thoughtfully, “about this school for magicians in Kerala. The principal of the school said that half his students were fake astrologers and sadhus.”“Maybe he went there.” Then Lattu noticed that they were all wearing their good clothes and looking very neat and clean. “You all are also going there?” he asked sadly.\n\n\n\n\t\n\t\n\t\n\t\n\n\n\n“Just for a look, Lattu Bhaiya,” Saru said gently. “We’ll be back soon.”\n\n\n\n\n\nWhen they strolled up to Raghu Singh’s house, they discovered that a huge tent had been put up in front and behind it, a smaller tent that had a kitchen where two cooks were busy over a large karhai that was smoking over a fire.\n\nDamu zipped off for a quick look and came back with a happy gleam in his eyes. \n\n\n\n \n\n\t\n\t\n\t\n\t\n\n\nPeering in, they discovered that the main tent was packed with people. They squeezed in at the back and looked around; it looked like the whole village was present. \n\n\n\n \n\nThere was Dharampal Chacha, the chai shop owner who played Ram in the Ramleela and his pretty wife Billo Chachi. Kishan Prasad, the grocer was chatting with Masterji who was offering him a paan.Even Mangu Mali, the mango orchard owner was sitting in a corner giving everyone his sour smile.\n\n\n\nBadri, the mad buffalo man who was sitting right in front of them turned, gave a grin — his huge yellow teeth gleaming behind his bushy moustache - and asked, “Did you check the kitchen at the back?”\n\n \n\n\t\n\t\n\t\n\t\n\n\n“Of\ncourse I did,” Damu gave a superior smile. He never missed out on\nimportant matters like food. “They are making halwa and puri, with\nasli ghee!”\n\n“Aha\nha ha!” Badri rolled his eyes in ecstasy.\n\n\n\n\t\n\t\n\t\n\t\n\n\n \n\n“Raghu Singh is a fool,” Mangu Mali said grimly, “feeding everyone and wasting money like this.”\n\n\n\nA sort of stage had been built in front with folding tables. A very tall, thin man was busy covering it with a mattress and a white sheet and then he placed a couple of bolsters on top. He lit a bunch of incense sticks and waved them about in the air.\n\n \n\n\t\n\t\n\t\n\t\n\n\n\n\n“Who’s\nthat?” Munia wanted to know.\n\n\n“That\nis Paltan Pandey,” Shabbo said, as the thin man began fixing a\nmike. “I asked him and he told me that he was the Maharaj’s\nnumber one assistant.”\n\n\n\n\t\n\t\n\t\n\t\n\n\n\n“Where\nis number two?” Kallu looked around.\n\n“I\ndon’t think there is one,” Damu laughed.\n\nKallu\nwondered if people planned to spend their hard earned money to get\ntheir horoscopes read or, like\nhis\ngang, were only there for the ‘asli-ghee-halwa-puri prasad’\ntreat.\n\n \n\n\t\n\t\n\t\n\t\n\n\n\n\n\t\n\t\n\t\n\t\n\n\n\nMadan\nMurari Dev Maharaj was late and everyone was getting restless. Heads\nkept turning to the opening in the tent to see if he was coming. A\ncouple of babies began to bawl, then Moti Dadi had a coughing fit and\nSaru had to go out and get her a glass of water.&nbsp;\n\n \n\nBillo Chachi had come prepared to wait and had nearly finished knitting the sleeve of a sweater. Noticing the growing restlessness, Paltan Pandey suddenly sat down with a harmonium and began to sing a bhajan in a flat, tuneless moan.\n\n\n\nEveryone was falling into a bored trance when to their surprise, Paltan suddenly shot up his arms in the air and yelled “Jai Murari Dev!” making everyone jump.&nbsp;\n\n \n\n\t\n\t\n\t\n\t\n\n\n\nIt\nseemed the audience was expected to join in and they did. At least it\nwas something to do. So everyone waved their arms and echoed his\ncall, “Jai Murari Dev!”\n\nThe\ngang grinned at each other and joined in, yelling at the top of their\nvoices, “Jai Kapil Dev! Jai Kapil Dev!” but after they had called\nfor their cricket hero Kapil the third time, some of the elders\nturned and glared at them and they decided to shut up. Too much of\nthe funny stuff could get them kicked out of the tent and as Damu\npointed out, halwa-puri was at stake. As if finally hearing their\ncalls, Murari Dev arrived, leaning on the arm of Raghu Singh and\nwalking very, very slowly.\n\n\n\n\t\n\t\n\t\n\t\n\n\n\n“Baap re!” an astonished Saru whispered. “He’s really fat!” “That photo on the poster must have been taken years ago.”\n\n\n\n \n\n\t\n\t\n\t\n\t\n\n\n\nMurari\nDev was quite short and wearing a bright red flowing silk robe, and\nrows and rows of multi-coloured beads were hanging around his neck.\nHis long, grey beard flowed down over his generous pot-belly and he\nwas quite bald. There was a red tikka drawn on his forehead and even\nthough it was evening, to everyone’s surprise he wore a jazzy pair\nof dark glasses. \n\n\t\n\t\n\t\n\t\n\n\n“Dark\nglasses?” Damu looked around, “where’s the sun?”\n\nMurari\nDev went past them and they were swept away by the strong scent of\nhis cologne.\n\n“Kya\nbaat!” Kallu commented happily. “Dark glasses, \nbead\nnecklaces, perfume, this is a hero horoscope man! Straight from\nBollywood!”\n\nMunia\nwas still staring at Paltan with a thoughtful frown, “Paltan looks\nfamiliar somehow.”\n\n“I\nknow,” Shabbo grinned, “in a safari suit, he’d look just like\nRam Lochan at the petrol pump.”\n\n“Correct!”\nthey all said together. Badri turned to glare at them, “Chup!” So\nthey shut up but Munia and Saru had to try really hard to stop the\ngiggles. They never knew astrology could be so funny!\n\nBy then Murari Dev was sitting leaning against a bolster, panting slightly and wiping his face with a handkerchief.\n\n\n\n \n\n\t\n\t\n\t\n\t\n\n\nPaltan rushed up\nwith a glass of water. Raghu Singh switched on a table fan. Murari\nDev cleared his throat, checked his watch and pulled the mike closer.\n\n\n\n\t\n\t\n\t\n\t\n\n\n\n“Please\nstart,” Damu muttered, “the halwa is getting cold.”\n\nWith majestic slowness, Murari Dev stood up, walked to the edge of the stage and with a dramatic flourish, waved his podgy hands in the air.\n\n\n\n \n\n\t\n\t\n\t\n\t\n\n\nSuddenly walnuts and raisins were raining on the audience! Behind the\nastrologer, Paltan was banging away at the harmonium and swaying to\nthe tune. Murari Dev waved his arms again and more raisins and\nwalnuts flew around.\n\n \n\n“They’re real!” Saru mumbled, busy chewing.“Must have got them from Kishen Prasad’s grocery store,” Damu said as he scrambled about for more.The gang sat up. It looked like the introduction was over and the show was about to begin. Paltan announced on the mike that Murari Dev would now predict the future and read minds.\n\n\n\nHe then walked around in the audience with chits of paper. Someone would write a number on a chit, which would be sealed inside an envelope and carried to the astrologer, who would touch the envelope, hum a mantra and then recite the number correctly.&nbsp;\n\n&nbsp;&nbsp;\n\n \n\nVery impressed by the mind reading, people were soon trooping up on stage to know about their futures and many of them were carrying their horoscopes.Murari Dev talked to them in a low voice and then whispered his predictions into their ears. So the gang could not hear anything . The rupee notes were soon piling up in the brass plate kept before him.\n\n\n\nFinally the show was over and everyone got their leaf plate of halwa-puri. To the background music of the harmonium, Murari Dev got up and swayed across the stage.Then with a piercing yell and a splintering crash, Murari Dev vanished!\n\n \n\n\t\n\t\n\t\n\t\n\n\n\n\nThere\nwas pandemonium in the pandal. Paltan and Raghu Singh were\nfrantically searching for him. Moti Dadi was weeping loudly and\ncalling out, “Maharaj aap kahan ho?”&nbsp;Masterji\nwas yelling at the gang, ordering them to go and find a torch. And in\nthe middle of all the chaos, Badri and Mangu Mali stood there,\nlaughing their heads off.\n\n \n\n\t\n\t\n\t\n\t\n\n\n\n\nThen\nto everyone’s relief, Murari Dev slowly crawled out from under the\nstage and as Paltan and Raghu Singh rushed up to help him, he stood\nup groggily. He&nbsp;was\nquite a sight, his snazzy glasses askew, his beard covered in\nspider’s web and his silk robe all dusty.\n\n\n“What\nhappened?” Damu asked puzzled. “I thought it was a vanishing\nact,” Kallu said. \n\n\nIt\ntook a while to solve the mystery. The stage had been made with three\nwooden folding tables and one of them had a broken leg. When fat\nMurari Dev had stepped on it, the table had collapsed taking him down\nwith it. He now sat panting on a chair, flushed, dishevelled and\nobviously feeling very sorry for himself. \n\nAt this crucial moment, Saru spoke up. Planting herself in front of the astrologer, she bent a stern face towards him and said clearly above the hubbub, “But Murari Devji... I don’t understand this!”The fat astrologer sat up and stared at her.\n\n“You could read the numbers, pick walnuts out of the air and predict futures. How is it that you didn’t know that the table was broken?”In the growing silence, Murari Dev glared at Saru and her gang who were standing there looking critically at him. Then with a grim look on his face, he got up and stalked out of the pandal, as everyone began to laugh. Moti Dadi laughed so hard that she had another coughing fit and everyone agreed it had been a really great show.\n\n"""	#text), text, ">>>>>")
	cData = k.get_cleaned_data(text, 'english')
	#print(cData)
	# sentences = utils.get_tokenized_sentences(cData, 'english')
	# #print(sentences)
	# numOfChars = m.get_surface_features(sentences)
	# print(numOfChars)

	#nlp =  spacy.load('en_core_web_sm')

	#for i in sentences:
	#	doc = nlp(i)
	#	print(n.get_syntactic_features_for_english(doc))

	

