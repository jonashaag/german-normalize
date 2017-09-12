# encoding: utf-8
from __future__ import unicode_literals
import re
import unicodedata


def normalize(text, lexicographic=False, heuristic_case=False):
    assert not heuristic_case or not lexicographic, "'heuristic_case' conflicts with 'lexicographic'"

    text = text.replace('ß', 'ss').replace('ẞ', 'SS')
    if not lexicographic:
        if heuristic_case:
            text = re.sub('Ä(?=[a-z])', 'Ae', text)
            text = re.sub('Ö(?=[a-z])', 'Oe', text)
            text = re.sub('Ü(?=[a-z])', 'Ue', text)
        for original, replacement in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'),
                                      ('Ä', 'AE'), ('Ö', 'OE'), ('Ü', 'UE')):
            text = text.replace(original, replacement)
    return unicodedata.normalize('NFKD', text).encode('ascii',
                                                      'ignore').decode()
