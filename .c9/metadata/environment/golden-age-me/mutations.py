{"filter":false,"title":"mutations.py","tooltip":"/golden-age-me/mutations.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":16},"end":{"row":7,"column":16},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"39e3f5745e5d30f42254a94df3ccd1c463274cac","mime":"text/x-script.python","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":7,"column":16},"action":"insert","lines":["def mutate_string(string, position, character):","    return string[:position]+character+string[position+1:]","","if __name__ == '__main__':","    s = input()","    i, c = input().split()","    s_new = mutate_string(s, int(i), c)","    print(s_new)"],"id":2}]]},"timestamp":1665033719290}