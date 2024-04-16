import cv2
from wnd import WagonNumberDetection

videoPath = "vids/3.MP4"

vid = cv2.VideoCapture(videoPath)
previousWagonNumber = ""
currentWagonNumber = ""
while True:
    ret, frame = vid.read()

    if not ret:
        print("no frame")
        break
    
    wagonNumber, outputFrame = WagonNumberDetection.DetectWagonNumber(frame)

    currentWagonNumber = wagonNumber
    if currentWagonNumber == "" or previousWagonNumber == currentWagonNumber:
        print("no wagon number")
    else:
        cv2.putText(frame, wagonNumber, (230, 380), cv2.FONT_HERSHEY_DUPLEX, 1.8, (255,255,255) , 1, cv2.LINE_AA)
        
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
