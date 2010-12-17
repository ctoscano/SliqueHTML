'''
Created on Jun 23, 2009

@author: ctoscano
'''
from slique.html.element import element

PACKAGE = 'slique.html'

class html(object):
    def __getattr__(self, tag):
        if tag in ('ul', 'table'):
            modelClass = __import__(PACKAGE + '.' + tag, 
                                     globals=globals(), 
                                     locals=locals(), 
                                     fromlist=[tag]).__dict__[tag]
            out = modelClass()
        else:
            modelClass = element
            out = modelClass(tag)
            
        return out
    
new = html()