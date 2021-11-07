import json

class Convert():
    def __init__(self) :
        with open('MorseCode.json', encoding='utf-8') as Code:
            self.morseCodeDic=json.load(Code)

    def textConvertMorseCode(self,text):
        if text:
            result=''
            text=text.upper()
            for char in text:
                morseCode=self.morseCodeDic.get(char)
                result+=morseCode+' ' if morseCode else ''

            return result
        else:
            return 'Please input some words.'

    def get_English_from_morseCode(self,d, val):
        for k, v in d.items():
            if v.strip() == val.strip():
                return k
        return ''

    def morseCodeConvertText(self,morsetext):
        if morsetext:
            result=''
            codeList=morsetext.split()
            for code in codeList:
                result+=self.get_English_from_morseCode(self.morseCodeDic,code) if code else ''
            return result

    def convertProcess(self,typeChoose='english text'):
        ''' type e:english text ,m:morse code '''
        if typeChoose.lower()=='english text' or typeChoose.lower()=='morse code':
            userInput=input('Please Enter Text :')
            respone=''
            if typeChoose.lower()=='english text':
                respone=self.textConvertMorseCode(userInput) 
            elif typeChoose.lower()=='morse code':
                respone=self.morseCodeConvertText(userInput)
            print(respone)
        else:
            print("Please enter English text or Morse code.")


    def userInputProcess(self):
        userInputChoose=input('Do you want to enter English text or Morse code? (if entering Morse code,please using blank to separate symbol.)')
        if userInputChoose:
            self.convertProcess(typeChoose=userInputChoose)
            userInputExit=input("If you don't want to continue? Please enter N.")
            if userInputExit.lower()=='n':
                return 'n' 
