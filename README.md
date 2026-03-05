🫁 Pneumonia Detection from Chest X-Ray Images

This project implements a deep learning model using VGG16 transfer learning to automatically detect pneumonia from chest X-ray images. The system uses a convolutional neural network trained on medical imaging data to classify X-rays as Normal or Pneumonia.

The model was developed using TensorFlow and Keras, and deployed as an interactive Streamlit web application on Hugging Face Spaces, allowing users to upload chest X-ray images and receive real-time predictions.

🚀 Features

Deep learning model based on VGG16 transfer learning

End-to-end pipeline for medical image classification

Data preprocessing and augmentation for improved generalization

Achieved 88.6% accuracy on unseen test data

Streamlit web interface for easy interaction

Cloud deployment on Hugging Face Spaces

🧠 Model Architecture

The model uses VGG16 as the base CNN with transfer learning.

Steps used:

Load pretrained VGG16 convolutional base

Freeze early layers to retain learned features

Add custom classification layers

Fine-tune the network for pneumonia classification

Architecture:

Input Image (96x96)
       │
   VGG16 Base
       │
    Flatten
       │
    Dense Layer
       │
    Dropout
       │
 Sigmoid Output

Output classes:

Normal

Pneumonia

📊 Dataset

Dataset used:

Chest X-Ray Images (Pneumonia)

It contains labeled chest X-ray images for:

Normal lungs

Pneumonia infections

Dataset structure:

chest_xray
 ├── train
 │   ├── NORMAL
 │   └── PNEUMONIA
 ├── val
 └── test
⚙️ Technologies Used

Python

TensorFlow

Keras

NumPy

Streamlit

Hugging Face Spaces

OpenCV

🖥️ Web Application

The trained model is deployed using Streamlit, allowing users to upload an X-ray image and receive predictions.

Workflow:

Upload chest X-ray

Model preprocesses image

AI predicts pneumonia probability

Display diagnosis and confidence score

📈 Model Performance
Metric	Value
Test Accuracy	88.6%
Model	VGG16 Transfer Learning
Task	Binary Classification
📂 Project Structure
pneumonia-detector
│
├── app.py
├── chest_xray_vgg16_model.h5
├── requirements.txt
└── README.md
🌐 Live Demo

You can try the deployed application here:

Hugging Face Space:
https://huggingface.co/spaces/yourusername/pneumonia-detector

⚠️ Disclaimer

This project is intended for educational and research purposes only and should not be used as a substitute for professional medical diagnosis.
