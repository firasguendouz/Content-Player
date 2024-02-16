'''
Handles extraction and display of metadata for videos.
'''
from moviepy.editor import VideoFileClip
class Metadata:
    def __init__(self, video):
        self.video = video
    def get_title(self):
        return self.video.reader.infos['title']
    def get_artist(self):
        return self.video.reader.infos['artist']
    def get_album(self):
        return self.video.reader.infos['album']
    def get_duration(self):
        return self.video.reader.duration