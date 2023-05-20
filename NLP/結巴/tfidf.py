import math
import pandas as pd

def tokenize_documents(documents):
    tokenized_docs = [[word.lower() for word in doc.split() if len(word) >= 2] for doc in documents]
    return tokenized_docs

def calculate_tf(tokenized_docs):
    tf = {}
    for i, doc in enumerate(tokenized_docs):
        for word in doc:
            if word not in tf:
                tf[word] = [0] * len(tokenized_docs)
            tf[word][i] = doc.count(word) / len(doc)
    return tf

def calculate_idf(tokenized_docs):
    idf = {}
    total_docs = len(tokenized_docs)
    for doc in tokenized_docs:
        for word in set(doc):
            if word not in idf:
                num_docs_containing_word = sum(1 for d in tokenized_docs if word in d)
                idf[word] = math.log((total_docs + 1) / (num_docs_containing_word + 1)) + 1
    return idf

def calculate_tfidf(tokenized_docs, tf, idf):
    tfidf = []
    for word in sorted(set(tf.keys())):
        values = [tf[word][i] * idf[word] for i in range(len(tokenized_docs))]
        tfidf.append(values)
    return pd.DataFrame(tfidf)

def tf_idf(documents):
    tokenized_docs = tokenize_documents(documents)
    tf = calculate_tf(tokenized_docs)
    idf = calculate_idf(tokenized_docs)
    return calculate_tfidf(tokenized_docs, tf, idf)
