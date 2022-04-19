import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

class Model():
    def __init__(self, n_components, min_df, beta, gamma, score_indexes):
        self.n_components = n_components
        self.min_df = min_df
        self.transform_matrix = None
        self.vocab = None
        self.idf = None
        self.gamma = gamma
        self.beta = beta 
        self.score_indexes = score_indexes

    def is_trained(self):
        return self.transform_matrix == None 

    def train(self, corpus):
        tfidf = TfidfVectorizer(min_df=self.min_df)
        raw_vectors = tfidf.fit_transform(list(map(lambda a: a.data_text, corpus)))
        self.vocab = tfidf.get_feature_names_out()
        self.idf = np.log(len(corpus) / np.count_nonzero(raw_vectors.toarray(), axis=0))
        svd = TruncatedSVD(n_components=self.n_components)
        self.transform_matrix = svd.fit_transform(raw_vectors.T)

    def vectorize(self, a):
        tf = CountVectorizer(vocabulary=self.vocab).fit_transform([a.data_text])
        return (tf * self.idf) @ self.transform_matrix
    
    def score(self, u, a):
        dist = np.linalg.norm(a.vector - u.prefs)
        score = np.exp(-self.gamma*a.age)/(1+dist)
        return score

    def recommend(self, user, corpus):
        args = np.argsort(list(map(lambda a: self.score(user, a), corpus)))
        return corpus[args[self.score_indexes]]

    def new_user_pref(self, user, article, rating):
       return (self.beta * user.n * user.prefs + rating * article.vector) / (self.beta * user.n + 1)


