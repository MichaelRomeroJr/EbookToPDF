# -*- coding: utf-8 -*-
import os
import TurnPage

def Requirements():      
    """Create save directory for images and pdf """
    PathToDesktop = input("Enter path to desktop: ")
    DirectoryPath = PathToDesktop + '/NewFolder/'
    
    if not os.path.exists(DirectoryPath):
        os.makedirs(DirectoryPath)

    #Number of pages of pdf
    NumberofPages = input("Enter number of pages: ")
    PageCount = int(NumberofPages)
    
    #Get position of "Turn Page" button 
    print("Click 'next page' button on eReader to identify x,y coordinates" +
          "(click next page once then toggle back to cover page of book)")
    XCoordinate, YCoordinate = TurnPage.GetTurnPageCoordinates()
   
    return DirectoryPath, PageCount, XCoordinate, YCoordinate