class CountVectorizer:
    def __init__(self, ngram_size):
        self.token_size = ngram_size
        self.vocab = dict()
        self.tokens = set()

    @staticmethod
    def __vectorizeString(string, size):
        res_arr = []
        for i in range(len(string) - 1):
            res_arr.append(f'{string[i:i + size]}')
        return res_arr

    def fit(self, corpus):
        self.vocab.clear()
        self.tokens.clear()
        for string in corpus:
            for token in self.__vectorizeString(string, self.token_size):
                self.tokens.add(token)

        self.vocab = {k: v for v, k in enumerate(sorted(list(self.tokens)))}

    def transform(self, corpus):
        corpus_list = []
        for string in corpus:
            line = self.__vectorizeString(string, self.token_size)
            token_counter = dict()
            for token in line:
                if token in token_counter:
                    token_counter[token] += 1
                else:
                    token_counter[token] = 1

            corpus_line = []
            vocab = self.vocab
            for key, value in vocab.items():
                if key in token_counter:
                    corpus_line.append(token_counter[key])
                else:
                    corpus_line.append(0)
            corpus_list.append(corpus_line)
        return corpus_list

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)

