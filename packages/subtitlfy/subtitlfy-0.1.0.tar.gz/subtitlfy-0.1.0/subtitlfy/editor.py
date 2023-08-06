import os
import subprocess

import cv2
import numpy as np


class SubtitlesEditor:
    def __init__(self, video_path):
        # Load the video file
        self.video_path = video_path
        self.cap = cv2.VideoCapture(self.video_path)

        # Get the video properties
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        # Create the video writer
        self.output_path = f'{os.getcwd()}/temporary_video.mp4'
        self.out = cv2.VideoWriter(self.output_path, self.fourcc, self.fps, (self.frame_width, self.frame_height))

        # Define the font and its properties
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 1
        self.font_thickness = 1
        self.text_color = (255, 255, 255)  # white color

    def add_text(self, text_dict):
        # "text_dict" should resembling of [(0, 1, "Hello world")]
        # 0 - Start Time; 1 - Eng Time; (in sec)

        # Loop through each frame of the video
        for frame_num in range(self.total_frames):
            # Read the next frame
            ret, frame = self.cap.read()
            
            if ret:
                # Check if the current frame time is in the text_dict and get the corresponding text
                current_time = frame_num / self.fps
                text = None
                for start_time, end_time, t in text_dict:
                    if current_time >= start_time and current_time < end_time:
                        text = t
                        break
                
                # If no text is found, continue to the next frame
                if text is None:
                    self.out.write(frame)
                    continue
                    
                # Define the position of the text at the bottom of the frame
                text_position = (50, self.frame_height - 50)

                # Define the size of the background rectangle based on the text size
                (text_width, text_height), _ = cv2.getTextSize(text, self.font, self.font_scale, self.font_thickness)
                background_size = (text_width + 20, text_height + 20)

                # Check if the text fits within the frame, otherwise decrease the font size
                while background_size[0] > self.frame_width or background_size[1] > self.frame_height:
                    self.font_scale -= 0.1
                    (text_width, text_height), _ = cv2.getTextSize(text, self.font, self.font_scale, self.font_thickness)
                    background_size = (text_width + 20, text_height + 20)

                # Define the position of the background rectangle based on the text position
                background_position = (text_position[0] - 10, text_position[1] - text_height - 10)

                # Make sure the background rectangle fits within the frame
                if background_position[0] + background_size[0] > self.frame_width:
                    background_position = (self.frame_width - background_size[0] - 10, background_position[1])
                if background_position[1] < 0:
                    background_position = (background_position[0], 10)

                # Add the background rectangle to the frame
                background = np.zeros((background_size[1], background_size[0], 3), dtype=np.uint8)
                background.fill(0)
                cv2.rectangle(background, (0, 0), (background_size[0], background_size[1]), (0, 0, 0), -1)
                
                # Add the text to the background rectangle
                cv2.putText(background, text, (10, text_height + 10), self.font, self.font_scale, self.text_color, self.font_thickness, cv2.LINE_AA)
                
                # Add the background rectangle to the frame
                background_height, background_width, _ = background.shape
                frame[background_position[1]:background_position[1]+background_height, 
                    background_position[0]:background_position[0]+background_width] = background
                
                # Write the frame to the output video file
                self.out.write(frame)
            else:
                break

    def release(self, substitute=True):
        # Release the resources
        self.cap.release()
        self.out.release()

        # Combine audio and video
        self.__extract_audio()
        self.__combine_with_audio(substitute)

    def get_duration(self):
        return self.total_frames / self.fps

    def __extract_audio(self):
        # Extract the audio from the original video
        self.audio_path = f'{os.getcwd()}/temporary_audio.mov'
        subprocess.call(['ffmpeg', '-i', self.video_path, '-vn', '-acodec', 'copy', self.audio_path])

    def __combine_with_audio(self, substitute):
        # Combine the audio and video into a single file
        self.final_path = f'{os.getcwd()}/output_video.mp4' if not substitute else self.video_path
        subprocess.call(['ffmpeg', '-i', self.output_path, '-i', self.audio_path, '-c', 'copy', '-map', '0:v:0', '-map', '1:a:0', self.final_path])
    
    def __del__(self):
        os.remove(self.output_path)
        os.remove(self.audio_path)
