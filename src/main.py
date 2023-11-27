"""Citation main function"""""
from entities.citationArticle import CitationArticle
from services.generateCitate import GenerateCitate


def main():
    citation = CitationArticle("article", "CitekeyArticle", "P. J. Cohen",
                               "The independence of the continuum hypothesis",
                               "Proceedings of the National Academy of Sciences",
                               1963, "50", "6", "1143--1148")
    # print(citation)
    print(citation.citation_to_bibtex_entry())


if __name__ == "__main__":
    main()
