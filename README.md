
# Tired Parents - LLM Recommender Instructions
[Video Demo](https://umich-mads.slack.com/files/U01GNEPBSEB/F07GLU6AYSK/team-4-team-tired-parents.mp4?origin_team=TJWKJSBN3&origin_channel=C05RG8TH8AK)

[Project report](https://docs.google.com/document/d/1wU80AYTI1v_Bn-dqWXD4ImV5DDfHF_qTauIGNRl-npk/edit?usp=sharing)

# Authors:
Hsiao Chen Yeh - hcyeh@umich.edu

Kevin Deloria - kevinjd@umich.edu

# How to Run Code:
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

# Data Access Statement
The data that ended up being used in this project was sourced from Social Explorer, accessible through a subscription provided by the University of Michigan. Although Social Explorer’s data is behind a paywall, we gained access via this link: https://www.lib.umich.edu/database/link/10387  as students. This platform provides a comprehensive range of demographic information about the United States.
