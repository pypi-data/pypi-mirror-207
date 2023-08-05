#
# forked from goodatlas/zeroth
# step3 (step_tmp) script
#


import re
from re import Match

def segment(match: Match[str]) -> str:
  text=match.group(0)
  text=re.sub('([\,\.\'\!\/])', ' ', text)
  return text


def normalize(text: str) -> str:
  # numbers with '.'
  text = re.sub('(?=\S*[A-Z])(?=\S*[\.\,\'])\S*', segment, text)
  text = re.sub('(?=\S*[A-Z])(?=\S*[0-9])\S*', segment, text)

  text = re.sub(r'(\ )+', ' ', text).strip()
  return text
