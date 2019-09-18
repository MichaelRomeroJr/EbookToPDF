# -*- coding: utf-8 -*-
import os
import TurnPage

def Requirements():      
    """Confirm dependent libraries"""
    try: 
        import mss
    except:
        print("import mss fail")
    try:
        import PyUserInput
    except:
        print("import PyUserInput fail")
    
    """Create save directory for images and pdf """
    PathToDesktop = input("Enter path to desktop: ")
    DirectoryPath = PathToDesktop + '/NewFolder/'
    
    if not os.path.exists(DirectoryPath):
        os.makedirs(DirectoryPath)

    """Get number of pages of eBook"""
    NumberofPages = input("Enter number of pages: ")
    PageCount = int(NumberofPages)
    
    """Get positino of 'turn page' button of eBook"""
    print("Click 'next page' button on eReader to identify x,y coordinates" +
          "(click next page once then toggle back to cover page of book)")
    XCoordinate, YCoordinate = TurnPage.GetTurnPageCoordinates()
   
    return DirectoryPath, PageCount, XCoordinate, YCoordinate
