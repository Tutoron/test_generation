from test_generation.paperParser import paperParser
from test_generation import util

pp = paperParser()
# sentences = list(pp.parse_paper("data/example_paper.tex"))
sentences = list(pp.parse_paper("data/fully connect paper/paper.tex"))

detector = util.SymbolDetector()

i = 1

for s in sentences:
    if detector.detect_symbol(s, '\mb{f}'):
    # if detector.detect_symbol(s, '\\mathtt'):
        print("Number " + str(i))
        i += 1
        print(s)
        print("\n")
