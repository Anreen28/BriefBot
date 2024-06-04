import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """The Samsung Galaxy A series is a line of mid-range smartphones and tablets manufactured by Samsung Electronics as part of their Galaxy line. The first model in the series was the first-generation Galaxy Alpha, released on 31 October 2014.

Following the announcement of the 2017 series, Samsung announced that they hoped to sell up to 20 million Galaxy A series smartphones, targeting consumers in Europe, Africa, Asia, the Middle East and Latin America.[1]

As of 2020, most of the Galaxy A series models are available in most countries. Galaxy Tab A is also part of the A series and is available in most countries as well"""

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    #print(doc)

    tokens = [token.text for token in doc]

    word_freq ={}

    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text] +=1

    #print(word_freq)            

    max_freq = max(word_freq.values())

    for word in word_freq.keys():
        word_freq[word]= word_freq[word]/max_freq

    sent_tokens = [sent for sent in doc.sents]

    sent_score ={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent]= word_freq[word.text]
                else:
                    sent_score[sent] += word_freq[word.text]    

    #print(sent_score)

    select_len = int(len(sent_tokens)*0.37)
    #print(select_len)
    summary = nlargest(select_len, sent_score, key = sent_score.get)
    #print(summary)
    fin_sum = [word.text for word in summary]
    summary = ' '.join(fin_sum)
    # print(text)
    # print("org length", len(text.split(' ')))
    # print(summary)
    # print("sum length", len(summary.split(' ')))
    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))