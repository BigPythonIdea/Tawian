import jieba

def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def segment(text, stopwords_path):
    jieba.set_dictionary("./NLP/dict.txt")
    stopwords = load_stopwords(stopwords_path)
    tokens = jieba.cut(text)
    filtered_tokens = [token for token in tokens if token not in stopwords and token != '\n' and token != " "]
    return ''.join(filtered_tokens)
