import joblib
import cv2
import numpy as np
from skimage.feature import local_binary_pattern

def predict(file_path):
    try:
        # Load the pre-trained model
        model = joblib.load('model/modelGray3.pkl')
        
        # Parameters for LBP feature extraction
        radius = 1
        n_points = 8 * radius
        METHOD = 'uniform'

        # Load the image and convert it to grayscale
        image = cv2.imread(file_path)
        if image is None:
            return 'Error: Unable to load the image.'

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Preprocess the image (Gaussian blur)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        # Extract Local Binary Pattern (LBP) features
        lbp = local_binary_pattern(gray, n_points, radius, METHOD)
        
        # Calculate histogram of LBP features
        hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, n_points + 3), range=(0, n_points + 2))
        hist = hist.astype('float')
        hist /= (hist.sum() + 1e-7)

        # Make prediction using the model
        prediction = model.predict([hist])

        # Return the predicted class label
        if prediction[0] == "parkinson":
            return 'You may be Diagnosed with Parkinson'
        else:
            return 'You are Healthy!!'

    except Exception as e:
        return f'Error: {str(e)}'
