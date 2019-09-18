# -*- coding: utf-8 -*-
from PIL import Image

def GetImages(directory, count):
    images = []
    for i in range(2,count):
        #Start on Page 2 since we'll make the pdf with Page 1 and append pages 2-n
        path = directory + str(i) + '.jpeg'
        image = Image.open(path)
        images.append(image)

    return images

def MakePDF(directory, count):
    coverpath = directory + '1' + '.jpeg'
    cover = Image.open(coverpath) #First Image of PDF    
    pdf_filename = directory + "/Book.pdf" #Address to save PDF    
    paths = GetImages(directory, count) #Paths of images to append to Cover image
    cover.save(pdf_filename, "PDF" ,resolution=100.0, save_all=True, append_images=paths) # Save as PDF
    
    return