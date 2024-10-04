# Corporate Forecasting using Traditional AI and Generative AI

This is my first project about **Artificial Intelligence** in CRM context. Moreover, this is also a part of my Bachelor's Degree final thesis on "*Corporate Forecasting using Shallow and Generative Learning Models: A CRM Department Use Case*", a thesis in which I analyze a dataset from an Iranian telecommunication company where combining forecasting models using **machine Learning techniques** and purposing an approach with Generative AI using Llama 3.1B to create a Conversational Assistant for a CRM Analyst.

## Structure of the Project
There are two script files in **Python**, one for analysis done via [Traditional AI models](Trad-AI.ipynb) and the other for construction and analysis via [Generative AI](Chatbot-test.py).

## Traditional AI techniques:
In the first analysis, dataset appeared like that: ![Dataset](https://github.com/user-attachments/assets/35f78923-8ea1-478a-a25c-f5a36d9d6a5b)
Then, after a **Data Preparation** (Data Cleaning + Feature Engineering) and an **Explorative Data Analysis (EDA)**, I analyzed customer churn using various methods:
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
![Churn Rate influenced by](https://github.com/user-attachments/assets/1d2b0502-6851-48db-966a-fb77135b5700)
![Extracting insights from dataset](https://github.com/user-attachments/assets/7668f69b-bb64-4529-9278-67ee512ac989)
![Build the best machine learning model_1](https://github.com/user-attachments/assets/5fe69ee1-e558-47c4-83ab-ed824e1e7946) ![Build the best machine learning model_2](https://github.com/user-attachments/assets/b98ab09d-24be-492b-8849-fa15b57a3e65)

## Conclusions
So, who won this AI showdown? Well, that depends on what you value most. If you are looking for precision, reliability, and those kinds of insights that make you look like a genius in the boardroom, traditional AI is still hard to beat. The Random Forests and logistic regressions we used in this project delivered solid results with clear explanations, which is something any data scientist or business leader-would appreciate. But if you're fortunate to work in one of those dynamic environments that forces one to think on the spot, accept rapid change, and perfect a great many what-if scenarios, then generative AI offers some serious benefits. It's imperfect but indisputably powerful, and there's a bright promise in store or its future-more so as the technology continues to mature. 

After all, this thesis did not compare two AI models but underlined strengths and weaknesses for two fundamentally different ways of doing problem-solving in AI. Traditional AI is akin to a well-crafted tool: highly effective in the right hands. Generative AI is more like a Swiss Army knife-versatile, full of potential, but still needing a bit more refinement to reach full potential.

