# from gensim.models import KeyedVectors
# self.__instance.__model = KeyedVectors.load_word2vec_format(word2vecbin, binary=True, unicode_errors="ignore")
from singleton import SingletonMeta
from gensim.models import KeyedVectors
from numpy import array 

class GensimService(metaclass=SingletonMeta):
    model = None

    def __init__(self):
        print('init called')
        if (self.model == None):
            self.init_model()
    
    def init_model(self):
        print('init_model')
        self.model = KeyedVectors.load_word2vec_format('frWac_non_lem_no_postag_no_phrase_200_cbow_cut100.bin', binary=True, unicode_errors="ignore")
        print('init_model... ok! :)')

    def list_words(self):
        self.model.index_to_key

    def most_similar(self, _word: str, _topn=10) -> array:
        """ Ref: https://github.com/RaRe-Technologies/gensim/blob/develop/gensim/models/keyedvectors.py """
        return self.model.most_similar(positive=_word, topn=_topn)

    def similarity(self, _word1: str, _word2) -> float:
        """ Ref: https://tedboy.github.io/nlps/_modules/gensim/models/word2vec.html#Word2Vec.similarity """
        return self.model.similarity(w1=_word1, w2=_word2)