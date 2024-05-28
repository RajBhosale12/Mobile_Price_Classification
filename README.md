# Mobile_Price_Classification

Project Overview
The Mobile Price Classification project aims to predict the price range of mobile phones based on various features such as Battery Power(mAh),Clock Speed,Front Camera Megapixels,5G Support (0 for No, 1 for Yes): ,Internal Memory (GB),Number of Cores(1 to 8),Primary Camera Megapixels(1 to 20).
This can help manufacturers and retailers to categorize new products appropriately and understand market trends better.

Project Structure :
mobile_price_classification/
├── static/
│ └── images/
│ ├── 1.jpg
│ ├── download.jfif
│ ├── mobile.jfif
│ └── th.jfif
├── templates/
│ └── index.html
├── app.py
├── main.py
├── model.pkl
├── train.csv
├── README.md
├── requirements.txt

static/
Contains static assets such as images used in the project.

templates/
Contains HTML templates for rendering web pages.

Root Directory
app.py: The main application file to run the web server or Flask application.
main.py: Script to run the main logic of the project, which could include model training or prediction.
model.pkl: Serialized model file (pickle) that contains the trained machine learning model.
train.csv: CSV file containing the training data used for building the model.
README.md: A markdown file that provides an overview of the project, how to set it up, and how to use it.
requirements.txt: A file that lists all the dependencies and libraries needed to run the project.

Dataset
The dataset used in this project is stored in train.csv, containing various features and price range labels.
