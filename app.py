import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
import streamlit as st

from db_config import collection
from med_assistance import search_nearby_hospitals

model = tf.keras.models.load_model('tumor_classification_model.h5')

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

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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
                st.markdown("""

                **Brief Info:**  
                Glioma is a type of brain tumor that originates in the glial cells, which support nerve cells in the brain.

                **Symptoms:**  
                - Persistent headaches  
                - Seizures  
                - Nausea or vomiting  
                - Vision problems  
                - Memory or speech difficulties  

                **Treatment Recommendations:**  
                - Surgery to remove the tumor  
                - Radiation therapy  
                - Chemotherapy  
                - Targeted therapy (in some cases)

                ⚠️ This information is for educational/research purposes only. Please consult a qualified medical professional for diagnosis and treatment.""")

            elif predicted_label == "Meningioma":
                st.markdown("""

                **Brief Info:**  
                Meningioma is a tumor that forms in the meninges, the membranes that surround the brain and spinal cord.

                **Symptoms:**  
                - Headaches  
                - Vision changes  
                - Hearing loss  
                - Seizures  
                - Weakness in arms or legs  

                **Treatment Recommendations:**  
                - Monitoring (for slow-growing tumors)  
                - Surgical removal  
                - Radiation therapy  

                ⚠️ This information is for educational/research purposes only. Please consult a qualified medical professional for diagnosis and treatment.""")
                
            elif predicted_label == "Pituitary":
                st.markdown("""

                **Brief Info:**  
                Pituitary tumors develop in the pituitary gland, which controls hormone production in the body.

                **Symptoms:**  
                - Hormonal imbalances  
                - Vision problems  
                - Headaches  
                - Unexplained weight changes  
                - Fatigue  

                **Treatment Recommendations:**  
                - Medication to regulate hormones  
                - Surgery  
                - Radiation therapy  

                ⚠️ This information is for educational/research purposes only. Please consult a qualified medical professional for diagnosis and treatment.""")

            else:
                st.success("No tumor detected. You may continue a healthy lifestyle, but always monitor your health regularly.")

            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            document = {
                "image_name": uploaded_file.name,
                "image_path": file_path,
                "predicted_class": predicted_label,
                "upload_time": datetime.utcnow()
            }

            collection.insert_one(document)
            st.success("Prediction saved to database successfully!")

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