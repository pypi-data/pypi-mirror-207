#
# forked from goodatlas/zeroth
# 

import re
from . import at_unicode

def normalize(text: str) -> str:
  # separator (conventions)
  text = re.sub('['+re.escape(at_unicode.separators)+']','\n', text)

  # remove bracked contents 
  text = re.sub('\([^\)]+\)', '', text)
  text = re.sub('\[[^\]]+\]', '', text)
  text = re.sub('【[^】]+】', '', text)
  text = re.sub('\<[^\>]+\>', '', text)

  # handle apostrophe
  quotes = at_unicode.apostrophe + at_unicode.quatation
  text = re.sub('([a-zA-Z])['+re.escape(quotes)+']([a-zA-Z])', '\\1<apostrophe>\\2', text)
  text = re.sub('['+re.escape(quotes)+']', '', text)
  text = re.sub('<apostrophe>', '\'',text)

  # replace various percent into one 
  text = re.sub('['+re.escape(at_unicode.percents)+']', '%' ,text)

  # miscellaneous
  text = re.sub('%p', '% 포인트', text)
  text = re.sub('±', '플러스 마이너스', text)
  text = re.sub('[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]*',' ', text)   # delete e-mail
  
  # remove chinese and japanese characters
  text = re.sub(at_unicode.chinese, '', text)
  text = re.sub(at_unicode.japanese, '', text)
  
  # segment b/w Hangul and non-Hangul
  text = re.sub(r"([가-힣])([^ 가-힣])",r"\1 \2", text)
  text = re.sub(r"([^ 가-힣])([가-힣])",r"\1 \2", text)

  # segment b/w numerices and non-numerics
  text = re.sub('([0-9])([^ \.\,0-9])', '\\1 \\2', text)
  text = re.sub('([^ \+\-\.\,0-9])([0-9])', '\\1 \\2', text)

  # Leave only valid characters
  text = re.sub(at_unicode.invalids_chars, ' ', text)

  # remove repeated valid symbols
  text = re.sub('(['+re.escape(at_unicode.valids)+'])+', '\\1', text)

  # make valid symbols, except puctuations, as a unique word
  symbols = at_unicode.measureUnits + at_unicode.percents + at_unicode.currencies + at_unicode.userDefines
  regexEpr = r"([" + re.escape(symbols) + "])"
  text = re.sub(regexEpr, ' \\1 ', text)

  # remove spaces before puctuations 
  #text = re.sub('\s+(['+re.escape(at_unicode.puctuations)+'])', '\\1', text)

  # segment sentences
  text = re.sub('([가-힣])\s*\.', '\\1.\n', text)

  # segment sentences 2
  text = re.sub('([가-힣])\s*([\.?!])\s*([^가-힣]+ )', '\\1\\2\n\\3', text)
  
  # segment sentences 3
  # / (not readable)
  text = re.sub('([가-힣])\s+[/=:]\s+([가-힣])', '\\1\n\\2', text)
  text = re.sub('([a-zA-Z])\s+[/=:]\s+([가-힣])', '\\1\n\\2', text)
  text = re.sub('([가-힣])\s+[/=:]\s+([a-zA-Z])', '\\1\n\\2', text)
  text = re.sub(r'(\ )+', ' ', text).strip()
  return text
