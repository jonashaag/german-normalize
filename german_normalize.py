# encoding: utf-8
from __future__ import unicode_literals
import unicodedata


def normalize(text, lexicographic=False):
    text = text.replace('ß', 'ss').replace('ẞ', 'SS')
    if not lexicographic:
        for original, replacement in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'),
                                      ('Ä', 'AE'), ('Ö', 'OE'), ('Ü', 'UE')):
            text = text.replace(original, replacement)
    return unicodedata.normalize('NFKD', text).encode('ascii',
                                                      'ignore').decode()
