'''
Created on Jun 23, 2009

@author: ctoscano
'''
from slique.html.element import element

class doctype(element):
    '''
    doctype
    
    http://www.w3.org/QA/2002/04/valid-dtd-list.html
    '''

    HTML_4_01_STRICT = '''html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd"'''


    def __init__(self):
        '''
        Constructor of DOCTYPE tags
        
        http://www.w3.org/QA/2002/04/valid-dtd-list.html
        '''
        super(doctype, self).__init__('!DOCTYPE')
        self.addFlag(doctype.HTML_4_01_STRICT)
        self.setHasChildren(False)
        
    def set(self, flag):
        for _flag in self.flags: self.flags.remove(_flag)
        self.addFlag(flag)
