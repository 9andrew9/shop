# -*- coding: utf-8 -*-
from slugify import slugify

d = """ """
with open('text.txt', "r") as f:
    for i in f:
        a = slugify(i)
        d += (a + '\n')
print(d)
