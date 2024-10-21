## Contents
1. [Usage Instructions and Execution Steps in Local System](#usage-instructions-and-execution-steps-in-local-system)
2. [How do I directly run this Chatbot](#how-do-i-directly-run-this-chatbot)
3. [Issues with this Model](#issues-with-this-model)

# Usage Instructions and Execution Steps in Local System
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
cd SQuAD_using_gpt2-medium
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
- Let me explain the step-by-step instructions of the code structure here.
- Step-1:
  - Click (Single click or double click whatever works) on the `squad_lora_gpt2_medium_training.ipynb` file.
  - You will notice the file opened.
  - Click `Run` button from the Menu bar and select the option of your interest (`Run Cell` or `Run All` button).
  - Repeat the same above 3 steps for `squad_lora_gpt2_medium_training.ipynb` file.
  - You can look at the execution results within the file and interpret accordingly.
    - !!! IMPORTANT NOTE AND DO NOT MISS THIS !!! 
      Ensure that all the code cells are properly and successfully without any errors.

- Step-2:
  Open the `SQuAD_using_gpt2-medium_chatbot_UI.ipynb` file and execute it. You will notice a link provided there. [Example Link is here](http://127.0.0.1:7860)
    - Click on the provided link and you will notice a window being opened in your browser.
    - Provide some context/paragraph at the left side textbox of your page and click on `Set Context` button.
    - Now, at the bottom of the page, you will find a section `Ask a Question` suggesting you to enter your question in its textbox. Do it and click on `Submit Question` button.
    - You will get your answer in the chat window.
      - !!! IMPORTANT NOTE AND DO NOT MISS THIS !!! 
          - Ensure that you are asking the question from the same context.
          - Ensure that if you ask your question without setting the context first, you will notice a message `Please set the context before asking questions.` at the bottom of the UI page.
          - If your system is in Dark mode, this UI page looks in the same theme. If you system is in Light mode, then you will view it in white color.
    - You can look at the execution results within the Notebook file as well as [here](https://github.com/kraviteja95usd/smartchat-conversational-chatbot/tree/main/SQuAD_using_gpt2-medium/SQuAD_using_gpt2-medium_chatbot_UI_Screenshots) and interpret accordingly.
      - Note that there are 2 folders inside it and there are screenshot files inside each of those folders. You can view anything to understand that.

## How do I directly run this Chatbot
- Clone the repository using the steps provided in [Usage Instructions and Execution Steps in Local System](#usage-instructions-and-execution-steps-in-local-system) section.
- Navigate inside `SQuAD_using_gpt2-medium` folder and open `jupyter notebook` or `jupyter lab` from this path using your terminal.
- Open the `SQuAD_using_gpt2-medium_chatbot_UI.ipynb` file and execute it. You will notice a link provided there. [Example Link is here](http://127.0.0.1:7860)
- Hit the link and you are good to go!

## Issues with this Model
- If you are using MacBook, I would suggest you to install a Virtual Box within it and install Ubuntu inside it. 
- Somehow, this model works only in Windows and Linux/Ubuntu. I have mentioned a note to have this resolved in the `Future Recommendations` section of the PPT. 
