'''
Created on Feb 20, 2010

@author: ctoscano
'''
from slique.html.element import element
from slique.html.html import new

class table(element):
    '''
    classdocs
    '''


    def __init__(self, **attrs):
        '''
        Constructor
        '''
        super(table, self).__init__('table', **attrs)
        self.set(**attrs)
        self.__tbody = new.tbody
        self.append(self.__tbody)
        self.nextRow()
        
    @property
    def tbody(self):
        return self.__tbody
    
    def getRow(self, index):
        return self.tbody[index]
    
    def add(self, item):
        assert(hasattr(item, 'tag') and item.tag == 'tr')
        self.tbody.append(item)
        
    def addCell(self, item='', as_html=False, **attrs):
        td = new.td(**attrs)
        if as_html:
            td.appendHTML(item)
        else:
            td.append(item)
        self.tbody[-1].append(td)
        return td
    
    def nextRow(self, **attrs):
        self.tbody.append(new.tr(**attrs))
    
class HorizontalTable(table):
    
    def __init__(self, **attrs):
        '''
        Constructor
        '''
        super(HorizontalTable, self).__init__(**attrs)
        
    @property
    def row(self):
        return self.tbody[0]
        
    def add(self, item, valign='top', **attrs):
        if (hasattr(item, 'tag') and item.tag == 'tr'):
            super(HorizontalTable, self).add(item)
        else: 
            self.row.append(new.td(valign=valign, **attrs).append(item))
        
    def insert(self, item, index):
        self.row.insert(index, new.td().append(item))
        
class VerticalTable(table):
    
    def __init__(self, **attrs):
        '''
        Constructor
        '''
        super(VerticalTable, self).__init__(**attrs)
        
        
    def add(self, item):
        self.addCell(item)
        self.nextRow()
        
    def insert(self, item, index):
        self.row.insert(index, new.tr().append(new.td().append(item)))
        
