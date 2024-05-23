import cv2
import numpy as np

# Load the trained model for disease detection
model = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# Define the list of classes
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Define the function for disease detection
def detect_disease(image):
    # Create a blob from the input image
    blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416), (0, 0, 0), True, crop=False)

    # Set the input for the model
    model.setInput(blob)

    # Get the output from the model
    outs = model.forward(model.getUnconnectedOutLayersNames())

    # Initialize the list for detected diseases
    diseases = []

    # Loop through the output layers
    for out in outs:
        # Loop through the detections in the output layer
        for detection in out:
            # Get the class ID and confidence score
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Filter out weak detections
            if confidence > 0.5:
                # Get the name of the disease
                disease_name = classes[class_id]

                # Get the bounding box coordinates
                center_x = int(detection[0] * image.shape[1])
                center_y = int(detection[1] * image.shape[0])
                w = int(detection[2] * image.shape[1])
                h = int(detection[3] * image.shape[0])

                # Calculate the top-left corner coordinates
                x = int(center_x - w/2)
                y = int(center_y - h/2)

                # Add the disease to the list
                diseases.append((disease_name, confidence, x, y, w, h))

    # Filter out overlapping detections
    diseases = [disease for disease in diseases if not any(np.array(disease[3:5]) < np.array([max(other[5], other[7]), max(other[6], other[8])]) or np.array(disease[3:5]) > np.array([min(other[5], other[7]), min(other[6], other[8])]) for other in diseases)]

    # Return the list of detected diseases
    return diseases

# Load the input image
image = cv2.imread('crop_image.jpg')

# Detect the disease in the image
diseases = detect_disease(image)

# Print the detected diseases
for disease in diseases:
    print(f'Disease: {disease[0]}, Confidence: {disease[1]:.2f}')

# Provide remedy based on the detected disease
if 'Bacterial Blight' in [disease[0] for disease in diseases]:
    print('Remedy: Apply copper-based bactericides to control the disease.')
elif 'Leaf Miner' in [disease[0] for disease in diseases]:
    print('Remedy: Remove and destroy affected leaves to prevent further spread.')
elif 'Spider Mite' in [disease[0] for disease in diseases]:
    print('Remedy: Apply acaricides to control the pest.')
else:
    print('No disease or pest detected.')