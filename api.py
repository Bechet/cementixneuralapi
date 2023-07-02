"""First hug API (local, command-line, and HTTP access)"""
import hug
from gensimService import GensimService

@hug.cli()
@hug.get(example='word1=france&word2=france')
@hug.local()
def similarity(word: hug.types.text):
    """Get a list of word most similar to given word"""
    service = GensimService()
    return service.most_similar(word)

if __name__ == '__main__':
    similarity.interface.cli()
