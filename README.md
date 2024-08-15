# Data-Abstractor

## Introduction

The Data-Abstractor is an end-to-end tool designed to summarize extensive texts by extracting key information, providing a concise summary. This tool helps save time by offering quick overviews of lengthy documents, making it a valuable asset for efficient data processing.

## Table of Contents

1. [GitHub Repository Setup](#github-repository-setup)
2. [Project Template Creation](#project-template-creation)
3. [Project Setup](#project-setup)
4. [Requirement Installation](#requirement-installation)
5. [Logging, Utils, and Exception Module](#logging-utils-and-exception-module)
6. [Project Workflow](#project-workflow)
7. [Notebook Experiment and Testing](#notebook-experiment-and-testing)
8. [Component Modular Code Implementation](#component-modular-code-implementation)
9. [Prediction Pipeline & User App Creation](#prediction-pipeline--user-app-creation)
10. [Final CI/CD Deployment on AWS](#final-cicd-deployment-on-aws)

## GitHub Repository Setup

1. Set up the GitHub repository.
2. Connect it with your local machine.
3. Use the following Git commands to manage your repository:
    ```bash
    git add .
    git commit -m "done"
    git push origin main
    ```

## Project Template Creation

1. Create a virtual environment using Conda:
    ```bash
    conda create -n EVM 
    source activate base
    activate EVM
    ```

## Project Setup

1. Create and activate a virtual environment.

## Requirement Installation

1. Utilize Hugging Face libraries.
2. Write the setup in `setup.py`.
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Logging, Utils, and Exception Module

1. Create custom logging in `__init__.py`.
2. Configure utility functions in `common.py` for frequent use.
3. Develop the NLP Data Abstractor using Google Colab.
4. Upload the data from [this link](https://github.com/AyushKumar177/Data/raw/main/DataAbstractorData.zip) to the `research` folder.

## Project Workflow

1. Update `config.yaml`.
2. Update `params.yaml`.
3. Update entities in the `src` folder.
4. Update the configuration manager in `src/config`.
5. Update components.
6. Update the pipeline.
7. Update `main.py`.
8. Update `app.py`.

## Notebook Experiment and Testing

1. Create `01_data_ingestion.ipynb`.
2. Configure `config.yaml` and `params.yaml`.
3. Update the entity for return types.
4. Update components and pipeline.
5. Create the `artifacts` folder and its contents.
6. Convert to modular coding.

## Component Modular Code Implementation

1. Implement modular code using `01_data_ingestion.ipynb`.
2. Update `__init__.py` inside the `entity` folder.
3. Update `src/config/configuration.py`.
4. Update `src/components/data_ingestion.py`.
5. Update `pipeline/stage_01_data_ingestion.py`.
6. Write data ingestion stage code in `main.py`.
7. Exclude the `artifacts` folder from Git by adding it to `.gitignore`.

## Prediction Pipeline & User App Creation

1. Create the prediction pipeline in `pipeline/prediction.py`.
2. Develop the user application in `app.py`.
3. Set up hosting and port configurations.

## Final CI/CD Deployment on AWS

1. Deploy the project using CI/CD pipelines on AWS.

