import DocParsing 
 
"""
========================================================
:mod:`jsonParsingMain` jsonParsingMain
========================================================
.. moduleauthor:: 김승재

설명
=====

Cuckoo-report Json Parsing Module

    * main()

관련 작업자
===========

본 모듈은 다음과 같은 사람들이 관여했습니다:
    * 인텔리전스팀 김승재

작업일지
--------

다음과 같은 작업 사항이 있었습니다:
    * [2019/12/09] - 문서 관련 업데이트

"""

class DocParsingMain(): 
    """Json Parsing Main 테스트 클래스

    :param none
    """

    def __init__(self): 
        path = './Report/Doc/info_09_05--004-reports.json' 
        self.parsingMain = DocParsing.DocParsing(path) 
 
    def main(self): 
        self.parsingMain.parsing() 
        self.parsingMain.DocPrint()
 
if __name__ == '__main__': 
    main_class = DocParsingMain() 
    main_class.main()