import json

"""
========================================================
:mod:`jsonParsing` jsonParsing
========================================================
.. moduleauthor:: 김승재
.. moduleauthor:: 윤채훈

설명
=====

Cuckoo-report Json Parsing Module

    * category_file()
    * category_process()
    * category_system()
    * category_ole()
    * category_synchronisation()

관련 작업자
===========

본 모듈은 다음과 같은 사람들이 관여했습니다:
    * 인텔리전스팀 김승재, 윤채훈

작업일지
--------

다음과 같은 작업 사항이 있었습니다:
    * [2019/11/13] - 초기 개발

"""

class jsonParsing():
    """Cuckoo 분석 후에 나오는 report.json 을 필요한 부분 추출 하는 클래스.
        
    :param str path: 파싱 파일의 위치.
    :param str save_path: 추출 내용 저장 파일 이름.
    """

    def __init__(self, path, save_path):
        self.path = path
        self.save_path = save_path
    
    def category_file(self, c):
        """report.json 의 file 객체에서 필요한 부분 추출

        :param str c: report file 객체
        :return: 추출한 값을 문자열로 리턴
        """

        behavior_file =  "%-15s%s%s%s" % ("category", ": [" , c['category'] , "]\n")
        behavior_file += "%-15s%s%s%s" % ("api", ": [" , c['api'] , "]\n")
        if ('filepath' in c['arguments']):
            behavior_file += "%-15s%s%s%s" % ("filepath", ": [" , c['arguments']['filepath'] , "]\n")

        if ('filepath_r' in c['arguments']):
            behavior_file += "%-15s%s%s%s" % ("filepath_r", ": [" , c['arguments']['filepath_r'] , "]\n")

        behavior_file += "%-15s%s%s%s" % ("flag", ": [" , json.dumps(c['flags']) , "]\n\n")
        return behavior_file

    def category_process(self, c):
        """report.json 의 process 객체에서 필요한 부분 추출
        
        :param str c: report process 객체
        :return: 추출한 값을 문자열로 리턴
        """

        behavior_process =  "%-15s%s%s%s" % ("category", ": [" , c['category']  , "]\n")
        behavior_process += "%-15s%s%s%s" % ("api", ": [" , c['api'] , "]\n")

        if ('process_identifier' in c['arguments']):
            behavior_process += "%-15s%s%s%s" % ("process_identifier", ": [" , c['arguments']['process_identifier'] , "]\n")

        if ('base_address' in c['arguments']):
            behavior_process += "%-15s%s%s%s" % ("base_address", ": [" , c['arguments']['base_address'] , "]\n")

        behavior_process += "%-15s%s%s%s" % ("flags", ": [" , json.dumps(c['flags']) , "]\n\n")
        return behavior_process

    def category_system(self, c):
        """report.json 의 system 객체에서 필요한 부분 추출
        
        :param str c: report system 객체
        :return: 추출한 값을 문자열로 리턴
        """

        behavior_system =  "%-15s%s%s%s" % ("category", ": [" , c['category'] , "]\n")
        behavior_system += "%-15s%s%s%s" % ("api", ": [" , c['api'] , "]\n")
        
        if ('basename' in c['arguments']):
            behavior_system += "%-15s%s%s%s" % ("basename", ": [" , c['arguments']['basename'] , "]\n")
            behavior_system += "%-15s%s%s%s" % ("module_name", ": [" , c['arguments']['module_name'] , "]\n")
        
        if ('handle' in c['arguments']):
            behavior_system += "%-15s%s%s%s" % ("handle", ": [" , c['arguments']['handle'] , "]\n")

        if ('ordinal' in c['arguments']):
            behavior_system += "%-15s%s%s%s" % ("module", ": [" , c['arguments']['module'] , "]\n")
            behavior_system += "%-15s%s%s%s" % ("function_name", ": [" , c['arguments']['function_name'] , "]\n")

        if ('library' in c['arguments']):
            behavior_system += "%-15s%s%s%s" % ("library", ": [" , c['arguments']['library'] , "]\n")
        
        behavior_system += "%s" % ("\n")

        return behavior_system

    def category_ole(self, c):
        """report.json 의 ole 객체에서 필요한 부분 추출
        
        :param str c: report ole 객체
        :return: 추출한 값을 문자열로 리턴
        """

        behavior_ole =  "%-15s%s%s%s" % ("category", ": [" , c['category'] , "]\n")
        behavior_ole += "%-15s%s%s%s" % ("api", ": [" , c['api'] , "]\n")
        behavior_ole += "%-15s%s%s%s" % ("flag", ": [" , json.dumps(c['flags']) , "]\n\n")
        return behavior_ole

    def category_synchronisation(self, c):
        """report.json 의 synchronisation 객체에서 필요한 부분 추출
        
        :param str c: report synchronisation 객체
        :return: 추출한 값을 문자열로 리턴
        """

        behavior_synchronisation =  "%-15s%s%s%s" % ("category", ": [" , c['category'] , "]\n")
        behavior_synchronisation += "%-15s%s%s%s" % ("api", ": [" , c['api'] , "]\n")
        behavior_synchronisation += "%-15s%s%s%s" % ("flag", ": [" , json.dumps(c['flags']) , "]\n\n")
        return behavior_synchronisation

    def category_registry(self, c):
        """report.json의 registry 객체에서 필요한 부분 추출

        :param str c: report registry 객체
        :return: 추출한 값을 문자열로 리턴
        """

        behavior_registry =  "%-15s%s%s%s" % ("category", ": [" , c['category'] , "]\n")
        behavior_registry += "%-15s%s%s%s" % ("api", ": [" , c['api'] , "]\n")
        
        if ('value' in c['arguments']):
            behavior_registry += "%-15s%s%s%s" % ("value", ": [" , c['arguments']['value'] , "]\n")

        if ('regkey' in c['arguments']):
            behavior_registry += "%-15s%s%s%s" % ("regkey", ": [" , c['arguments']['regkey'] , "]\n")

        if ('regkey_r' in c['arguments']):
            behavior_registry += "%-15s%s%s%s" % ("regkey_r", ": [" , c['arguments']['regkey_r'] , "]\n")

        behavior_registry += "%-15s%s%s%s" % ("flag", ": [" , json.dumps(c['flags']) , "]\n\n")
        return behavior_registry

    def category_misc(self, c):
        """report.json의 misc 객체에서 필요한 부분 추출

        :param str c: report misc 객체
        :return: 추출한 값을 문자열로 리턴
        """

        behavior_misc =  "%-15s%s%s%s" % ("category", ": [" , c['category'] , "]\n")
        behavior_misc += "%-15s%s%s%s" % ("api", ": [" , c['api'] , "]\n")
        
        if ('username' in c['arguments']):
            behavior_misc += "%-15s%s%s%s" % ("username", ": [" , c['arguments']['username'] , "]\n")

        if ('computer_name' in c['arguments']):
            behavior_misc += "%-15s%s%s%s" % ("computer_name", ": [" , c['arguments']['computer_name'] , "]\n")

        if ('dirpath' in c['arguments']):
            behavior_misc += "%-15s%s%s%s" % ("dirpath", ": [" , c['arguments']['dirpath'] , "]\n")

        if ('dirpath_r' in c['arguments']):
            behavior_misc += "%-15s%s%s%s" % ("dirpath_r", ": [" , c['arguments']['dirpath_r'] , "]\n")

        if ('filepath' in c['arguments']):
            behavior_misc += "%-15s%s%s%s" % ("filepath", ": [" , c['arguments']['filepath'] , "]\n")

        behavior_misc += "%-15s%s%s%s" % ("flag", ": [" , json.dumps(c['flags']) , "]\n\n")
        return behavior_misc
        
    def category_ui(self, c):
        """report.json의 ui 객체에서 필요한 부분 추출

        :param str c: report ui 객체
        :return: 추출한 값을 문자열로 리턴
        """

        behavior_ui =  "%-15s%s%s%s" % ("category", ": [" , c['category'] , "]\n")
        behavior_ui += "%-15s%s%s%s" % ("api", ": [" , c['api'] , "]\n")
        
        if ('string' in c['arguments']):
            behavior_ui += "%-15s%s%s%s" % ("string", ": [" , c['arguments']['string'] , "]\n")

        behavior_ui += "%-15s%s%s%s" % ("flag", ": [" , json.dumps(c['flags']) , "]\n\n")
        return behavior_ui


    def parsing(self, category):
        """ report.json 의 원하는 부분을 추출 하는 로직
        
        :param str category: 추출 category 의 키워드
        """
        
        with open(self.path) as json_file: 
            json_data = json.load(json_file) 
            print(json_data['process_path']) 

            for c in json_data['calls']:

                if ((category == "all" or category == "file") and c['category'] == "file"):
                    save_file = open(self.save_path+"_"+category+".txt", 'a', -1, "utf-8")
                    save_file.write(self.category_file(c))

                elif ((category == "all" or category == "process") and c['category'] == "process"):
                    save_file = open(self.save_path+"_"+category+".txt", 'a', -1, "utf-8")
                    save_file.write(self.category_process(c))

                elif ((category == "all" or category == "system") and c['category'] == "system"):
                    save_file = open(self.save_path+"_"+category+".txt", 'a', -1, "utf-8")
                    save_file.write(self.category_system(c))

                elif ((category == "all" or category == "ole") and c['category'] == "ole"):
                    save_file = open(self.save_path+"_"+category+".txt", 'a', -1, "utf-8")
                    save_file.write(self.category_ole(c))

                elif ((category == "all" or category == "synchronisation") and c['category'] == 'synchronisation'):
                    save_file = open(self.save_path+"_"+category+".txt", 'a', -1, "utf-8")
                    save_file.write(self.category_synchronisation(c))
            
                elif ((category == "all" or category == "registry") and c['category'] == "registry"):
                    save_file = open(self.save_path+"_"+category+".txt", 'a', -1, "utf-8")
                    save_file.write(self.category_registry(c))

                elif ((category == "all" or category == "misc") and c['category'] == "misc"):
                    save_file = open(self.save_path+"_"+category+".txt", 'a', -1, "utf-8")
                    save_file.write(self.category_misc(c))

                elif ((category == "all" or category == "ui") and c['category'] == "ui"):
                    save_file = open(self.save_path+"_"+category+".txt", 'a', -1, "utf-8")
                    save_file.write(self.category_ui(c))