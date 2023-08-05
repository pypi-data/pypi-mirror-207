import re
import unicodedata
from .normalizer import step1, step2, step3, step4

#
# forked from openai/whisper
#

# non-ASCII letters that are not separated by "NFKD" normalization
ADDITIONAL_DIACRITICS = {
  "œ": "oe",
  "Œ": "OE",
  "ø": "o",
  "Ø": "O",
  "æ": "ae",
  "Æ": "AE",
  "ß": "ss",
  "ẞ": "SS",
  "đ": "d",
  "Đ": "D",
  "ð": "d",
  "Ð": "D",
  "þ": "th",
  "Þ": "th",
  "ł": "l",
  "Ł": "L",
}


def remove_symbols_and_diacritics(s: str, keep=""):
  """
  Replace any other markers, symbols, and punctuations with a space,
  and drop any diacritics (category 'Mn' and some manual mappings)
  """
  return "".join(
    c
    if c in keep
    else ADDITIONAL_DIACRITICS[c]
    if c in ADDITIONAL_DIACRITICS
    else ""
    if unicodedata.category(c) == "Mn"
    else " "
    if unicodedata.category(c)[0] in "MSP"
    else c
    for c in unicodedata.normalize("NFKD", s)
  )


def remove_symbols(s: str):
  """
  Replace any other markers, symbols, punctuations with a space, keeping diacritics
  """
  return "".join(
    " " if unicodedata.category(c)[0] in "MSP" else c
    for c in unicodedata.normalize("NFKC", s)
  )

class ZerothKoreanNormalizer:
  """ Text Normalizer for Korean Text
  
  """
  def __init__(self, remove_diacritics: bool = False, split_letters: bool = False):
    self.normalizers = [step1.normalize, step2.normalize, step3.normalize, step4.normalize]
    self.clean = (
      remove_symbols_and_diacritics if remove_diacritics else remove_symbols
    )
    self.split_letters = split_letters

  def __call__(self, s: str, steps=4):
    """_summary_

    Args:
      s (str): input korean text
      
      steps (int, optional): `Zeroth` script processes input string up to 4 steps. 
      This argument specifies how many steps it applies to input text. Defaults to 4.

    Returns:
      _type_: Normalized input text
    """
    
    if steps < 1: steps = 1 
    if steps > 4: steps = 4
    
    for i in range(steps):
      s = self.normalizers[i](s)
    
    s = re.sub(r'(\ )+', ' ', s).strip()
    return s
  
