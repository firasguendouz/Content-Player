'''
Handles file selection and loading functionalities.
'''
import os
from PIL import Image
from moviepy.editor import VideoFileClip
from tkinter import filedialog
class FileManager:
    SUPPORTED_IMAGE_FORMATS = [".jpeg", ".jpg", ".png"]
    SUPPORTED_VIDEO_FORMATS = [".mp4", ".avi"]
    @staticmethod
    def browse_files():
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpeg;*.jpg;*.png"), ("Video Files", "*.mp4;*.avi")])
        return list(file_paths)
    @staticmethod
    def validate_file(file_path):
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() in FileManager.SUPPORTED_IMAGE_FORMATS + FileManager.SUPPORTED_VIDEO_FORMATS:
            return True
        return False
    @staticmethod
    def load_file(file_path):
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() in FileManager.SUPPORTED_IMAGE_FORMATS:
            return FileManager.load_image(file_path)
        elif file_extension.lower() in FileManager.SUPPORTED_VIDEO_FORMATS:
            return FileManager.load_video(file_path)
        else:
            raise ValueError("Invalid file format")
    @staticmethod
    def load_image(file_path):
        try:
            image = Image.open(file_path)
            return image
        except IOError:
            raise IOError("Failed to load image")
    @staticmethod
    def load_video(file_path):
        try:
            video = VideoFileClip(file_path)
            return video
        except IOError:
            raise IOError("Failed to load video")