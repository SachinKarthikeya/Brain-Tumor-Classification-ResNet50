# 🧠 Brain Tumor Classification with BrainyBot

A deep learning-powered web application that performs **brain tumor classification from MRI images** using **ResNet50**, and provides **personalized medical assistance** via **SerpAPI chatbot**. The app is built with **Tensorflow** for the model, **Streamlit** for the frontend, and integrates **MongoDB** to store prediction records.

## 🚀 Features

- **Brain Tumor Classification** (Glioma, Meningioma, Pituitary, No Tumor) using ResNet50.
- **Emergency Assessment** with detailed explanations and recommended actions.
- **Nearby Hospital Finder** based on user’s city or area using SerpAPI.
- **MongoDB** database integration to store predictions for future use.
- **Interactive Interface** with real-time image upload and classification via Streamlit.

## 📄 Workflow

- User uploads an MRI image via the Streamlit interface.
- The image is preprocessed and passed through the trained ResNet50 model.
- The model predicts the tumor type and gives a brief information about symptoms and treatment options.
- Automatically stores the images along with predictions in the database.
- An AI chatbot answers user queries and helps find nearby hospitals.

## 📁 Versions
For this project, there are two versions which work separately:

**Version 1**:
- No MongoDB database integrated
- Containerized the project using Docker

**Version 2**:
- MongoDB database integrated
- Docker containerization not performed.

## 🧰 Tech Stack
- Frontend: Streamlit
- DL Model: ResNet50
- Backend: SerpAPI
- Database: MongoDB

## 📢 Future Enhancements

- Locate tumor in the image using YOLO
- Automated alerts to hospitals in extreme emergency cases
