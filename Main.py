# -*- coding: utf-8 -*-
import Screenshot
import TurnPage
import Setup
import ImagesToPDF

def Run():
    DirectoryPath, NumberofPages, XCoordinate, YCoordinate = Setup.Requirements()
    
    for i in range(1, NumberofPages+1): #Turn each page and grab screenshot as jpeg
        ImagePath = DirectoryPath + '/' + str(i)+ '.jpeg'
        Screenshot.HDCapture(ImagePath)
        TurnPage.Click(XCoordinate, YCoordinate)
   
    ImagesToPDF.MakePDF(DirectoryPath, NumberofPages)
    return

Run()