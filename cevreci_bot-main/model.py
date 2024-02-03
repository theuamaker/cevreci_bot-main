from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import time

def error(image_path):
    #print("Merhaba, lego parçalarını tanıyan yapay zeka projesine hoş geldiniz!")
    #time.sleep(1)
    #print("Legonun cinsi algılanıyor, lütfen bir yere ayrılmayın...")
    #time.sleep(2)
    #print("Pieces are detected")
    #time.sleep(2)
    # print("İşlem yapılıyor")
    # time.sleep(1.5)
    # print("...")
    # time.sleep(1)
    # print("...")

    # # Disable scientific notation for clarity
    # np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("cevreci_bot-main/keras_model.h5", compile=False)

    # Load the labels
    class_names = open("cevreci_bot-main/labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Predict the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index][2:]
    confidence_score = prediction[0][index]

    return class_name, confidence_score

# # Örnek kullanım
# image_path = "images/Ekran görüntüsü 2024-02-03 161040.png"
# class_name, confidence_score = error(image_path)

# # Print prediction and confidence score
# print("Class:", class_name)
# print("Confidence Score:", confidence_score)
# print(".")
# print(".")
# print("BİTTİ!")