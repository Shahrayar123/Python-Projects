# QR Code Generator Python Program

## Description
This is a Python program that allows you to generate QR codes from text input. It uses the `PyQRCode` library to generate the QR code and the `Tkinter` library for creating the graphical user interface (GUI).

## Requirements
- Python 3.x
- PyQRCode library (`pip install pyqrcode`)
- Tkinter library (usually pre-installed with Python)

## Usage
1. Run the program (`python qr_code_generator.py`).
2. A new window will open with the title "QR Code Gen".
3. Enter the text or data you want to encode into the QR code in the input field.
4. Click the "Generate" button to generate the QR code image.
5. The generated QR code will be displayed in the main window.
6. To save the QR code as a PNG file, click the "Save" button.
   - The file will be saved in the same directory as the program, with the filename being the current timestamp (e.g., `1684150800.0.png`).

## Code Overview
The program consists of the following main components:

1. **Importing necessary modules**: The program imports the required modules, including `tkinter` for creating the GUI, `time` for generating timestamps, and `pyqrcode` for generating QR codes.

2. **Function definitions**:
   - `gen_qr()`: This function generates the QR code image based on the input text and displays it in the GUI window.
   - `save()`: This function calls the `gen_qr()` function and then saves the generated QR code as a PNG file with the current timestamp as the filename.

3. **Main program**:
   - The program creates a `Tkinter` window with the title "QR Code Gen" and sets its size and properties.
   - It defines a `StringVar` object called `con` to store the input text.
   - The GUI is divided into three frames: `f1` for the title, `f2` for the input field and buttons, and `f3` for displaying the generated QR code.
   - Widgets such as labels, entry fields, and buttons are added to the respective frames.
   - The `mainloop()` function is called to start the GUI event loop.