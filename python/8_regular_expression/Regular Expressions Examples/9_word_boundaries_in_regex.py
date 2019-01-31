# Match word boundaries
"""
    Word boundaries \b are commonly used to detect and match the beginning or end of a word.
    
    That is, one side is a word character and the other side is whitespace and vice versa.

    For example, the regex \btoy will match the ‘toy’ in ‘toy cat’ and not in ‘tolstoy’.
    
    In order to match the ‘toy’ in ‘tolstoy’, you should use toy\b
    
    Can you come up with a regex that will match only the first ‘toy’ in ‘play toy broke toys’? (hint: \b on both sides)

    Likewise, \B will match any non-boundary.
    
    For example, \Btoy\B will match ‘toy’ surrounded by words on both sides, as in, ‘antoynet’.
"""
import re

word_bound1 = "toy cat"

print re.findall('\btoy', word_bound1)
