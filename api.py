"""First hug API (local, command-line, and HTTP access)"""
import hug
from gensimService import GensimService

@hug.cli()
@hug.get(example='word=france')
@hug.local()
def most_similar(word: hug.types.text):
    """Get a list of word most similar to given word"""
    service = GensimService()
    return service.most_similar(word)

@hug.cli()
@hug.get(example='word1=france&word2=france')
@hug.local()
def similarity(word1: hug.types.text, word2: hug.types.text):
    """Get a list of word most similar to given word"""
    service = GensimService()
    return service.similarity(word1, word2)

if __name__ == '__main__':
    most_similar.interface.cli()
    similarity.interface.cli()
