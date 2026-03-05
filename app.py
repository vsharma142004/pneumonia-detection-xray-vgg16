import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("chest_xray_vgg16_model.h5")
    return model

model = load_model()

IMG_SIZE = (96, 96)

st.title("Chest X-Ray Pneumonia Detection")
st.write("Upload a chest X-ray image to detect pneumonia.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])


def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    image = np.array(image)

    if image.shape[-1] == 4:
        image = image[:, :, :3]

    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    return image


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)[0][0]

    if prediction > 0.5:
        result = "PNEUMONIA DETECTED"
        confidence = prediction
    else:
        result = "NORMAL"
        confidence = 1 - prediction

    st.subheader("Prediction Result")
    st.write(result)
    st.write(f"Confidence: {confidence:.2f}")