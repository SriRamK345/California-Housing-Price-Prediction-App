```markdown
# California Housing Price Prediction App

This is a simple web application built using **Streamlit** to predict housing prices based on the California Housing dataset. The app allows users to input various features of a house and provides an estimated price.

## Table of Contents

- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [License](#license)

## Demo

![Demo Image](demo_image.png)  <!-- Replace with a demo image if you have one -->

## Technologies Used

- Python
- Streamlit
- scikit-learn
- joblib
- NumPy

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/california-housing-price-prediction.git
   cd california-housing-price-prediction
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Train and save the model (if not already done):
   ```bash
   python model.py
   ```

## Usage

To run the Streamlit app, use the following command:

```bash
streamlit run app.py
```

Open your web browser and go to `http://localhost:8501` to access the app.

### Input Features

The app requires the following inputs to make a prediction:

- Median Income (in $10,000s)
- House Age (in years)
- Average Number of Rooms
- Average Number of Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

### Prediction

After entering the values, click the "Predict" button to see the estimated house price.

## Model Training

The model is trained using the California Housing dataset from **scikit-learn**. The following steps are taken:

1. Load the dataset.
2. Split the data into training and testing sets.
3. Train a **Linear Regression** model.
4. Save the trained model using `joblib`.
