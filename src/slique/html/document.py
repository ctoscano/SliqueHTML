'''
Created on Jun 23, 2009

@author: ctoscano
'''
from slique.html.element import element
from slique.html.head import head
from slique.html.doctype import doctype

class document(list):
    '''
    root document containing doctype, head, and body
    '''


    def __init__(self, ie_compatability_mode=False):
        '''
        Constructor
        '''
        self.__doctype = doctype()
        self.append(self.doctype)
        
        self.__html = element('html')
        self.append(self.html)
        
        self.__head = head()
        self.html.append(self.head)
        
        self.__body = element('body')
        self.html.append(self.body)
        
        if ie_compatability_mode:
            self.head.appendHTML('''<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />''')
        
    @property
    def doctype(self):
        return self.__doctype
    
    @property
    def html(self):
        return self.__html
    
    @property
    def head(self):
        return self.__head
    
    @property
    def body(self):
        return self.__body
        
    def __str__(self):
        return '\n'.join(map(element.strSafe, self))
