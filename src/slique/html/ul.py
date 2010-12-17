'''
Created on Jun 24, 2009

@author: ctoscano
'''
from slique.html.element import element

class ul(element):
    '''
    simplifies adding li to ul
    '''


    def __init__(self, **attrs):
        '''
        Constructor
        '''
        super(ul, self).__init__('ul')
        self.set(**attrs)
        
    def _childrenToStr(self):
        '''Places children between li tags'''
        
        def envelope(item):
            if hasattr(item, 'tag') and item.tag == 'li':
                return '%s' % item                       # Avoid redundant li tag
            return '<li>%s</li>' % item    
        
        return '\n'.join(map(envelope, self))
        