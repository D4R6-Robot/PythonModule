import jsonParsing 
 
"""
========================================================
:mod:`jsonParsingMain` jsonParsingMain
========================================================
.. moduleauthor:: 김승재
.. moduleauthor:: 윤채훈

설명
=====

Cuckoo-report Json Parsing Module

    * main()

관련 작업자
===========

본 모듈은 다음과 같은 사람들이 관여했습니다:
    * 인텔리전스팀 김승재, 윤채훈

작업일지
--------

다음과 같은 작업 사항이 있었습니다:
    * [2019/11/13] - 초기 개발

"""

class jsonParsingMain(): 
    """Json Parsing Main 테스트 클래스

    :param none
    """

    def __init__(self): 
        path = './1424409_apistats_ps1.json' 
        save_path = './1424409_apistats_ps1_report' 
        self.parsingMain = jsonParsing.jsonParsing(path, save_path) 
 
    def main(self): 
        self.parsingMain.parsing("all") 
        self.parsingMain.parsing("file") 
        self.parsingMain.parsing("process") 
        self.parsingMain.parsing("system") 
        self.parsingMain.parsing("ole") 
        self.parsingMain.parsing("synchronisation")
        self.parsingMain.parsing("registry")
        self.parsingMain.parsing("misc")
        self.parsingMain.parsing("ui")
 
if __name__ == '__main__': 
    main_class = jsonParsingMain() 
    main_class.main()