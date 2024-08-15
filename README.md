# Tired Parents - LLM Recommender Instructions

Make sure to create a .venv using Python 3.11
Install requirements:
```
pip install -r requirements.txt
```

Installing PyMuPDF in requirements.txt doesn't work, please run in terminal 

```terminal
pip install PyMuPDF
```

In order to generate interactive map visualization:
- run cells in 1_se_data_preprocessing.ipynb to generate pickle files
- run cells in 2a_se_vis.ipynb, this will generate a html file located in the mapVis directory

In order to run chatbot app:
- Start backend service in the API directory (you will not be able to do this if you don't have credentials for our AWS instance, need to host your own)
```angular2html
python application.py -key <key> -secret <secret>
```
- Start the front end service
```angular2html
npm run start
```
- Navigate to localhost with the port you specified