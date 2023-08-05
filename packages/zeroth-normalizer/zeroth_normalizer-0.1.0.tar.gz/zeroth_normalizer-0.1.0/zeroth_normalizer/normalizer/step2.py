#
# forked from goodatlas/zeroth
#

import re 
from . import at_unicode

def normalize(text: str) -> str:
  text = text.strip()
  # remove meaningless start
  text = re.sub('^[^0-9a-zA-Z가-힣]+', '', text) 
  
  # delete no-Hangul line
  text = re.sub('^([^가-힣]+)$', ' ', text)

  # ignore sentences with urls
  if re.search('www', text): return text 
  if re.search('http', text): return text 
  if re.search('ftp', text): return text 

  # .
  text = re.sub('\.\s*$', '.', text)
  
  # ;
  text = re.sub(';', '', text)

  # ignore sentences with multi-variate pronunciation symbols
  # too many, need to another approach
  if re.search('[/\-=:~+]', text): return text

  # remove ? !
  #text = re.sub('[!?]', ' ', text)
  text = re.sub('\s+([\.\,\'\!\?])', '\\1 ', text)

  # . , should be removed after treating numerics
  
  # filter sentence with [a-z] characters
  #  not convertable into Korean now, need transliteration
  regexEpr = r"^[ \.,?!가-힣0-9A-Z" + re.escape(at_unicode.valids) + r"]+$"
  if re.match(regexEpr, text):
    text = re.sub(r'(\ )+', ' ', text).strip()

  return text

