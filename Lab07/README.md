
# Lab 7: Image Classification with Caltech-101 Dataset and Explainability using Grad-CAM

This project focuses on training and evaluating three deep learning models (VGG19, ResNet50, and EfficientNet-B0) for image classification using the Caltech-101 dataset. The project also incorporates Explainable AI (XAI) techniques, specifically Grad-CAM, to visualize model decision-making processes.

## Objectives
- Classify images into one of 101 categories using convolutional neural networks (CNNs).
- Implement and compare pre-trained models: VGG19, ResNet50, and EfficientNet-B0.
- Evaluate the models on various metrics, including Top-k accuracy, per-class accuracy, and a classification report.
- Visualize the decision-making process using Grad-CAM.
- Visualize feature embeddings with t-SNE for global interpretability.

## Dataset
The Caltech-101 dataset contains images from 101 object categories and 1 background category. Images per category range from 40 to 800, with a total of approximately 9,146 images. Images are resized and preprocessed for consistency.

## Requirements
### Libraries
- Python 3.10+
- PyTorch
- torchvision
- scikit-learn
- matplotlib

### Installation
Run the following commands to install the required libraries:
```bash
pip install torch torchvision scikit-learn matplotlib
```

## Features
### 1. **Dataset Preprocessing**
- Resize images to 128x128 pixels.
- Apply data augmentation techniques like rotation, flipping, and color jitter.
- Normalize images based on ImageNet standards.

### 2. **Models**
- **VGG19**: Pre-trained on ImageNet, final layer adjusted for 101 classes.
- **ResNet50**: Pre-trained on ImageNet, final layer adjusted for 101 classes.
- **EfficientNet-B0**: Pre-trained on ImageNet, final layer adjusted for 101 classes.

### 3. **Evaluation Metrics**
- Confusion Matrix
- Classification Report
- Top-k Accuracy
- Per-Class Accuracy

### 4. **Explainable AI**
- Grad-CAM visualization highlights regions contributing to model predictions.
- Visualizations include an "autumn" background with a jet overlay.

### 5. **t-SNE Visualization**
- Projects high-dimensional feature embeddings into 2D space for visual analysis.

## How to Run
1. Clone this repository or copy the code into a Python environment.
2. Ensure the Caltech-101 dataset is available at the specified path (`/kaggle/input/caltech-101-f`).
3. Execute the script to train, validate, and evaluate all three models.



## Results
- The script provides detailed evaluation metrics and visualizations for each model.
- Grad-CAM and t-SNE visualizations aid in understanding the models' decision-making processes.

## Project Structure
- **train_model**: Trains the models.
- **validate_model**: Evaluates validation accuracy.

## Example Outputs
1. **Grad-CAM Visualization**:
   - Highlights areas influencing the model's predictions.

2. **t-SNE Visualization**:
   - Visualizes the separability of classes in 2D space.

## Acknowledgments
- Dataset: [Caltech-101](http://www.vision.caltech.edu/Image_Datasets/Caltech101/).
- Grad-CAM implementation inspired by `pytorch-grad-cam` library.

## Future Improvements
- Implement hyperparameter tuning.
- Save models and visualizations for reproducibility.
