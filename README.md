# `german_normalize`

Python module to normalize ä ü ö ß -> a(e) u(e) o(e) ss (DIN 5007).

Supports both Python 2 and 3.

Example:

```py
from german_normalize import normalize


normalize(u'Naïve Café Äpfel ẞ')
# => 'Naive Cafe AEpfel SS'


normalize(u'Naïve Café Äpfel ẞ', lexicographic=True)
# => 'Naive Cafe Apfel SS'


normalize(u'Naïve Café Äpfel ẞ', heuristic_case=True)
# => 'Naive Cafe Aepfel SS'
```
