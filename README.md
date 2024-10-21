## Contents

1. [Repository Name](#repository-name)
2. [Title of the Project](#title-of-the-project)
3. [Short Description of the Project](#short-description-of-the-project)
4. [Objectives of the Project](#objectives-of-the-project)
5. [Name of the Dataset](#name-of-the-dataset)
6. [Description of the Dataset](#description-of-the-dataset)
7. [Goal of the Project using this Dataset](#goal-of-the-project-using-this-dataset)
8. [Size of the dataset](#size-of-the-dataset)
9. [Algorithms which are used as part of our investigation](#algorithms-which-are-used-as-part-of-our-investigation)
10. [Project Requirements](#project-requirements)
11. [Usage of the Project](#usage-of-the-project)
12. [Which chatbot architecture should the users use](#which-chatbot-architecture-should-the-users-use)
13. [Authors](#authors)

# Repository Name
smartchat-conversational-chatbot

# Title of the Project
SmartChat: A Context-Aware Conversational Agent

# Short Description of the Project
Develop a chatbot that can effectively adapt to context and topic shifts in a conversation, leveraging the Stanford Question Answering Dataset to provide informed and relevant responses, and thereby increasing user satisfaction and engagement.

# Objectives of the Project
Create a user-friendly web or app interface that enables users to have natural and coherent conversations with the chatbot, with high satisfaction rating.

# Name of the Dataset
The dataset used in this project is **Stanford Question Answering Dataset**.

**Data Source:** [Kaggle](https://www.kaggle.com/datasets/stanfordu/stanford-question-answering-dataset)

**Type of the Dataset:** Text

# Description of the Dataset
The Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset consisting of questions posed by crowdworkers on a set of Wikipedia articles. The answer to every question is a segment of text, or span, from the corresponding reading passage. There are 100,000+ question-answer pairs on 500+ articles.
More information can be found at: https://rajpurkar.github.io/SQuAD-explorer/

# Goal of the Project using this Dataset
- The goal of the project is to develop a chatbot that can carry out multi-turn conversations, adapt to context, and handle a variety of topics.

# Size of the Dataset:
- The dataset has 2 JSON files. One is for training and the other is for testing
  - dev-v1.1.json – 4.9 MB
  - train-v1.1.json – 30.3 MB

# Algorithms which are used as part of our investigation
- 2 different architectures are used:
  - GPT2-Medium architecture using LoRA and PEFT
  - BERT (bert-base-uncased)

# Project Requirements
- python3
- datasets 
- torch 
- peft 
- transformers 
- evaluate 
- safetensors 
- numpy 
- pandas 
- matplotlib 
- scikit-learn 
- seaborn
- nltk 
- rouge-score
- rouge
- gradio
- tqdm

# Usage of the Project
- Goto [SQuAD Dataset Preprocessing](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/tree/main/pre-processing) and ensure that you have `train-v1.1.json` and `dev-v1.1.json` files. 
  - In case you don't have them, you can download them [here](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/SQuAD_using_bert-base-uncased/dev-v1.1.json) and [here](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/SQuAD_using_bert-base-uncased/train-v1.1.json)
- Goto [SQuAD Dataset Preprocessing](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/pre-processing/SQuAD_Dataset_preprocessing.ipynb) file and run all the cells.
- To execute and view the results of BERT (bert-base-uncased) approach, please go through the instructions provided in the [SQuAD_chatbot_using_bert-base-uncased_README.md](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/SQuAD_using_bert-base-uncased/SQuAD_chatbot_using_bert-base-uncased_README.md) file.
- To execute and view the results of GPT (gpt2-medium using LoRA and PEFT) approach, please go through the instructions provided in the [SQuAD_chatbot_using_gpt2-medium_README.md](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/SQuAD_using_gpt2-medium/SQuAD_chatbot_using_gpt2-medium_README.md) file.

# Which chatbot architecture should the users use
- Actually, both the chatbots are running well.
- [SQuAD_using_gpt2-medium](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/SQuAD_using_gpt2-medium) generates the answers but most of the times it has issues.
  - For more information on the observations and technical details, refer [training](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/SQuAD_using_gpt2-medium/squad_lora_gpt2_medium_training.ipynb) and [validation](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/SQuAD_using_gpt2-medium/squad_lora_gpt2_medium_validation.ipynb) files.
- [SQuAD_using_bert-base-uncased](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/SQuAD_using_bert-base-uncased) is working very well as expected.
- Final conclusion is: Users can use any chatbot. But for perfect generation of answers, make use of [SQuAD_using_bert-base-uncased](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/blob/main/SQuAD_using_bert-base-uncased).

# Authors
| Author            | Contact Details         |
|-------------------|-------------------------|
| Ravi Teja Kothuru | rkothuru@sandiego.edu   |
| Soumi Ray         | soumiray@sandiego.edu   |
| Anwesha Sarangi   | asarangi@sandiego.edu   |
