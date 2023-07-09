# from Colorizer import *
# import tkinter as tk

# root = tk.Tk()

# root.geometry("500x500")
# root.title("Colorization")


# root.mainloop()


# colorizer = Colorizer(use_cuda = False, width = 600, height = 600)

# '''for img in glob.glob("input/i2.jpg"):
#     colorizer.processImage(img)
# '''
# # colorizer.processVideo("input/v1.mp4")

import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from Colorizer import *
import os


class ColorizerUI:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Security - Colorization")
        self.colorizer = None

        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Create a header label
        self.title = tk.Label(self.root, text="Upload Media", font=("Arial", 20))
        self.title.pack(padx=10, pady=20)


        # Create a label for the input file selection
        self.input_file_label = tk.Label(self.root, text="Input file")
        self.input_file_label.pack(padx=5, pady=5)

        # Create a text box for the input file path
        self.input_file_textbox = tk.Entry(self.root, state='readonly')
        self.input_file_textbox.pack(padx=5, pady=0)


        self.button_frame = tk.Frame(self.root)

        # Create a button to select the input file
        self.input_file_button = tk.Button(self.button_frame, text="Browse", command=self.select_input_file)
        self.input_file_button.grid(row=0, column=0, padx=5, pady=5)

        # Create a button to start the colorization
        self.colorize_button = tk.Button(self.button_frame, text="Colorize", command=self.colorize)
        self.colorize_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_frame.pack(pady=15)

    def select_input_file(self):
        # Open a file selection dialog box and update the input file text box
        file_path = filedialog.askopenfilename()
        self.input_file_path = os.path.abspath(file_path)
        file_name = os.path.basename(file_path)
        self.input_file_textbox.config(state='normal')
        # self.input_file_textbox.delete(0, tk.END)
        self.input_file_textbox.insert(0, file_name)
        self.input_file_textbox.config(state='readonly')

    def colorize(self):

        # Check if a file has been selected
        if not hasattr(self, 'input_file_path') or not self.input_file_path:
            messagebox.showerror("Error", "Please select a file")
            return
        
        # Clear the input file textbox
        self.input_file_textbox.config(state='normal')
        self.input_file_textbox.delete(0, tk.END)
        self.input_file_textbox.config(state='readonly')

        # Get the input file path and run the colorization process
        input_file_name = self.input_file_path
        input_file_path = os.path.abspath(input_file_name)
        self.colorizer = Colorizer(use_cuda=False, width=600, height=600)

        _, ext = os.path.splitext(input_file_path)
        if ext in ['.jpg', '.jpeg', '.png']:
            # Run the colorization process on the image
            self.colorizer = Colorizer(use_cuda=False, width=600, height=600)
            self.colorizer.processImage(input_file_path)
        elif ext in ['.mp4', '.avi', '.mov']:
            # Run the colorization process on the video
            self.colorizer = Colorizer(use_cuda=False, width=600, height=600)
            self.colorizer.processVideo(input_file_path)
        else:
            # Display an error message if the selected file is not an image or video
            messagebox.showerror("Error", "Unsupported file format")
    
    # def run(self):
    #     self.root.state('zoomed') 
    #     self.root.mainloop()

if __name__ == "__main__":
    colorizer_ui = ColorizerUI()
    colorizer_ui.root.mainloop()
    colorizer_ui.run()