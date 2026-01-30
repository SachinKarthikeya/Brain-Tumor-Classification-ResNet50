# Brain Tumor Classification with BrainyBot

A deep learning-powered web application that performs **brain tumor classification from MRI images** using **ResNet50**, and provides **personalized medical assistance** via **SerpAPI chatbot**. The app is built with **Tensorflow** for the model, **Streamlit** for the frontend, and integrates **Llama3.2:1b** model for in detailed tumor description.

## Features

- **Brain Tumor Classification** (Glioma, Meningioma, Pituitary, No Tumor) using ResNet50.
- **Emergency Assessment** with detailed explanations and recommended actions using Llama3.2:1b.
- **Nearby Hospital Finder** based on user’s city or area using SerpAPI.
- **Interactive Interface** with real-time image upload and classification via Streamlit.

## Workflow

- User uploads an MRI image via the Streamlit interface.
- The image is preprocessed and passed through the trained ResNet50 model.
- The model predicts the tumor type and gives a brief information about symptoms and treatment options.
- An AI chatbot answers user queries and helps find nearby hospitals.

## Tech Stack
- Frontend: Streamlit
- DL Model: ResNet50
- Backend: SerpAPI
- AI: Llama3.2:1b via Ollama

## Future Enhancements

- Locate tumor in the image using YOLO
- Save uploaded image with the classified tumor type in a NoSQL database 
