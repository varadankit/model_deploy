# Iris Species Classification API

## Overview
This project implements a machine learning model to classify Iris flower species based on sepal and petal measurements. It uses a logistic regression model, deployed as a Flask API on Azure Cloud Platform.

## Features
- Logistic Regression model trained on the Iris dataset
- Flask API for real-time predictions
- Dockerized application for easy deployment
- Deployed on Azure Container Instances

## Technical Stack
- Python 3.8
- scikit-learn for machine learning
- Flask for API development
- Docker for containerization
- Azure Container Instances for cloud deployment

## Setup and Deployment
1. Clone the repository
2. Build the Docker image: docker build -t iris-classification-api .
3. Push the image to a container registry (e.g., Docker Hub)
4. Deploy to Azure Container Instances using the Azure CLI or Azure Portal

## API Usage
Send a POST request to API (http://model-hegde.fcd2hxetacfxbtdq.japaneast.azurecontainer.io:5000/classify) with JSON data:

```json
{
 "sepal_length_cm": 5.1,
 "sepal_width_cm": 3.5,
 "petal_length_cm": 1.4,
 "petal_width_cm": 0.2
}
```
The API will respond with the predicted Iris species.

Examples:
```json
{"sepal_length_cm": 5.1,"sepal_width_cm": 3.5,"petal_length_cm": 1.4,"petal_width_cm": 0.2} //setosa
{"sepal_length_cm": 6.4,"sepal_width_cm": 3.2,"petal_length_cm": 4.5,"petal_width_cm": 1.5} //versicolor 
{"sepal_length_cm": 7.7,"sepal_width_cm": 3.0,"petal_length_cm": 6.1,"petal_width_cm": 2.3}  //virginica
{"sepal_length_cm": 5.1,"sepal_width_cm": 3.5, "petal_length_cm": 1.4} //error
```
