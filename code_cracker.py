#!/bin/env python
# -*- coding: iso-8859-15 -*-

message="""
o eqf'z rg ziol qfndgkt. it ktyxltl zg wtsotct qfnziofu ol vkgfu...
o afgv.r
oz vgf'z wt dxei sgfutk. it'ss iqct zg ktqsomt zitf.
hkgdolt?
qkt ngx of wtr?
fg, o'd of zit aozeitf.
ug gxz gf zit hgkei qfr eqss dt. it vgf'z itqk.
... qskouiz.
uoct dt q dofxzt.
"""

replace_map={'z':'t','e':'c','q':'a','f':'n','o':'i','i':'h','t':'e','a':'k','l':'s',
             'v':'w','g':'o','u':'g','k':'r','y':'f','n':'y','d':'m','r':'d','x':'u',
             's':'l','c':'v','w':'b','h':'p'}
# message="""
# o'ct vkozztf lgdt hnzigf zg lgsct oz
# """
for char in message:
    if (char in replace_map):
        new_char="\033[1;32;40m" + replace_map[char] + "\033[1;37;40m"
    else:
        new_char=char
    print(new_char, end="")

'''encode'''
code_map = dict([(value, key) for key, value in replace_map.items()]) 
message="i've written some python to solve it"
for char in message:
    if (char in code_map):
        new_char="\033[1;32;40m" + code_map[char] + "\033[1;37;40m"
    else:
        new_char=char
    print(new_char, end="")
