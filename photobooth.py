import os, time, sys
from PIL import Image
import time
import random
from datetime import datetime
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image
from kivy.uix.carousel import Carousel
from kivy.clock import Clock
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import glob

sys.path.append("/home/tgrecojr")





photoPath = "/Users/tgrecojr/Downloads/photos/"


cam = Camera()        #Get the camera
cam=Camera(resolution=(3280,2464),size_hint=(1, .8))
sm = ScreenManager(transition=SlideTransition(),duration=10)
carousel = Carousel(direction='right',loop='true',size_hint=(1, .8))

# Callback function for photo button
def photo_callback(obj):
        #photoName = time.strftime("%Y%m%d%H%M%S") + "_photobooth.jpg"
        #cam.texture.save("IMG_" + photoName, flipped=False)
        sm.current = 'MessageScreen'
        Clock.schedule_once(change_screen,3)

def change_screen(obj):
    sm.current = 'PhotoScreen'

def gallery_callback(obj):
    pathname = photoPath + '*.jpg'
    for name in glob.glob(pathname):
        theimage = Image(source=name)
        carousel.add_widget(theimage)
    sm.current = 'GalleryScreen'

def gallery_back_callback(obj):
    sm.current = 'PhotoScreen'

class MyApp(App):



        #photo = kivyImage(source="/Users/tgrecojr/Downloads/thumbnail.jpg",size_hint=(.2, 1))
        cam.play = True  # Start the camera
        #cam.size_hint(.8,1)
        def build(self):

                photoscreen = Screen(name='PhotoScreen')
                sm.add_widget(photoscreen)
                messagescreen = Screen(name='MessageScreen')
                sm.add_widget(messagescreen)
                galleryscreen = Screen(name='GalleryScreen')
                sm.add_widget(galleryscreen)

                # Set up the layout
                photobox = StackLayout(padding=0,spacing=0)

                # Create the UI objects (and bind them to callbacks, if necessary)
                galleryButton = Button(text="Photo Gallery", size_hint=(.5, .2))
                galleryButton.bind(on_press=gallery_callback)
                photoButton = Button(text="Take Photos",size_hint=(.5, .2)) # Button: 20% width, 100% height
                photoButton.bind(on_press=photo_callback) # when pressed, trigger the photo_callback function

                gallerybox = StackLayout(padding=0,spacing=0)
                gallerybackbutton = Button(text="Back to Take Pictures", size_hint=(1, .2))
                gallerybackbutton.bind(on_press=gallery_back_callback)
                gallerybox.add_widget(gallerybackbutton)
                gallerybox.add_widget(carousel)
                galleryscreen.add_widget(gallerybox)

                # Add the UI elements to the layout
                photobox.add_widget(galleryButton)
                photobox.add_widget(photoButton)
                #photobox.add_widget(self.photo)
                photobox.add_widget(cam)
                

                photoscreen.add_widget(photobox)

                return sm
                
                
        # Callback for thumbnail refresh
        #def callback(self, instance):
        #        self.photo.reload()


if __name__ == '__main__':
        MyApp().run()