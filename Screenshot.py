# -*- coding: utf-8 -*-
import mss

def HDCapture(path):
    """Take hi-res screenshot of monitor and save .jpeg to path
        Aviod using numpy to preserve image quality for the pdf"""
    with mss.mss() as sct:
        sct.shot(mon=1, output=path) #-1 means first monitor
    return