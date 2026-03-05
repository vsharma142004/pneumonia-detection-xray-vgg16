🫁 Pneumonia Detection from Chest X-Ray Images using VGG16

This project implements a deep learning model using VGG16 transfer learning to automatically detect pneumonia from chest X-ray images. The model analyzes chest radiographs and classifies them as Normal or Pneumonia.

The system was developed using TensorFlow and Keras, with data preprocessing, augmentation, and model fine-tuning. The trained model was deployed as an interactive web application using Streamlit on Hugging Face Spaces, allowing users to upload X-ray images and receive predictions in real time.

🚀 Features

Deep learning model based on VGG16 transfer learning

Binary classification of chest X-ray images (Normal vs Pneumonia)

Image preprocessing and normalization

Data augmentation to improve generalization

88.6% test accuracy on unseen data

Interactive Streamlit web application

Cloud deployment on Hugging Face Spaces

🧠 Model Architecture

The model uses VGG16 as a pretrained convolutional base and adds custom classification layers.

Architecture Flow
Input Image (96x96x3)
        │
     VGG16
 (Pretrained CNN)
        │
      Flatten
        │
      Dense
        │
     Dropout
        │
      Dense
        │
   Sigmoid Output

Output Classes:

Normal

Pneumonia

📊 Model Performance
Metric	Value
Model	VGG16 Transfer Learning
Task	Binary Image Classification
Test Accuracy	88.6%
Framework	TensorFlow / Keras
📂 Dataset

The model was trained using the Chest X-Ray Pneumonia Dataset.

Dataset Source:

https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

The dataset contains labeled chest X-ray images categorized as Normal or Pneumonia.

Dataset Structure
chest_xray
│
├── train
│   ├── NORMAL
│   └── PNEUMONIA
│
├── val
│
└── test
⚙️ Technologies Used

Python

TensorFlow

Keras

NumPy

Streamlit

OpenCV

Matplotlib

Pillow

📂 Project Structure
pneumonia-detection-xray-vgg16
│
├── app.py
├── requirements.txt
├── pneumonia_model_training.ipynb
└── README.md
💻 Installation

Clone the repository:

git clone https://github.com/yourusername/pneumonia-detection-xray-vgg16.git

Navigate into the project folder:

cd pneumonia-detection-xray-vgg16

Install dependencies:

pip install -r requirements.txt
▶️ Running the Application

Run the Streamlit app:

streamlit run app.py

The application will open in your browser where you can upload chest X-ray images and view predictions.

🌐 Live Demo

Try the deployed application here:

Hugging Face Space

https://huggingface.co/spaces/yourusername/pneumonia-detector

Upload a chest X-ray image to receive an AI-generated pneumonia prediction.

📸 Application Interface

(Add screenshot here after uploading one)

Example:

![App Screenshot](screenshots/demo.png)
⚠️ Disclaimer

This project is intended for educational and research purposes only.
It should not be used as a substitute for professional medical diagnosis.

👨‍💻 Author

Developed by Vaibhav Sharma

GitHub:
https://github.com/vsharma142004

⭐ If you found this project useful, consider giving it a star!
