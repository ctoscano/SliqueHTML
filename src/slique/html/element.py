'''
Created on Jun 23, 2009

@author: ctoscano
'''
import cgi

class element(list):
    '''
    Base class for all html elements
    '''
    ATTRIBUTE_EXCEPTIONS = {'cls':'class', # class is a python keyword
                            'http_equiv':'http-equiv', # - is not allowed
                            'fr':'for',
                            }

    def __init__(self, tag, **attrs):
        '''
        Constructor
        '''
        self.__tag = tag
        self.__parent = None
        self.__attributes = {}
        self.__hasChildren = True
        self.__flags = []
        if len(attrs) > 0: self.set(**attrs)
        
        if tag in ('img', 'input', 'link', 'meta'):
            self.setHasChildren(False)
        
    @property
    def tag(self):
        return self.__tag
        
    @property
    def parent(self):
        return self.__parent
    
    @property
    def attributes(self):
        return self.__attributes
    
    @property
    def flags(self):
        return self.__flags
    
    def setHasChildren(self, boolean):
        '''@param boolean: set to False if doctype, img, or other without end tag'''
        self.__hasChildren = boolean
        
    def __str__(self):
        
        out = []
        inTag = []
        
        for attr in self.attributes:
            value = self.attributes[attr]
            if attr in element.ATTRIBUTE_EXCEPTIONS:
                attr = element.ATTRIBUTE_EXCEPTIONS[attr]
            inTag.append(' %s="%s"' % (attr, value))
            
        for flag in self.flags:
            inTag.append(' %s' % flag)
        
        # Open Tag
        out.append('<%s%s>' % (self.tag, ''.join(inTag)))
        
        if self.__hasChildren:
            # Children
            childStr = self._childrenToStr()
            if childStr != '': out.append(childStr)
            
            # End Tag
            out.append('</%s>'%self.tag)
        
        return ''.join(map(self.strSafe, out))

    @staticmethod
    def strSafe(obj):
        try: return str(obj)
        except UnicodeEncodeError: return unicode(obj)

    def _childrenToStr(self):
        '''Allows subclasses to override the way children are added'''
        return '\n'.join(map(self.strSafe, self))
        
    def __call__(self, **attrs):
        self.set(**attrs)
        return self
    
    def set(self, **attrs):
        '''Set attributes (ex. self.set(id="navBar") or .set(width=2)
        
        Use the keyword 'flag' for attributes without a value
            
        '''
        for attr, value in attrs.items():
            self.attributes[attr] = cgi.escape(unicode(value), quote=True)
        return self
    
    def get(self, attr):
        return self.attributes[attr] if self.attributes.has_key(attr) else None
    
    def addFlag(self, flag):
        '''add to opening tag; like attributes, but without a value
        
        ex. element('input')(type='button').addFlag('disabled').setHasChildren(False)
            => <input disabled type="button">
        '''
        self.__flags.append(flag)
        
    def addClass(self, cls):
        if 'cls' in self.attributes:
            current = self.strSafe(self.attributes['cls']).split(' ')
            if cls in current: return # element is already of class cls
            else: cls = ' '.join(current + [cls])
        self.set(cls=cls)
        
    def removeClass(self, cls):
        if 'cls' in self.attributes:
            current = self.strSafe(self.attributes['cls']).split(' ')
            if cls in current: 
                current.remove(cls)
                if len(current) == 0: self.attributes.remove('cls')
                else: self.set(cls=' '.join(current))
    
    def setParent(self, parent):
        self.removeFromParent()
        self.__parent = parent

    def removeFromParent(self):
        if self.parent is not None and hasattr(self.parent, 'remove'):
            self.parent.remove(self)
        self.__parent = None
            
    def append(self, child):
        '''works for element or text (escaped)'''
        if not isinstance(child, element):
            child = cgi.escape(str(child))
        else:
            child.removeFromParent()
            child.setParent(self)
        super(element, self).append(child)
        return self
    
    def appendHTML(self, html):
        '''Unsafe way of adding un-escaped text'''
        super(element, self).append('%s' % html)
        return self
        
    def add(self, child):
        return self.append(child)
    
    def addHTML(self, html):
        return self.appendHTML(html)
        
    def remove(self, elem):
        #TODO: does not seem to work.
#        pass
        if elem in self:
            super(element, self).remove(elem)
#            import logging
#            logging.debug(elem.__dict__)
