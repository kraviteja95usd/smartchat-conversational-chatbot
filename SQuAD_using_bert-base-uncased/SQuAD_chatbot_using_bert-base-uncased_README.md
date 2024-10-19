# Usage Instructions in Local System
- Clone using HTTPS
```commandline
https://github.com/kraviteja95usd/smartchat-conversational-chatbot.git
```
OR - 

- Clone using SSH
```commandline
git@github.com:kraviteja95usd/smartchat-conversational-chatbot.git
```

OR -

- Clone using GitHub CLI
```commandline
gh repo clone kraviteja95usd/smartchat-conversational-chatbot
```
 
- Switch inside the Project Directory
```commandline
cd smartchat-conversational-chatbot
```

- Install Requirements
```commandline
pip3 install -r requirements.txt
```

- Switch inside the Code Directory
```commandline
cd SQuAD_using_bert-base-uncased
```

- Open your terminal (Command Prompt in Windows OR Terminal in MacBook)
- Type any one of the below commands based on the software installed in your local system. You will notice a frontend webpage opened in the browser.
```commandline
jupyter notebook
```
OR -
```commandline
jupyter lab
```
- Step-1:
  - Click (Single click or double click whatever works) on the `SQuAD_using_bert-base-uncased_training_and_validation.ipynb` file.
  - You will notice the file opened.
  - Click `Run` button from the Menu bar and select the option of your interest (`Run Cell` or `Run All` button).
  - You can look at the execution results within the file and interpret accordingly.
    - !!! IMPORTANT NOTE AND DO NOT MISS THIS !!! 
      Ensure that all the code cells are properly and successfully without any errors.

- Step-2:
  Open the `SQuAD_using_bert-base-uncased_chatbot_UI.py` file and execute it. You will notice a link provided there. [Example Link is here](http://127.0.0.1:7860)
    - Click on the provided link and you will notice a window being opened in your browser.
    - Provide some context/paragraph at the left side textbox of your page and click on `Set Context` button.
    - Now, at the bottom of the page, you will find a section `Ask a Question` suggesting you to enter your question in its textbox. Do it and click on `Submit Question` button.
    - You will get your answer in the chat window.
      - !!! IMPORTANT NOTE AND DO NOT MISS THIS !!! 
          - Ensure that you are asking the question from the same context.
          - Ensure that if you ask your question without setting the context first, you will notice a message `Please set the context before asking questions.` at the bottom of the UI page.
          - If your system is in Dark mode, this UI page looks in the same theme. If you system is in Light mode, then you will view it in white color.
    - You can look at the execution results within the Notebook file as well as [here](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/tree/chatbot-by-ravi/SQuAD_using_bert-base-uncased/SQuAD_using_bert-base-uncased_chatbot_UI_Screenshots) and interpret accordingly.
      - Note that there are 2 PDFs and 2 word documents inside it. You can view anything to understand that. Whatever the word documents we have there, the PDFs also have the same content. I just uploaded both the formats.
