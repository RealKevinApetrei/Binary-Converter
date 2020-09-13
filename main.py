import tkinter as tk
from tkinter import font
import re

import config


class Application(tk.Tk): # Application Class Object
    def __init__(self):
        super().__init__() # Superclass (tk.Tk)
        
        self.title(f"{config.PROGRAM_NAME} | {config.BUILD_VERSION} | By {config.AUTHOR}") # Window Title
        self.geometry("500x250") # Window Size (Template)
        self.resizable(0, 0) # not Resizable

        self.space_pattern = re.compile(r"00100000") # SPACE PATTERN
        self.new_line_pattern = re.compile(r"00001010") # NEW LINE PATTERN
        
        # Fonts
        self.hel15b = font.Font(family="Helvetica", size=15, weight="bold") # Font (Helvetica, 15, Bold)
        self.sys20bu = font.Font(family="system", size=20, weight="bold", underline=1) # Font (system, 20, Bold, Underline)

        # Other
        self.back_image = tk.PhotoImage(file="./Other/back.png") # back.png for Back Icon

    def __repr__(self):
        __name = self.__class__
        __type = type(self)
        __module = type.__module__
        __qualname = type.__qualname__

        return f"""\
        Class Name: {__name}
        Class Details: {config.PROGRAM_NAME}

        Build Version: {config.BUILD_VERSION}
        Author: {config.AUTHOR}
        
        Class Type: {__type}
        Class Module: {__module}
        Class Qualname: {__qualname}
        """

    def back(self):
        self.destroy() # Destroy Window
        
        setup() # Run Main Menu Setup


class BinaryToText(Application): # Binary To Text Window
    def __init__(self):
        super().__init__() # Superclass (Application)

        self.geometry("500x500") # Window Size (AMENDED)

        # Window Contents
        tk.Label(self, text="Binary", font=self.sys20bu).place(x=250, y=50, anchor="center") # Binary Text Box (Title)
        self.binary_box = tk.Text(self, height=5, width=50)
        self.binary_box.place(x=250, y=150, anchor="center") # Binary Text Box

        tk.Label(self, text="ASCII Text", font=self.sys20bu).place(x=250, y=250, anchor="center") # Text Result Box (Title)
        self.text_box_result = tk.Text(self, height=5, width=50, state="disabled")
        self.text_box_result.place(x=250, y=350, anchor="center") # Text Result Box

        tk.Button(self, text="Convert", command=self.convert, font=self.hel15b).place(x=250, y=450, anchor="center") # Conversion Button (BtoT)
        
        tk.Button(self, command=self.back, image=self.back_image).place(x=450, y=450, anchor="e") # Back Button using back_image

    def convert(self):
        binary_text = self.binary_box.get("1.0", "end") # Get Binary Input
        binary_values = binary_text.split() # Get Individual Binary Values

        ascii_string = "" # Initialise ASCII Text String (for Output)
        
        try:
            for value in binary_values:
                ascii_string += chr(int(value, 2)) # Find the Chr for the Binary Value and Add to String
        except Exception as e:
            ascii_string = f"ERROR ({e})"
        finally:
            self.text_box_result.configure(state="normal") # Enable Text Box
            self.text_box_result.delete("1.0", "end") # Reset Text Box
            self.text_box_result.insert("1.0", ascii_string) # Insert Text Value
            self.text_box_result.configure(state="disabled") # Disable Text Box


class TextToBinary(Application): # Text to Binary Window
    def __init__(self):
        super().__init__() # Superclass (Application)

        self.geometry("500x500") # Window Size (AMENDED)

        # Variables
        self.remove_spaces = tk.IntVar() # Remove Spaces (1/0)
        self.remove_new_lines = tk.IntVar() # Remove New Lines (1/0)

        # Window Contents
        self.remove_spaces_check = tk.Checkbutton(self, text="Remove Spaces", variable=self.remove_spaces, onvalue=1, offvalue=0)
        self.remove_spaces_check.place(x=25, y=25, anchor="nw") # Check Box Remove Spaces

        self.remove_new_lines_check = tk.Checkbutton(self, text="Remove New Lines", variable=self.remove_new_lines, onvalue=1, offvalue=0)
        self.remove_new_lines_check.place(x=25, y=50, anchor="nw") # Check Box Remove New Lines

        tk.Label(self, text="ASCII Text", font=self.sys20bu).place(x=300, y=50, anchor="center") # Text Text Box (Title)
        self.text_box = tk.Text(self, height=5, width=50)
        self.text_box.place(x=250, y=150, anchor="center") # Text Text Box

        tk.Label(self, text="Binary", font=self.sys20bu).place(x=300, y=250, anchor="center") # Binary Result Box (Title)
        self.binary_result_box = tk.Text(self, height=5, width=50, state="disabled")
        self.binary_result_box.place(x=250, y=350, anchor="center") # Binary Result Box

        tk.Button(self, text="Convert", command=self.convert, font=self.hel15b).place(x=250, y=450, anchor="center") # Conversion Button (TtoB)
        
        tk.Button(self, command=self.back, image=self.back_image).place(x=450, y=450, anchor="e") # Back Button using back_image

    def convert(self):
        text_input = self.text_box.get("1.0", "end") # Get Text Input

        try:
            binary_list = [f"{ord(i):08b}" for i in text_input] # Binary List (for Output)
            
            if self.remove_spaces.get() == 1:
                binary_list = [i for i in binary_list if not self.space_pattern.match(i)] # Removed Spaces
            if self.remove_new_lines.get() == 1:
                binary_list = [i for i in binary_list if not self.new_line_pattern.match(i)] # Removed New Lines
        except Exception as e:
            binary_list = [f"ERROR ({e})"]
        finally:
            self.binary_result_box.configure(state="normal") # Enable Text Box
            self.binary_result_box.delete("1.0", "end") # Reset Text Box
            self.binary_result_box.insert("1.0", " ".join(binary_list)) # Insert Binary Values (joined)
            self.binary_result_box.configure(state="disabled") # Disable Text Box


class MainMenu(Application): # Main Menu
    def __init__(self):
        super().__init__() # Superclass (Application)

        # Window Contents
        tk.Button(self, text="Binary to Text", command=self.BinaryToTextAction, bg="gray50", width=25, font=self.hel15b).place(x=250, y=50, anchor="center") # Binary To Text (Button)
        tk.Button(self, text="Text to Binary", command=self.TextToBinaryAction, bg="gray50", width=25, font=self.hel15b).place(x=250, y=100, anchor="center") # Text to Binary (Button)

    def BinaryToTextAction(self): # Binary to Text Window Setup
        self.destroy() # Destroy Main Menu

        window = BinaryToText() # Binary to Text Window (init)
        window.mainloop() # Window Loop
        
    def TextToBinaryAction(self): # Text to Binary Window Setup
        self.destroy() # Destroy Main Menu

        window = TextToBinary() # Text to Binary Window (init)
        window.mainloop() # Window Loop

            
def setup(): # Main Menu Setup
    main = MainMenu() # Main Menu Window (init)
    main.mainloop() # Window Loop


if __name__ == "__main__": # If Program is run directly...
    setup() # App Setup