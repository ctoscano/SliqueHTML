

from slique.html.table import table

class DockPanel(table):
    '''
    
    __________________________________
    |                                |
    |________________________________|  # top
    |       |_______________|        |  # left; inner_top; right
    |       |               |        |  # left; center; right
    |       |_______________|        |  
    |_______|_______________|________|  # left; inner_bottom; right 
    |                                |  # bottom
    |________________________________|
    
    '''
    
    TOP = 'top'
    LEFT = 'left'
    RIGHT = 'right'
    INNER_TOP = 'inner_top'
    INNER_BOTTOM = 'inner_bottom'
    CENTER = 'center'
    BOTTOM = 'bottom'
    
    def __init__(self, **attrs):
        '''
        Constructor
        '''
        super(DockPanel, self).__init__(**attrs)
        
        self.__top = self.addCell(valign='top', colspan=3)
        self.nextRow()
        self.__left = self.addCell(valign='top', rowspan=3)
        self.__inner_top = self.addCell(valign='top')
        self.__right = self.addCell(valign='top', rowspan=3)
        self.nextRow()
        self.__center = self.addCell(valign='top')
        self.nextRow()
        self.__inner_bottom = self.addCell(valign='top')
        self.nextRow()
        self.__bottom = self.addCell(valign='top', colspan=3)
        
        self.__dict = {
                       DockPanel.TOP:self.__top,
                       DockPanel.LEFT:self.__left,
                       DockPanel.RIGHT:self.__right,
                       DockPanel.INNER_TOP:self.__inner_top,
                       DockPanel.INNER_BOTTOM:self.__inner_bottom,
                       DockPanel.CENTER:self.__center,
                       DockPanel.BOTTOM:self.__bottom
                       }
    
    def add(self, item, location):
        self.__dict[location].append(item)
        