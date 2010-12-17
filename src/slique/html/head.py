'''
Created on Jun 23, 2009

@author: ctoscano
'''
from slique.html.element import element

class head(element):
    '''
    element with head tag forces mandatory title child
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(head, self).__init__('head')
        self.__title = element('title')
        self.append(self.title)
        
    @property
    def title(self):
        return self.__title