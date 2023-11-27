<<<<<<< HEAD
# python file
from citationArticle import CitationArticle
=======
"""Citation main function"""""
from entities.citationArticle import CitationArticle
from services.generateCitate import GenerateCitate

>>>>>>> b7aff9b2ab08e9e69d887662f7d90c4173af1b9f

def main():
    citation = CitationArticle("article", "CitekeyArticle", "P. J. Cohen",
                               "The independence of the continuum hypothesis",
                               "Proceedings of the National Academy of Sciences",
                               1963, "50", "6", "1143--1148")
    # print(citation)
    print(citation.citation_to_bibtex_entry())


if __name__ == "__main__":
    main()
