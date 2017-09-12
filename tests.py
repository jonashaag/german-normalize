# encoding: utf-8
from __future__ import unicode_literals
from german_normalize import normalize


def test_non_lexicographic():
    assert normalize(u'Naïve Café üäöß ẞ') == 'Naive Cafe ueaeoess SS'


def test_lexicographic():
    assert normalize(
        u'Naïve Café üäöß ẞ', lexicographic=True) == 'Naive Cafe uaoss SS'

def test_heuristic_case():
    assert normalize(u'Äpfel SOẞE') == 'AEpfel SOSSE'
    assert normalize(u'Äpfel SOẞE', heuristic_case=True) == 'Aepfel SOSSE'
