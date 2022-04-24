import spacy
import os
import json

def tokenize(file, outname): 
	# load spacy model
	nlp = spacy.load('en_core_web_sm')
 
	# load data
	
	doc = nlp(open(file).read())
	 
	diction = dict()

	# print entities
	for ent in doc.ents:
		
		#print(ent.label_, ent.start_char, ent.end_char, ent.text)
		#Add each text to its specific label using dictionary 
		diction[ent.text] = ent.label_
		
    			
	#print(diction)
	f = open(outname, "w")
	json.dump(diction, f)
	
if __name__ == '__main__':
	
	#aljazeera
	'''
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/01/01_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/01/tokenized_01.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/02/02_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/02/tokenized_02.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/03/03_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/03/tokenized_03.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/04/04_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/04/tokenized_04.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/05/05_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/05/tokenized_05.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/06/06_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/06/tokenized_06.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/07/07_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/07/tokenized_07.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/08/08_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/08/tokenized_08.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/09/09_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/09/tokenized_09.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/10/10_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/10/tokenized_10.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/11/11_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/11/tokenized_11.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/12/12_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/12/tokenized_12.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/13/13_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/13/tokenized_13.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/14/14_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/14/tokenized_14.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/15/15_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/15/tokenized_15.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/16/16_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/16/tokenized_16.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/17/17_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/17/tokenized_17.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/18/18_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/18/tokenized_18.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/19/19_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/19/tokenized_19.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/20/20_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/20/tokenized_20.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/21/21_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/21/tokenized_21.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/22/22_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/22/tokenized_22.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/23/23_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/23/tokenized_23.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/24/24_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/24/tokenized_24.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/25/25_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/25/tokenized_25.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/26/26_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/26/tokenized_26.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/27/27_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/27/tokenized_27.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/28/28_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/28/tokenized_28.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/29/29_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/29/tokenized_29.json')
	tokenize('/Users/zahinroja/Downloads/data/aljazeera_text/30/30_aljazeera_concat.txt', '/Users/zahinroja/Downloads/data/aljazeera_NER_tokenization/30/tokenized_30.json')
	'''
	#cnn
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/01/01_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/01/tokenized_01.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/02/02_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/02/tokenized_02.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/03/03_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/03/tokenized_03.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/04/04_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/04/tokenized_04.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/05/05_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/05/tokenized_05.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/06/06_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/06/tokenized_06.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/07/07_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/07/tokenized_07.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/08/08_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/08/tokenized_08.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/09/09_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/09/tokenized_09.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/10/10_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/10/tokenized_10.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/11/11_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/11/tokenized_11.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/12/12_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/12/tokenized_12.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/13/13_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/13/tokenized_13.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/14/14_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/14/tokenized_14.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/15/15_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/15/tokenized_15.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/16/16_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/16/tokenized_16.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/17/17_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/17/tokenized_17.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/18/18_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/18/tokenized_18.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/19/19_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/19/tokenized_19.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/20/20_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/20/tokenized_20.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/21/21_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/21/tokenized_21.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/22/22_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/22/tokenized_22.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/23/23_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/23/tokenized_23.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/24/24_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/24/tokenized_24.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/25/25_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/25/tokenized_25.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/26/26_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/26/tokenized_26.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/27/27_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/27/tokenized_27.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/28/28_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/28/tokenized_28.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/29/29_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/29/tokenized_29.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/30/30_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/30/tokenized_30.json')
	tokenize('/Users/zahinroja/Downloads/data/cnn_text/31/31_cnn_concat.txt', '/Users/zahinroja/Downloads/data/cnn_NER_tokenization/31/tokenized_31.json')

	#fox
	tokenize('/Users/zahinroja/Downloads/data/fox_text/12/12_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/12/tokenized_12.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/13/13_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/13/tokenized_13.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/14/14_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/14/tokenized_14.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/15/15_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/15/tokenized_15.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/16/16_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/16/tokenized_16.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/17/17_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/17/tokenized_17.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/18/18_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/18/tokenized_18.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/19/19_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/19/tokenized_19.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/20/20_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/20/tokenized_20.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/21/21_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/21/tokenized_21.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/22/22_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/22/tokenized_22.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/23/23_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/23/tokenized_23.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/24/24_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/24/tokenized_24.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/25/25_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/25/tokenized_25.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/26/26_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/26/tokenized_26.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/27/27_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/27/tokenized_27.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/28/28_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/28/tokenized_28.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/29/29_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/29/tokenized_29.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/30/30_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/30/tokenized_30.json')
	tokenize('/Users/zahinroja/Downloads/data/fox_text/31/31_fox_concat.txt', '/Users/zahinroja/Downloads/data/fox_NER_tokenization/31/tokenized_31.json')
