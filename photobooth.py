import sys,time
from PIL import Image
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.carousel import Carousel
from kivy.clock import Clock
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.label import Label,CoreLabel
import glob


############################################
### GLOBALS ######
############################################
photoPath = "/Users/tgrecojr/Downloads/photos/"
cam = Camera()        #Get the camera
cam=Camera(resolution=(3280,2464),size_hint=(1, .8))
sm = ScreenManager(transition=SlideTransition(),duration=10)
carousel = Carousel(direction='right',loop='true',size_hint=(1, .8))
countdownMessage = Label(size_hint=(1, 1))

#############################################
def goto_take_photo_button_press(obj):
        photoName = time.strftime("%Y%m%d%H%M%S") + "_photobooth.jpg"
        #Message countdown here.... (or figure some way to do an onload event)
        #cam.texture.save(photoPath + "IMG_" + photoName, flipped=False)
        sm.current = 'MessageScreen'
        Clock.schedule_once(change_screen, 10)

def do_nothing(obj):
    print "doing nothing"

def change_screen(obj):
    sm.current = 'PhotoScreen'

def countdown_pressed(instance, value):
    print('User clicked on', value)

def goto_gallery_button_press(obj):
    cam.play=False
    pathname = photoPath + '*.jpg'
    for name in glob.glob(pathname):
        theimage = Image(source=name)
        carousel.add_widget(theimage)
    sm.current = 'GalleryScreen'

def gallery_back_callback(obj):
    cam.play=True
    sm.current = 'PhotoScreen'

class MyApp(App):

        cam.play = True  # Start the camera
        def build(self):

                # build the screens
                photoscreen = Screen(name='PhotoScreen')
                messagescreen = Screen(name='MessageScreen')
                galleryscreen = Screen(name='GalleryScreen')

                #Build the layout for the preview screen
                previewscreenlayout = StackLayout(padding=0,spacing=0)
                gotoGalleryButton = Button(text="Photo Gallery", size_hint=(.5, .2))
                gotoGalleryButton.bind(on_press=goto_gallery_button_press)
                gotoTakePhotoButton = Button(text="Take Photos", size_hint=(.5, .2))
                gotoTakePhotoButton.bind(on_press=goto_take_photo_button_press)
                previewscreenlayout.add_widget(gotoGalleryButton)
                previewscreenlayout.add_widget(gotoTakePhotoButton)
                previewscreenlayout.add_widget(cam)

                # build the layout for the gallery screen
                galleryscreenlayout = StackLayout(padding=0, spacing=0)
                gallerybackbutton = Button(text="Back to Take Pictures", size_hint=(1, .2))
                gallerybackbutton.bind(on_press=gallery_back_callback)
                galleryscreenlayout.add_widget(gallerybackbutton)
                galleryscreenlayout.add_widget(carousel)

                # build the layout for the message screen
                #messagescreenlayout = StackLayout(padding=0, spacing=0)
                messagescreenlayout = FloatLayout(padding=0, spacing=0);
                countdownMessage.bind(on_ref_press=countdown_pressed)
                countdownMessage.text = 'The PhotoBooth will take 4 photos, with a 3 second delay in between.  Get ready.......'
                countdownMessage.text_size =  500,500
                countdownMessage.font_size= 40
                countdownMessage.valign = 'middle'
                countdownMessage.halign = 'center'
                messagescreenlayout.add_widget(countdownMessage)


                # ADD layouts TO Screens
                photoscreen.add_widget(previewscreenlayout)
                galleryscreen.add_widget(galleryscreenlayout)
                messagescreen.add_widget(messagescreenlayout)

                # Add screens to screen manager
                sm.add_widget(photoscreen)
                sm.add_widget(messagescreen)
                sm.add_widget(galleryscreen)

                return sm



if __name__ == '__main__':
        MyApp().run()