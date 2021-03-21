# initial face detection 
from PIL import Image
import face_recognition

# loading image file
image = face_recognition.load_image_file("")

face_locations = face_recognition.face_locations(image)

print(" {} faces have been discovered within the selected image").format(lens(face_locations))


# face_location is renamed location
for location in face_locations:
    # prints face location for faces found in image
    top, right, bottom, left = location
    print("A face has been found in the stated pixel locations: Top: {}, Right: {}, Bottom {}, Left {}".format(top,right,bottom,left))



