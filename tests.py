# encoding: utf-8
from __future__ import unicode_literals
from german_normalize import normalize


def test_non_lexicographic():
    assert normalize(u'Naïve Café üäöß ẞ') == 'Naive Cafe ueaeoess SS'


def test_lexicographic():
    assert normalize(
        u'Naïve Café üäöß ẞ', lexicographic=True) == 'Naive Cafe uaoss SS'
