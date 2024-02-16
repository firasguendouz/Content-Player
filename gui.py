'''
Handles the graphical user interface using tkinter.
'''
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from moviepy.editor import concatenate_videoclips
from playlist import Playlist
from file_manager import FileManager
from preview import Preview
from metadata import Metadata
class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.playlist = Playlist()
        self.file_manager = FileManager()
        self.preview = Preview(self.playlist)
        self.metadata = None
        self.file_paths = []
        self.current_index = 0
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()
        self.add_button = tk.Button(self.window, text="Add", command=self.add_item_to_playlist)
        self.add_button.pack(side=tk.LEFT)
        self.remove_button = tk.Button(self.window, text="Remove", command=self.remove_item_from_playlist)
        self.remove_button.pack(side=tk.LEFT)
        self.rearrange_button = tk.Button(self.window, text="Rearrange", command=self.rearrange_items_in_playlist)
        self.rearrange_button.pack(side=tk.LEFT)
        self.save_button = tk.Button(self.window, text="Save Playlist", command=self.save_playlist)
        self.save_button.pack(side=tk.LEFT)
        self.load_button = tk.Button(self.window, text="Load Playlist", command=self.load_playlist)
        self.load_button.pack(side=tk.LEFT)
        self.play_button = tk.Button(self.window, text="Play", command=self.play_preview)
        self.play_button.pack(side=tk.LEFT)
        self.apply_filters_button = tk.Button(self.window, text="Apply Filters", command=self.apply_filters_to_preview)
        self.apply_filters_button.pack(side=tk.LEFT)
        self.customize_text_button = tk.Button(self.window, text="Customize Text", command=self.customize_text_overlay)
        self.customize_text_button.pack(side=tk.LEFT)
        self.load_files()
    def run(self):
        self.window.mainloop()
    def load_files(self):
        file_paths = self.file_manager.browse_files()
        self.file_paths = list(file_paths)
        for file_path in self.file_paths:
            if self.file_manager.validate_file(file_path):
                item = self.file_manager.load_file(file_path)
                duration = self.get_duration_from_user()
                self.playlist.add_item(item, duration)
        self.show_current_item()
    def show_current_item(self):
        self.canvas.delete("all")
        item, duration = self.playlist.get_items()[self.current_index]
        if isinstance(item, Image.Image):
            self.show_image(item)
        elif isinstance(item, concatenate_videoclips):
            self.show_video(item)
            self.metadata = Metadata(item)
            print("Title:", self.metadata.get_title())
            print("Artist:", self.metadata.get_artist())
            print("Album:", self.metadata.get_album())
            print("Duration:", self.metadata.get_duration())
        self.window.after(duration * 1000, self.show_next_item)
    def show_next_item(self):
        self.current_index = (self.current_index + 1) % len(self.playlist.get_items())
        self.show_current_item()
    def show_image(self, image):
        image = image.resize((800, 600))
        image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image)
        self.canvas.image = image
    def show_video(self, video):
        video.preview()
    def add_item_to_playlist(self):
        file_paths = self.file_manager.browse_files()
        file_paths = list(file_paths)
        for file_path in file_paths:
            if self.file_manager.validate_file(file_path):
                item = self.file_manager.load_file(file_path)
                duration = self.get_duration_from_user()
                self.playlist.add_item(item, duration)
        self.show_current_item()
    def remove_item_from_playlist(self):
        if len(self.playlist.get_items()) > 0:
            self.playlist.remove_item(self.current_index)
            self.current_index = min(self.current_index, len(self.playlist.get_items()) - 1)
            self.show_current_item()
    def rearrange_items_in_playlist(self):
        old_index = int(input("Enter the index of the item you want to rearrange: "))
        new_index = int(input("Enter the new index for the item: "))
        self.playlist.rearrange_items(old_index, new_index)
        self.current_index = new_index
        self.show_current_item()
    def save_playlist(self):
        # Implement saving the playlist functionality
        pass
    def load_playlist(self):
        # Implement loading the playlist functionality
        pass
    def play_preview(self):
        self.preview.play()
    def apply_filters_to_preview(self):
        self.preview.apply_filters()
    def customize_text_overlay(self):
        # Implement customizing text overlay functionality
        pass
    def get_duration_from_user(self):
        duration = input("Enter the duration (in seconds) for the item: ")
        return int(duration)