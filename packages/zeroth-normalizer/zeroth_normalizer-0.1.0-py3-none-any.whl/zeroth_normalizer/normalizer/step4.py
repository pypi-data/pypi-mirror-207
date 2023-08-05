import re
from re import Match
import sys

MAX_NUMBER  = 9999999999999999

readTextUnit  = [['','만','억','조'], '십', '백', '천']
readText      = ['영','일','이','삼','사','오','육','칠','팔','구', '']
readNumber    = ['공','일','이','삼','사','오','육','칠','팔','구', '']
readCountUnit = ['','열','스물','서른','마흔','쉰','예순', '일흔', '여든','아흔']
readCount     = [['','하나','둘','셋','넷','다섯','여섯','일곱','여덟','아홉'],
                 ['','한','두','세','네','다섯','여섯','일곱','여덟','아홉']]

COUNT_UNIT = [
'배','채','개','시','말','벌','축','톳','손','살','죽','쾌','닢','병','건','속','주', \
'망','포','피','미','팩','통','줄','봉','단','판','모','척','번','잔','장','쌍','명', \
'마리','가지','방울','자루','켤레','사람','박스','묶음','보루','봉지','포기','시루',  \
]

def number2readNumber(numbers: str):
    result=[]
    for number in reversed(numbers):
        idxNum = int(number)
        rNum = readNumber[idxNum]
        #rNum = "["+readNumber[idxNum]+"]"
        result.insert(0, rNum)
    return " ".join(result)

# 숫자를 서수방식으로 읽기
#  1~99 사이 숫자만 지원 
#  Option
#     0: 뒤에 단위가 없을 때 (default)
#     1: 뒤에 단위가 있는 경우 사용 
def number2readCount(numbers: str, option=1):
    # numbers expected as a text variable 
    cnt=0
    result=[]
    if int(numbers) > 99:
        sys.exit('Out-of-range: read count range is 1~99')
    for number in reversed(numbers):
        idxNum = int(number)
        if cnt == 0:
            res=readCount[option][idxNum]
        else:
            res=readCountUnit[idxNum]
        #print(number, res)     
        if res:
            #res = '['+res+']'
            result.insert(0, res)
        cnt +=1
    return result
    #return " ".join(result)


