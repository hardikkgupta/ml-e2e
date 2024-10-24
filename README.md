# ml-e2e
![cover](data/cover.png)

## Overview
This repository contains a complete end-to-end pipeline for building, deploying, and serving a machine learning model using Docker, Flask, AWS, and CI/CD with GitHub Actions. The pipeline includes data gathering, model building, API development, Dockerization, and deployment using AWS EC2.

![Description](data/timeline.png)

## Project Structure
- **app/**: Contains the application code including the Flask API (`app.py`) and utility functions (`utils.py`).
- **model.py**: Script for training and saving the machine learning model.
- **Dockerfile**: Defines the Docker image for the Flask application.
- **ci-cd.yml**: GitHub Actions workflow for CI/CD, automating linting, testing, Docker image building, and deployment.
- **tests/**: Contains unit tests for the utility functions (`test_utils.py`).

## Requirements
- Python 3.12
- Flask
- Scikit-learn
- Joblib
- Docker
- AWS CLI
- GitHub Actions for CI/CD

## How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/hardikkgupta/ml-e2e.git
   ```
2. Navigate to the project directory and create a virtual environment:
   ```bash
   cd ml-e2e
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Train the model and save it:
   ```bash
   python model.py
   ```
5. Run the Flask API:
   ```bash
   python app/app.py
   ```

## Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t ml-flask-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 ml-flask-app
   ```