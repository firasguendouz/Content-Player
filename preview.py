'''
Handles real-time preview of the compiled content loop.
'''
import tkinter as tk
from PIL import ImageTk, Image
from moviepy.editor import concatenate_videoclips
class Preview:
    def __init__(self, playlist):
        self.playlist = playlist
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()
        self.current_index = 0
    def play(self):
        item, duration = self.playlist.get_items()[self.current_index]
        if isinstance(item, Image.Image):
            self.show_image(item)
        elif isinstance(item, concatenate_videoclips):
            self.show_video(item)
        self.window.after(duration * 1000, self.show_next_item)
        self.window.mainloop()
    def show_next_item(self):
        self.current_index = (self.current_index + 1) % len(self.playlist.get_items())
        self.canvas.delete("all")
        item, duration = self.playlist.get_items()[self.current_index]
        if isinstance(item, Image.Image):
            self.show_image(item)
        elif isinstance(item, concatenate_videoclips):
            self.show_video(item)
        self.window.after(duration * 1000, self.show_next_item)
    def show_image(self, image):
        image = image.resize((800, 600))
        image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image)
        self.canvas.image = image
    def show_video(self, video):
        video.preview()
    def apply_filters(self):
        item, _ = self.playlist.get_items()[self.current_index]
        if isinstance(item, Image.Image):
            # Implement image filters
            pass
        elif isinstance(item, concatenate_videoclips):
            # Implement video filters
            pass