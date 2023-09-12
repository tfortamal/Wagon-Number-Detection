from ultralytics import YOLO
import cv2
import easyocr


def detectionVerification(s):
      if s.isdigit():
        if len(s) == 11:
            print("11-digit Wagon number found")
            return True
        if len(s) == 6 or len(s) == 5:
            print("Multi-line Wagon number found")
            return True
      else:
        print("Non-Numerical Character found")
        return False
      

# load the models
# import trained model to see if there is a train or not
classificatonModel = YOLO("/Users/tamaldas/Desktop/DSS/OCR/WND/models/wagonClassificationV1.pt")
# load the next model to detect the wagon number in the train body
wadonNumberDetectionModel = YOLO("/Users/tamaldas/Desktop/DSS/OCR/WND/models/wagonNumberDetectionV2.pt")
# initilize the reader
reader = easyocr.Reader(['en'], gpu=False)


# load the video
cap = cv2.VideoCapture("/Users/tamaldas/Desktop/DSS/OCR/vidData/phoneDataVids/compressedVids/4.MP4")

wagonNo = "-"
confidence = 0

# list of ground truth of wagon number
gtList = ["21141123717", "21120942179", "21141128088", "21110867659", "21131124519", "21131123499"]

fcount = 1
while True:
    # read each frame from video
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Failed to capture frame")
        break

    # Resize the image
    new_height = 480
    new_width = int(frame.shape[1] * (new_height / frame.shape[0]))
    resized_frame = cv2.resize(frame, (new_width, new_height))
    
    # classify if there is wagon on the frame or not
    classificationResults = classificatonModel.predict(source=resized_frame, show=False, save=False, save_txt=False)

    # get classification results
    # print(classificationResults)
    id = classificationResults[0].probs.top1
    clsName = classificationResults[0].names[id]

    # Format wagonNoDetectionResults on the image
    string = "[ "+ clsName +" ]"
    font = cv2.FONT_HERSHEY_DUPLEX

    # if there is a wagon on the frame
    if clsName == "wagon":
        # perform wagon no detection on the frame
        wagonNoDetectionResults = wadonNumberDetectionModel.predict(source=resized_frame, show=True, save=False, save_txt=False)
        # print(wagonNoDetectionResults)
        color = (0, 255, 0) # green
        # Draw the filled (solid) rectangle on the image
        start_point = (50, 50)
        end_point = (250, 120)
        cv2.rectangle(resized_frame, start_point, end_point, color, -1)
        # put result text on image
        cv2.putText(resized_frame, string, (65, 95), font, 1, (0, 0, 0) , 2, cv2.LINE_AA)
        ocrStatus = "OCR Status: Detecting Wagon Number"
        cv2.putText(resized_frame, ocrStatus, (50, 170), font, .8, (0, 255, 0) , 1, cv2.LINE_AA)
        detectedText = "Wagon Number: "+wagonNo
        # Draw the filled (solid) rectangle on the image
        start_point = (50, 180)
        end_point = (470, 220)
        cv2.rectangle(resized_frame, start_point, end_point, color, -1)
        cv2.putText(resized_frame, detectedText, (65, 208), font, .8 ,(0,0,0), 1, cv2.LINE_AA)
        # segemnt or crop the frame
        for result in wagonNoDetectionResults:
            bboxes = []
            bboxes = result.boxes.xyxy
            for bbox in bboxes:
                  print("Bounding box of detection: ", bbox)
                  x1 = int(bbox[0])
                  y1 = int(bbox[1])
                  x2 = int(bbox[2])
                  y2 = int(bbox[3])
            
                  point1 = (x1, y1)
                  point2 = (x2, y2)

                  # crop and display the frame
                  croppedFrame = resized_frame[point1[1]:point2[1],point1[0]:point2[0]]
                  
                  # perform OCR on the frame
                  
                  ocrResults = reader.readtext(croppedFrame)

                  img = frame
                  for result in ocrResults:
                        # render results on image
                        text = result[1]
                        if detectionVerification(text):
                              wagonNo = text
                              print("Result", result)
                              confidence = result[2]
                              print("\nWagon Number: ", wagonNo)
                              top_left = tuple(int(val) for val in result[0][0])
                              bottom_right = tuple(int(val) for val in result[0][2])

                            #   cv2.imshow('Cropped Image', croppedFrame)
                            #   if cv2.waitKey(1) & 0xFF == ord('q'):
                            #         break
                              
                              font = cv2.FONT_HERSHEY_SIMPLEX
                              # cv2.rectangle(frame,point1,bottom_right,(0,255,0),2)
                              # cv2.putText(resized_frame,wagonNo,(50, 200), font, 1,(0,0,255),3,cv2.LINE_AA)

    else:
        color = (0, 0, 255) # red
        # Draw the filled (solid) rectangle on the image
        start_point = (50, 50)
        end_point = (290, 120)
        cv2.rectangle(resized_frame, start_point, end_point, color, -1)
        # put result text on image
        cv2.putText(resized_frame, string, (65, 95), font, 1, (255, 255, 255) , 2, cv2.LINE_AA)
        ocrStatus = "OCR Status: Not Detecting Wagon Number"
        cv2.putText(resized_frame, ocrStatus, (50, 170), font, .8, (0, 0, 255) , 1, cv2.LINE_AA)
        
        

# Display the captured frame
    cv2.imshow('frame', resized_frame)
    print(f"Frame count {fcount}")
    fcount=fcount+1
    # Check for the 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
