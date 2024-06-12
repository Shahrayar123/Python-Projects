import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        
        self.video_source = ""
        self.vid = None
        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()
        
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(anchor=tk.CENTER, expand=True)
        
        self.btn_open = tk.Button(self.control_frame, text="Load Video from path", width=20, command=self.open_video)
        self.btn_open.pack(side=tk.LEFT)
        
        self.btn_play = tk.Button(self.control_frame, text="Play", width=10, command=self.play_video)
        self.btn_play.pack(side=tk.LEFT)
        
        self.btn_stop = tk.Button(self.control_frame, text="Pause", width=10, command=self.stop_video)
        self.btn_stop.pack(side=tk.LEFT)
        
        self.delay = 15
        self.stop = False

    def open_video(self):
        self.video_source = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
        if not self.video_source:
            return
        
        self.vid = cv2.VideoCapture(self.video_source)
        if not self.vid.isOpened():
            messagebox.showerror("Error", "Unable to open the video file.")
        else:
            self.stop = False

    def play_video(self):
        if not self.vid or not self.vid.isOpened():
            messagebox.showwarning("Warning", "No video has been opened.")
            return
        
        self.stop = False
        self.update_frame()

    def stop_video(self):
        self.stop = True

    def update_frame(self):
        if self.vid and not self.stop:
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
                image_tk = ImageTk.PhotoImage(image=image)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
                self.canvas.image_tk = image_tk
                self.root.after(self.delay, self.update_frame)
            else:
                self.vid.release()
                self.canvas.image_tk = None

    def __del__(self):
        if self.vid and self.vid.isOpened():
            self.vid.release()

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