# 숫자를 기수방식을 읽기
# 최대숫자 9999,9999,9999,9999
# option1
#    0: 모두 기수방식으로 읽음 (default)
#    1: 백자리 아래를 서수로 읽음
# option2 
#    number2readCount option 참조
#
def number2readText(numbers: str, option1=0, option2=0):
    # numbers expected as a text variable 
    cnt=0
    result=[]
    # pre-processing
    numbers = numbers.lstrip("0")
    if numbers == '':
        numbers = "0"
    if int(numbers) > MAX_NUMBER:
        return number2readNumber(numbers)
    for number in reversed(numbers):
        idxNum = int(number)
        prec   = cnt%4
        if prec == 0:
            # for every 4th location
            rNum = readText[idxNum]
            rLoc =  ''
            if cnt != 0: # 1's location ignore
                rLoc = readTextUnit[0][cnt//4]
                #rLoc = "{"+readTextUnit[0][cnt//4]+"}"
            res  = rNum +' '+  rLoc
        else:
            rNum = readText[idxNum]          # 일, 이 ...
            rLoc = readTextUnit[cnt%4]       # 천, 백 ... 
            #rLoc = "("+ readTextUnit[cnt%4] +")"       # 천, 백 ... 
            res  = rNum + rLoc
        
        # Exceptions for '영'
        if rNum in ['영', '[영]']:
            if len(numbers) != 1:
                #if rLoc in ['{만}', '{억}', '{조}']:
                if rLoc in ['만', '억', '조']:
                    cLoc=len(numbers)-cnt
                    if numbers[cLoc-4:cLoc] == '0000':
                        res=''
                    else:
                        res=rLoc
                else:
                    res=''
            else:
                res=rNum

        # Exceptions for '일'
        if rNum == '일':
            if cnt not in [12, 8, 4, 0]:
                res=rLoc
            else:
                if cnt == 4 and len(numbers) == 5:
                    res=rLoc

        #print(res, number, prec, cnt)
        if res: 
            if prec != 0:
                #res = '['+res+']'
                res = res
            result.insert(0, res)
        cnt +=1
    if option1:
        rStr = number2readCount(numbers[-2:], option2)
        result[-2:]=rStr

    # 조/억/만 단위 띄어쓰기
    outext = " ".join(result)
    return outext
    #outList = list(outext)
    #if '조' in outList:
    #    outList.insert(outList.index('조')+1,' ')
    #if '억' in outList:
    #    outList.insert(outList.index('억')+1,' ')
    #if '만' in outList:
    #    outList.insert(outList.index('만')+1,' ')
    #return "".join(outList)



def convNumType3(match: Match[str]) -> str:
    #regex: '(\-?)(\d+)(\.)(\d+)'

    text = '['
    if match.group(1):
        text += '마이너스 '
    g2 = number2readText(match.group(2), 0, 0)
    text += g2
    g4 = number2readNumber(match.group(4))
    text += ' 쩜|. '+g4
    return text + ']'

def convNumType4(match: Match[str]) -> str:
    #regex: '([\d\.]+)'

    text = '['
    tNum=match.group(0).split('.')

    for elem in tNum:
        text += number2readNumber(elem)+" "
    return text + ']'


def convNumType5(match: Match[str]) -> str:
    opt = 0
    for elem in COUNT_UNIT:
        # pitfall '미' is in '밀리미터' ... 
        if elem in match.group(7):
            opt = 1

    text=' '
    if match.group(1):
        g1 = number2readText(match.group(1), opt, opt)
        text += g1 + ' '
    if int(match.group(5)) - int(match.group(1)) > 1:
        text += " 에서"
    g5 = number2readText(match.group(5), opt, opt)
    text += ' ' + g5 + ' ' + match.group(7)
    return text

def convNumType6(match: Match[str]) -> str:
    opt = 0
    for elem in COUNT_UNIT:
        if elem in match.group(3):
            opt = 1

    text=' '
    g1 = number2readText(match.group(1), opt, opt)
    text += g1 + ' '
    if match.group(3):
        text += match.group(3)
    return text

def convNumType9(match: Match[str]) -> str:
    text=' '
    #g1 = number2readText(match.group(1), 0, 0)
    g1 = number2readNumber(match.group(1))
    text += g1 + ' '
    return text

def convNum_1(match: Match[str]) -> str:
    matchedTxt = match.group(0)
    tlist = matchedTxt.split('.')
    text  = ''
    if len(tlist) == 3 and  len(str(int(tlist[0]))) == 4:
        text += number2readText(tlist[0].strip(), 0, 0)+" 년 "
        text += number2readText(tlist[1].strip(), 0, 0)+" 월 "
        text += number2readText(tlist[2].strip(), 0, 0)+" 일"
    else:
        for elem in tlist[:-1]:
            text += number2readText(elem.strip(), 0, 0)+' 쩜 '
        text += number2readText(tlist[-1].strip(), 0, 0)
    return text

def convNum_2(match: Match[str]) -> str:
    matchedTxt = match.group(1)
    tlist = matchedTxt.split('.')
    text = ''
    for elem in tlist[:-1]:
        text += number2readText(elem.strip(), 0, 0)+' 쩜 '
    #text += number2readText(tlist[-1].strip(), 0, 0)
    text += number2readNumber(tlist[-1].strip())
    return text+" "+match.group(2)

def convNum_3(match: Match[str]) -> str:
    matchedTxt = match.group(0)
    tlist = matchedTxt.split('.')
    text = ''
    for elem in tlist[:-1]:
        text += number2readText(elem.strip(), 0, 0)+' [쩜] '
    text += number2readNumber(tlist[-1].strip())
    return text

def convNum_4(match: Match[str]) -> str:
    matchedTxt = match.group(0)
    tlist = matchedTxt.split('-')
    text  = ''
    for elem in tlist[:-1]:
        text += number2readText(elem.strip(), 0, 0)+' '
    text += number2readText(tlist[-1].strip(), 0, 0)
    return text

def convNum_5(match: Match[str]) -> str:
    matchedTxt = match.group(1)
    return number2readText(matchedTxt, 0, 0)+" "

def convNum_6(match: Match[str]) -> str:
    matchedTxt = match.group(1)
    return " [쩜] "+number2readNumber(matchedTxt)

# could be a number with count-unit, leave it to lexicon dictionary
def convNum_7(match: Match[str]) -> str:  
    return "["+match.group(1)+"]"+match.group(2)


def convNum_8(match: Match[str]) -> str:
    matchedTxt = match.group(1)
    text = number2readText(matchedTxt, 0, 0)+" "
    #if match.group(2):
    #    text += match.group(2)
    return text

def convNumType8(match: Match[str]) -> str:
    num = match.group(1)
    tNum = num.split(',')
    num = "".join(tNum)
    return " "+num+" "

def normalize(text: str) -> str:
  #-----------
  # numbers with ,: 123,456 --> 123456
  text = re.sub('([^ 0-9]),([^ 0-9])', '\\1, \\2', text) 
  text = re.sub('([0-9]),([^ 0-9])', '\\1, \\2', text) 
  text = re.sub('([^ 0-9]),([0-9])', '\\1, \\2', text) 
  #text = re.sub('(?=.*[0-9].*)([0-9,]+)', convNumType8, text)
  text = re.sub('\s([0-9][,0-9]{3,}[0-9])\s', convNumType8, text)
  #text = re.sub(',', ' ', text)


  # numbers with '.'
  text = re.sub('\d+\.\s*\d+(\.\s*\d+)+', convNum_1,text)       # 2016.1.2 or 1.2.1 
  text = re.sub('(\d+\.\d+)([^ 0-9A-Za-z]+)', convNum_2,text)  # 1.23%    [일] 쩜 [이] [삼]
  text = re.sub('\d+\.\d+', convNum_3,text)                    # 1.23     [일] [쩜] [이] [삼], 3.1 운동
  #text = re.sub('(\d+)\.', convNum_5,text)                        # 1.
  #text = re.sub('\.', ' ', text) 
  text = re.sub('\s\.([0-9]+)', convNum_6,text)                 # .234

  # numbers possively with count-unit (수량사)
  #   leave it as a numeric  
  #   ex.  배추 1 박스 --> 배추 [1] 박스
  text = re.sub('\\b(\d{1,2})(\s*[^ \]0-9]+)', convNum_7, text)
  
  # segment (just for sure)
  text = re.sub('(\S)\[', '\\1 [', text)
  text = re.sub('\](\S)', '] \\1', text)

  ## convert all numeric into korean Numbers if there is no surrounding brackets 
  #words=text.split()
  #for i in range(len(words)):
  #    if words[i][0] != '[' and words[i][-1] != ']':
  #        words[i] = re.sub('(\d+)(\S*)', convNum_8 , words[i])
  #text= ' '.join(words)+'\n'
  text  = re.sub('(\\b\d{3,}\\b)', convNum_8 , text)

  ## remove brackets and . ,
  ##text = re.sub('[\[\]\.,]', '', text)
  text = re.sub('[\[\]]', '', text)

  text = re.sub('[\.\,\'\?\!]',' ', text)

  # segment sentences
  #text = re.sub('\s+(['+re.escape(at_unicode.puctuations)+'])', '\\1', text)
  #text = re.sub('([가-힣])\s*\.', '\\1.\n', text)
  #text = re.sub('([가-힣])\s*([\.?!])\s*([^가-힣]+ )', '\\1\\2\n\\3', text)

  # remove repeated characters 
  text = re.sub('(.)\\1{4,}', '\\1\\1\\1', text)
  
  text = re.sub(r'(\ )+', ' ', text).strip()
  return text
