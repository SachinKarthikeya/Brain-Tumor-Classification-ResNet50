import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import ollama
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from med_assistance import search_nearby_hospitals

model = tf.keras.models.load_model('/Users/sachinkarthikeya/Downloads/Projects/BTC-ResNet50/tumor_classification_model.h5')

class_labels = ['Glioma', 'Meningioma', 'Notumor', 'Pituitary']

def preprocess_image(image_path):
    img = load_img(image_path, target_size=(224, 224))

    plt.imshow(img)
    plt.axis('off')
    plt.show()

    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

def predict_tumor(image_path):
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)
    predicted_class_index = np.argmax(predictions[0])
    predicted_label = class_labels[predicted_class_index]
    return predicted_label

def autoresponder(prompt):
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]

st.title("Brain Tumor Classification with BrainyBot")
st.write("Upload an MRI image to classify the type of brain tumor.")

uploaded_file = st.file_uploader("Upload an MRI image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image.save("uploaded_image.jpg")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("Uploaded MRI Image")
        st.image(image, use_column_width=True)

    with col2:
        if st.button("Predict Tumor Type"):
            with st.spinner('Classifying...'):
                predicted_label = predict_tumor("uploaded_image.jpg")
                st.write(f"Predicted Tumor Type: **{predicted_label}**")

            if predicted_label == "Glioma":
                prompt = """
                You are an AI assistant in brain tumor information.
                User has uploaded an MRI image and the predicted class is Glioma.
                Please provide a brief information about its definition, symptoms and treatment recommendations.
                For reliability: This is for educational purposes only; consult a doctor for real advice or treatment options.
                """
                with st.spinner('Gathering Information...'):
                    response = autoresponder(prompt)
                    st.markdown(f"<h3>Tumor Info:</h3><p>{response}</p>", unsafe_allow_html=True)

            elif predicted_label == "Meningioma":
                prompt = """
                You are an AI assistant in brain tumor information.
                User has uploaded an MRI image and the predicted class is Meningioma.
                Please provide a brief information about its definition, symptoms and treatment recommendations.
                For reliability: This is for educational purposes only; consult a doctor for real advice or treatment options.
                """
                with st.spinner('Gathering Information...'):
                    response = autoresponder(prompt)
                    st.markdown(f"<h3>Tumor Info:</h3><p>{response}</p>", unsafe_allow_html=True)

            elif predicted_label == "Pituitary":
                prompt = """
                You are an AI assistant in brain tumor information.
                User has uploaded an MRI image and the predicted class is Pituitary.
                Please provide a brief information about its definition, symptoms and treatment recommendations.
                For reliability: This is for educational purposes only; consult a doctor for real advice or treatment options.
                """
                with st.spinner('Gathering Information...'):
                    response = autoresponder(prompt)
                    st.markdown(f"<h3>Tumor Info:</h3><p>{response}</p>", unsafe_allow_html=True)

            else:
                st.success("No tumor detected. You may continue a healthy lifestyle, but always monitor your health regularly.")

else:
    st.info("Please upload an MRI image to get started.")    

st.divider()
st.header("Find Hospitals Near You")
location = st.text_input("Enter your location (city or locality address):")

if location:
    with st.spinner('Searching for nearby hospitals...'):
        hospital_list = search_nearby_hospitals(location)
        for hospital in hospital_list:
            st.markdown("---")
            st.markdown(f"<h3>{hospital}</h3>", unsafe_allow_html=True)
    if not hospital_list:
        st.write("No hospitals found in your area.")