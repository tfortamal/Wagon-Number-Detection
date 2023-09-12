# Train Wagon number Detection and Extraction System
## YOLO + EasyOCR
⚠️ This repository contains the code for Train Wagon number Detection and Extraction System using EasyOCR and YOLOv8 algorithm by ultralytics for object classification on custom data. The project provides code for procedural-oriented programming implementations in Python.  

# Table of Contents
* [Wagon Numbering System of Indian Railways]()
* [Requirements]()
* [Work flow and Flowchart]()
* [Results]()

<p align="center">
    <img src="" width=800>
</p>

# Wagon Numbering System of Indian Railways
According to the railway system, The 11 digit wagon number holds great importance in intentifying the wagon individually.
The first of pair digits signifis the type of wagon.
The second pair of digits represent the railway owning the wagon.
The thirt pair of digits represrnt the year of manufacture. e.g. if the third pair is 11 then it means it was manufactured in 2011

  

Requirements installation
```
pip install ultralytics
pip install easyocr
pip install opencv-python
pip install Pillow==9.5.0
```
Click here for [Quickstart](https://docs.ultralytics.com/quickstart/)

For more details check
ultralytics YOLOv8 Github [repository](https://github.com/ultralytics/ultralytics) and the YOLOv8 python [documentation](https://docs.ultralytics.com/usage/python/#train)
EasyOCR Github [repository](https://github.com/JaidedAI/EasyOCR)


## Training Results
<p float="left">
    <img src="https://github.com/tfortamal/Conveyor-Belt-Material-Classification-YOLOv8/blob/9527fa3c3bf636cf3329134de2a50adeb5825505/train_results/val_batch0_pred.jpg" width="300" />
    <img src="https://github.com/tfortamal/Conveyor-Belt-Material-Classification-YOLOv8/blob/9527fa3c3bf636cf3329134de2a50adeb5825505/train_results/val_batch1_labels.jpg" width="300"/>
    <img src="https://github.com/tfortamal/Conveyor-Belt-Material-Classification-YOLOv8/blob/389f7c0845dcf3eed409c883edb88966300c280d/train_results/val_batch2_pred.jpg" width="300"/> 
</p>

<p align="center">
    <img src="https://github.com/tfortamal/Conveyor-Belt-Material-Classification-YOLOv8/blob/9527fa3c3bf636cf3329134de2a50adeb5825505/train_results/results.png" width=600>
</p>




## Results from running the model video
Link to file: [materialClassificarionj1c1.py](https://github.com/tfortamal/Conveyor-Belt-Material-Classification-YOLOv8/blob/0bc66e292c7381385366e3268649da987ed2690e/code/materialClassificarionj1c1.py)


### Author: _**Tamal Das** August, 2023
