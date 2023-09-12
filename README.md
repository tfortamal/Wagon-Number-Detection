# Train Wagon number Detection and Extraction System
## YOLO + EasyOCR
⚠️ This repository contains the code for the Train Wagon number Detection and Extraction System using EasyOCR and YOLOv8 algorithm by ultralytics for object classification on custom data. The project provides code for procedural-oriented programming implementations in Python.  

# Table of Contents
* [Wagon Numbering System of Indian Railways](https://github.com/tfortamal/Wagon-Number-Detection/tree/main#wagon-numbering-system-of-indian-railways)
* [Requirements]()
* [Workflow and Flowchart]()
* [Results]()

<p align="center">
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/d134a2349672e044cee910e3042fef34af6ea63e/img/WagonNumber.png" width=950>
</p>

# Wagon Numbering System of Indian Railways
According to the railway system, The 11-digit wagon number holds great importance in identifying the wagon individually.
The first of pair digits signify the type of wagon.
The second pair of digits represents the railway owning the wagon.
The third pair of digits represent the year of manufacture. e.g. if the third pair is 11 then it means it was manufactured in 2011
The next set of four digits represents individual wagon number
The last digit is a check digit to check and verify the other 10 digits just like a parity checking.

 
<p align="center">
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R2.png" width="600"/>
</p>
<p align="center">
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R3.png" width="600"/>
</p>
<p align="center">
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R4.png" width="600"/>
</p>
<p align="center">
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R5.png" width="600"/>
</p>

 

Requirements installation
```
pip install ultralytics
pip install easyocr
pip install opencv-python
pip install Pillow==9.5.0
```
Click here for [Quickstart](https://docs.ultralytics.com/quickstart/)

For more details check
* ultralytics YOLOv8 [Github repository](https://github.com/ultralytics/ultralytics) and the YOLOv8 python [documentation](https://docs.ultralytics.com/usage/python/#train)
* EasyOCR Github [repository](https://github.com/JaidedAI/EasyOCR)



## Results
<p float="center">
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R1.png" width="800" />
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R2.png" width="800"/>
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R3.png" width="800"/>
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R4.png" width="800"/>
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R5.png" width="800"/>
    <img src="https://github.com/tfortamal/Wagon-Number-Detection/blob/0bc24c6724de4cda3c068ad744604e5523a848c5/img/R6.png" width="800"/>
</p>



## Results from running the model video
Download and run the code for video inference
* Link to file: [wnd.py](src/wnd.py)
Code to Verify The Detected Wagon Number
* 


### Author: _**Tamal Das** August, 2023
