import json
import array

"""
========================================================
:mod:`jsonParsing` jsonParsing
========================================================
.. moduleauthor:: 김승재

설명
=====

Cuckoo-report Document Parsing Module

    * ProcessTree()
    * SummaryFile()
    * OfficeMacros()
    * HttpMalCheck()
    * category_synchronisation()

관련 작업자
===========

본 모듈은 다음과 같은 사람들이 관여했습니다:
    * 인텔리전스팀 김승재

작업일지
--------

다음과 같은 작업 사항이 있었습니다:
    * [2019/12/09] - 초기 개발

"""

class DocParsing():
    """Cuckoo 분석 후에 나오는 report.json 을 필요한 부분 추출 하는 클래스.
        
    :param str path: 파싱 파일의 위치.
    :param str save_path: 추출 내용 저장 파일 이름.
    """

    def __init__(self, path):
        self.path = path
        self.processTree = 0
        self.xslCount = 0
        self.jsCount = 0
        self.msformsCount = 0
        self.macrosCount = 0
        self.httpCount = 0
        self.ntList = [0, 0, 0, 0, 0, 0, 0]
        self.fileList = [0, 0, 0, 0, 0, 0]
    
    def ProcessTree(self, json_data):
        """report.json behavior 의 generic 필요한 부분 추출
           중요한 파일에 대한 가중치를 부여하는 값 추출

        :param dict json_data: report process 객체
        :return: 중요한 파일의 가중치.
        """
        generic = json_data['behavior']['generic']
        
        for i in generic:
            if i['process_name'].lower() == "wscript.exe":
                self.processTree = self.processTree + 1
            elif i['process_name'].lower() == "wmic.exe":
                self.processTree = self.processTree + 2
            elif i['process_name'].lower() == "powershell.exe":
                self.processTree = self.processTree + 3

    def SummaryFile(self, json_data):
        """report.json office 의 generic 필요한 부분 추출
        
        :param dict json_data: report process 객체
        :return: file 카운트.
        """

        generic = json_data['behavior']['generic']

        for i in generic:
            if i['summary'].get('file_created') != None:
                fileCreate = json.dumps(i['summary']['file_created'])
                if ".xsl" in fileCreate.lower():
                    self.xslCount = self.xslCount + 1
                if ".js" in fileCreate.lower():
                    self.jsCount = self.jsCount + 1
                if "msforms.exd" in fileCreate.lower():
                    self.msformsCount = self.msformsCount + 1

    def OfficeMacros(self, json_data):
        """report.json office 의 macro 필요한 부분 추출
        
        :param dict json_data: report process 객체
        :return: macro 추출한 값을 리턴.
        """
        self.macrosCount = len(json_data['static']['office']['macros'])

    def HttpMalCheck(self, json_data):
        """report.json network 의 필요한 부분 추출
        
        :param dict json_data: report process 객체
        :return: network 추출한 값을 배열에 삽입.
        """
        http = json_data['network']['http']
        
        for i in http:
            if i.get('user-agent') == None or 'microsoft' not in i['user-agent'].lower():
                self.httpCount = self.httpCount + 1

    def ApiStats(self, json_data):
        """report.json apistats 의 Nt 객체에서 필요한 부분 추출
        
        :param dict json_data: report process 객체
        :return: api count 추출한 값을 배열에 삽입.
        """
        apistats = json_data['behavior']['apistats']

        for i in apistats:
            if apistats[i].get('NtQueryKey') != None:
                self.ntList[0] = self.ntList[0] + apistats[i]['NtQueryKey']
            if apistats[i].get('NtOpenKey') != None:
                self.ntList[1] = self.ntList[1] + apistats[i]['NtOpenKey']
            if apistats[i].get('NtOpenFile') != None:
                self.ntList[2] = self.ntList[2] + apistats[i]['NtOpenFile']
            if apistats[i].get('NtWriteFile') != None:
                self.ntList[3] = self.ntList[3] + apistats[i]['NtWriteFile']
            if apistats[i].get('NtQueryValueKey') != None:
                self.ntList[4] = self.ntList[4] + apistats[i]['NtQueryValueKey']
            if apistats[i].get('NtDelayExecution') != None:
                self.ntList[5] = self.ntList[5] + apistats[i]['NtDelayExecution']
            if apistats[i].get('NtCreateFile') != None:
                self.ntList[6] = self.ntList[6] + apistats[i]['NtCreateFile']

    def FileStats(self, json_data):
        """report.json summary 의 file 객체에서 필요한 부분 추출
        
        :param dict json_data: report process 객체
        :return: dict 추출한 값을 배열에 삽입.
        """
        behavior = json_data['behavior']['summary']

        if behavior.get('file_created') != None:
            self.fileList[0] = len(behavior['file_created'])
        if behavior.get('file_recreated') != None:
            self.fileList[1] = len(behavior['file_recreated'])
        if behavior.get('dll_loaded') != None:
            self.fileList[2] = len(behavior['dll_loaded'])
        if behavior.get('file_opened') != None:
            self.fileList[3] = len(behavior['file_opened'])
        if behavior.get('file_written') != None:
            self.fileList[4] = len(behavior['file_written'])
        if behavior.get('file_failed') != None:
            self.fileList[5] = len(behavior['file_failed'])

    def DocPrint(self):
        """Parsing 된 데이터 출력

        :return: 없음
        """
        print("processTree : ", self.processTree)
        print("xslCount : ", self.xslCount)
        print("jsCount : ", self.jsCount)
        print("msformsCount : ", self.msformsCount)
        print("macrosCount : ", self.macrosCount)
        print("httpCount : ", self.httpCount)
        print("ntList : ", self.ntList)
        print("fileList : ", self.fileList)


    def parsing(self):
        """ report.json 의 원하는 부분을 추출 하는 로직
            이것을 여기에 넣어야 하는지 고민 하는 중 - d4r6
        
        :return: 없음
        """
        cuckoo_string = ""
        with open(self.path) as json_file: 
            json_data = json.load(json_file) 

            self.ProcessTree(json_data)
            self.SummaryFile(json_data)
            self.OfficeMacros(json_data)
            self.HttpMalCheck(json_data)
            self.ApiStats(json_data)
            self.FileStats(json_data)

