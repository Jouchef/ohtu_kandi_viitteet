"""From doi to bibtex class"""
import sys
import urllib.request
from urllib.error import HTTPError

class CitationFromDoi:
    """From doi to bibtex"""
    BASE_URL = 'http://dx.doi.org/'


    def __init__(self, doi):
        self.doi = doi
        self.bibtex = None
        self._get_bibtex()

    def _get_bibtex(self):
        """Get bibtex from doi and save it to self.bibtex"""
        url = self.BASE_URL + self.doi
        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/x-bibtex')
        try:
            with urllib.request.urlopen(req) as f:
                self.bibtex = f.read().decode()
        except HTTPError as e:
            if e.code == 404:
                print('DOI not found.')
            else:
                print('Service unavailable.')
            sys.exit(1)

    def get_bibtex(self):
        """Return bibtex"""
        return self.bibtex
