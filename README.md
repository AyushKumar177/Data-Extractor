# Data-Extractor
0: Introduction

This is our end to end project where we will create a data abstractor tool .
This tool will take an elaborated text and summarize it to give us the short information or abstract
the important information to give us the summary as the output.
It is a very useful tool as it helps to reduce our time in going through the whole data and gives us the summary in the least time.


1: Github Repository Setting

First we have set up the github repository and then connected it with our local machine to work on it
    git add .
    git commit -m "done"
    git push origin main

2: Project template creation

We created the template for the project initially
    conda create -n EVM python=3.8 -y
    activate EVM

3: Project setup 

We create a virtual environment first

4: requirement installation

We use hugging face
Now we will go to setup.py and write it
and the install rewuirements
    pip install -r requirements.txt

5: logging ,utils and exception module

now first we will create custom logging inside the __init__.py file
now we will configure the utils common.py file(for frequent function)

-------------------------------------------------------------------------
We create the python code for the NLP Data Abstractor using google collab
-------------------------------------------------------------------------
data : https://github.com/AyushKumar177/Data/raw/main/DataAbstractorData.zip
 upload it to research folder

6: project workflow
    1.update config.yaml file 
    2.update params.yaml
    3.update entity in src
    4.update configuration manager in src config
    5.update the components
    6.update pipeline
    7.update main.py
    8.update app.py

7: notebook experiment and testing
now we create 01_data_ingestion.ipynb and configure our config.yaml and then update entity for return type

8: component modular code implementation


9: training pipeline


10: prediction pipeline & user app creation


11: final ci/cd deployment on AWS


-----------------------------------------------
 
