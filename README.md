# Corporate Forecasting using Traditional AI and Generative AI

This is my first project about **Artificial Intelligence** in CRM context. Moreover, this is also a part of my Bachelor's Degree final thesis on "*Corporate Forecasting using Shallow and Generative Learning Models: A CRM Department Use Case*", a thesis in which I analyze a dataset from an Iranian telecommunication company where combining forecasting models using **machine Learning techniques** and purposing an approach with Generative AI using Llama 3.1B to create a Conversational Assistant for a CRM Analyst.

## Structure of the Project
There are two script files in **Python**, one for analysis done via [Traditional AI models](Trad-AI.ipynb) and the other for construction and analysis via [Generative AI](Chatbot-test.py).

## Traditional AI techniques:
In the first analysis, dataset appeared like that: ![Dataset](https://github.com/user-attachments/assets/35f78923-8ea1-478a-a25c-f5a36d9d6a5b), then, after a **Data Preparation** (Data Cleaning + Feature Engineering) and an **Explorative Data Analysis (EDA)**, I analyzed customer churn using various methods:
* **Random Forest Classifier**: an ensemble model to enhance accuracy and reduce overfitting, showing the feature importance.
![Feature Importance RF](https://github.com/user-attachments/assets/e260912c-274c-4b42-ab32-0f64d7286bb6)

* **Stacked Ensemble Model**: it combines multiple base models, leveraging their strengths to produce superior predictive performance.
![Classification Report Stacked](https://github.com/user-attachments/assets/612a5d63-18db-453d-b0d5-7c38f3e244d5)

* **Artificial Neural Network (ANNs)**: deep learning models that mimic the brain's structure, excelling at learning non linear relationships and complex patterns.
![ANN visualize](https://github.com/user-attachments/assets/fb48118f-dc08-4096-97fb-910fdb4ae0e7)

The main aim was to come up with some important factors that cause customer churn and evaluate the performance of these models in predicting churn.

## Conversational Assistant:
In the second analysis, I chose **Llama 3.1** to build my Conversational Assistant because of its superior natural language understanding and context-based response generation. The success in getting Llama 3.1 to perform did not come in one fell swoop; it took numerous passes, one prompt at a time. This created a need for several iterations in fine-tuning prompts (**prompt engineering**).

Below are the key results:
* ![Extracting insights from dataset](https://github.com/user-attachments/assets/7668f69b-bb64-4529-9278-67ee512ac989)
* ![Build the best machine learning model_1](https://github.com/user-attachments/assets/5fe69ee1-e558-47c4-83ab-ed824e1e7946) ![Build the best machine learning model_2](https://github.com/user-attachments/assets/b98ab09d-24be-492b-8849-fa15b57a3e65)

