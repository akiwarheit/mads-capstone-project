# Tired Parents - LLM Recommender Instructions

[Video Demo](https://umich-mads.slack.com/files/U01GNEPBSEB/F07GLU6AYSK/team-4-team-tired-parents.mp4?origin_team=TJWKJSBN3&origin_channel=C05RG8TH8AK)

[Project report](https://docs.google.com/document/d/1wU80AYTI1v_Bn-dqWXD4ImV5DDfHF_qTauIGNRl-npk/edit?usp=sharing)

# Authors:

Hsiao Chen Yeh - hcyeh@umich.edu

Kevin Deloria - kevinjd@umich.edu

# Environment setup

Make sure you have aws cli installed & setup.

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

This will differ by environment (Mac, Windows, Linux).

Once you have the cli installed - login using the access & secret keys.

```shell
$ aws configure
AWS Access Key ID [None]: {key}
AWS Secret Access Key [None]: {secret}
Default region name [None]: us-east-1
Default output format [None]: json
```

# How to Run Code:

Make sure to create a .venv using Python 3.11
Install requirements:

```
pip install -r requirements.txt
```

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

In order to generate interactive map visualization:

- run cells in 1_se_data_preprocessing.ipynb to generate pickle files
- run cells in 2a_se_vis.ipynb, this will generate a html file located in the mapVis directory

In order to run chatbot app:

- Start backend service in the API directory (you will not be able to do this if you don't have credentials for our AWS instance, need to host your own)

```shell
python application.py -key <key> -secret <secret>
```

- Start the front end service

```shell
cd chatbot-app
npm i && npm run start
```

- Navigate to localhost with the port you specified

# Data Access Statement

The data that ended up being used in this project was sourced from Social Explorer, accessible through a subscription provided by the University of Michigan. Although Social Explorer’s data is behind a paywall, we gained access via this link: https://www.lib.umich.edu/database/link/10387 as students. This platform provides a comprehensive range of demographic information about the United States.
