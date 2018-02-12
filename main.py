from test_generation.paperParser import paperParser
from test_generation import util

pp = paperParser()
sentences = list(pp.parse_paper("data/example_paper.tex"))

detector = util.SymbolDetector()

for s in sentences:
    if detector.detect_symbol(s, '\\mathtt'):
        print(s)
