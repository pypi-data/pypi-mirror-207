from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import threading
import ctypes
import time

# Function to show the window
def show_window(icon, item):
    icon.stop()

# Function to quit the program
def quit_program(icon, item):
    icon.stop()
    
    # exit() only exits the current thread, so we have to kill all the other threads too.
    # exit()
    import psutil
    import os

    parent_pid = os.getpid()
    parent = psutil.Process(parent_pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    parent.kill()

# Function to set the volume of Discord
def set_program_volume(volume, process_name):
    global discord_volume
    
    # Set the global volume variable to the specified value
    discord_volume = volume
    
    # Get all audio sessions
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        # Check if this is the Discord session
        if session.Process and session.Process.name() == process_name:
            # Set the volume of Discord
            session.SimpleAudioVolume.SetMasterVolume(volume, None)

def system_tray_icon(tooltip, image_path):
    # Create an image for the system tray icon
    image = Image.open(image_path)
    # Create a system tray icon with the specified image and menu
    global tray_icon
    tray_icon = icon(tooltip, image, tooltip, menu=menu())

def create_function_in_thread(function):
    # Create a thread for the system tray icon
    global tray_thread
    tray_thread = threading.Thread(target=function)

def run_thread(thread):
    # Start the thread for the system tray icon
    thread.start()

def run_program_in_background():
    # Make it run in the background
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)