#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade

import Image

import opencv
from opencv import highgui




class MainWindow:
    def __init__(self, file):
        self.widgets=gtk.glade.XML(file)
        self.build_references_to_controls()
        
        self.camera=highgui.cvCreateCameraCapture(0)
        self.widgets.signal_autoconnect(self)

        self.buttonSelectFolder=self.__getitem__('buttonFolder')
        
        
        self.video=self.__getitem__('video')
        self.main_window.show()
    
    def build_references_to_controls(self):
        self.main_window=self.__getitem__('main_window')
        self.buttonStart=self.__getitem__('buttonStart')
        self.buttonStop=self.__getitem__('buttonStart')
        
    
    def __getitem__(self, key):
        return self.widgets.get_widget(key)
        
        
    def startCapture(self, args):
        im=highgui.cvQueryFrame(self.camera)
        area=self.video.window
        gc=area.new_gc()
        pil_image=opencv.adaptors.Ipl2PIL(im)
        pil_image.mode='RGB'
        #pil_image.show()
        area.draw_rgb_image(gc, 0,0,pil_image.size[0],pil_image.size[1], gtk.gdk.RGB_DITHER_NONE, pil_image.tostring())
        
        self.buttonStart.set_sensitive(0)
        self.buttonStop.set_sensitive(1)
    
    def stopCapture(self, args):
        self.buttonStart.set_sensitive(1)
        self.buttonStop.set_sensitive(0)
        
    def selectFolder(self, args):
        print "Elgi"
    def main_window_destroy_cb(self,args):
        gtk.main_quit()    


if __name__ == '__main__':
    window=MainWindow('interface.glade')
    gtk.main()