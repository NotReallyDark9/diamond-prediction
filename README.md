# Diamond Price Prediction Flask App

This repository contains a Flask application that predicts diamond prices. The prediction is based on features like carat, shape, cut, color, clarity, and report type.

## Features

- Predict diamond prices based on user input.
- Simple and intuitive user interface.
- REST API endpoint for predictions.

## Installation

To run this project, you will need to set up a Python environment and install the necessary packages.

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. It's recommended to set up a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the requirements:
```
pip install -r requirements.txt
```
4, Install random_forest_model.joblib: </p>
Since GitHub doesn't allow to upload 300mb file, I had to put it in Google Drive, you can download it [Here](https://drive.google.com/file/d/1XK0GvrZ-Q1SOLvVLYVp-Bfghb_LPksay/view?usp=drive_link). Put it in the main folder.

## Usage
To start the Flask server, run:
```flask run```
Or directly with python:
```python app.py```
Once the server is running, navigate to **http://127.0.0.1:5000/** in your web browser to use the application.

## API
You can also access the prediction functionality through the REST API endpoint:
```POST /predict```
Send a POST request with JSON content containing the diamond features, and you will receive a JSON response with the predicted price.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](https://docs.github.com/en/rest/licenses/licenses?apiVersion=2022-11-28) for details.
