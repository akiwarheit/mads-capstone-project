## README

Before using this project, ensure that you have the following installed:

- Python 3.8 or higher
- AWS CLI configured with appropriate access
- Docker (for running the Flask API)
- Node.js and npm (for running the web app)

## AWS SageMaker Endpoint

The project uses an AWS SageMaker endpoint for text generation. You need AWS CLI access to interact with this endpoint.

## Folder Structure

The repository is structured as follows:

- `api/`: Contains the Flask REST API that interacts with the SageMaker endpoint.
- `api/inference.py`: Defines the query_endpoint function to send requests to the SageMaker endpoint.
- `api/app.py`: The main Flask application that exposes an /ask endpoint.

## Getting Started

### Running the Flask API

1. Navigate to the api directory.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python app.py
```

The Flask API will be available at http://localhost:8080.

## Running the Web App

1. Navigate to the chatbot-app directory.
2. Install the required dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm start
```

The web application will be available at http://localhost:3000.
