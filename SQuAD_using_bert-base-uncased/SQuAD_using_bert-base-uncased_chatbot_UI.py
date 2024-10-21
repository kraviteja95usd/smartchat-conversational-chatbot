# Import necessary libraries
import gradio as gr
import torch
from transformers import BertTokenizerFast, BertForQuestionAnswering
import gc

# Create a context store
context_store = []


def update_context_store(context, question, answer):
    """
    Update the context store with the provided context, question, and answer.

    Args:
        context (str): The context related to the question.
        question (str): The question that was asked.
        answer (str): The answer generated for the question.
    """
    context_store.append({"context": context, "question": question, "answer": answer})


# Function to retrieve information from the context store
def retrieve_from_context_store(question):
    """
    Retrieve the context from the context store that matches the given question.

    Args:
        question (str): The question to search for in the context store.

    Returns:
        str or None: The matching context if found, otherwise None.
    """
    for item in context_store:
        if question in item["question"]:
            return item["context"]
    return None


# Function to load the tokenizer and model
def load_model_and_tokenizer():
    """
    Load the pre-trained BERT model and tokenizer for question answering.

    Returns:
        tuple: A tuple containing the tokenizer, model, and device.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Loading model on device: {device}")

    model_save_path = "squad-bert-trained/saved_model"
    model = BertForQuestionAnswering.from_pretrained(model_save_path)
    tokenizer = BertTokenizerFast.from_pretrained(model_save_path)

    model.eval()
    model.to(device)

    gc.collect()
    torch.cuda.empty_cache()

    return tokenizer, model, device


# Load the model and tokenizer
tokenizer, model, device = load_model_and_tokenizer()


# Function to generate answers
def generate_answer(context, question):
    """
    Generate an answer for the given question based on the provided context.

    Args:
        context (str): The context related to the question.
        question (str): The question to be answered.

    Returns:
        str: The generated answer, or an error message if an error occurs.
    """
    try:
        max_context_size = 512
        chunk_size = max_context_size

        chunks = [context[i:i + chunk_size] for i in range(0, len(context), chunk_size)]

        answers = []
        for chunk in chunks:
            inputs = tokenizer(chunk, question, return_tensors='pt', truncation=True, max_length=max_context_size).to(device)

            with torch.no_grad():
                outputs = model(**inputs)
                answer_start_scores = outputs.start_logits
                answer_end_scores = outputs.end_logits

                answer_start = torch.argmax(answer_start_scores)
                answer_end = torch.argmax(answer_end_scores) + 1

                answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][answer_start:answer_end]))

                answers.append(answer)

        answer = ' '.join(answers)
        answer = answer.replace('[CLS]', '')

        return answer.strip()

    except Exception as e:
        print(f"Error during generation: {e}")
        return "❌ An error occurred while generating the answer."


# Gradio Interface
def chatbot_interface():
    """
    Create the Gradio interface for the chatbot.

    Returns:
        gr.Blocks: A Gradio interface with context-aware chatbot functionality.
    """
    with gr.Blocks() as demo:
        # Adding custom CSS for beautifying the interface
        gr.Markdown("""
            <style>
                body {
                    background-color: #f0f0f0;  /* Light gray background */
                }
                .chatbot-container {
                    background-color: #ffffff;  /* White background for chatbot area */
                    border-radius: 10px;
                    padding: 20px;
                    color: #333;  /* Dark text color */
                    font-family: Arial, sans-serif;
                }
                .gr-button {
                    background-color: #4CAF50;  /* Green button */
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-size: 14px;
                    cursor: pointer;
                }
                .gr-button:hover {
                    background-color: #45a049;  /* Darker green on hover */
                }
                .gr-textbox {
                    background-color: #ffffff;  /* White background for textboxes */
                    color: #333;  /* Dark text color in textbox */
                    border-radius: 5px;
                    border: 1px solid #ddd;
                    padding: 10px;
                }
                .gr-chatbot {
                    background-color: #e6e6e6;  /* Light gray background for chatbot */
                    border-radius: 10px;
                    padding: 15px;
                    color: #333;
                }
                .status-message {
                    color: #007bff;  /* Blue status message */
                    font-weight: bold;
                }
                .footer {
                    text-align: right;
                    font-size: 12px;
                    color: #777;
                    font-style: italic;
                }
            </style>
        """)

        gr.Markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 SmartChat: A Context-Aware Conversational Agent</h1>")
        gr.Markdown("<p style='text-align: center; color: #777;'>Set a context and then ask multiple questions based on that context.</p>")

        context_state = gr.State()

        with gr.Row():
            with gr.Column(scale=1):
                context_input = gr.Textbox(
                    label="Set Context",
                    placeholder="Enter the context here...",
                    lines=4
                )
                set_context_btn = gr.Button("Set Context")

                clear_context_btn = gr.Button("Clear Context")

                status_message = gr.Markdown("")

            with gr.Column(scale=2):
                chatbot = gr.Chatbot(label="Chatbot")

        question_input = gr.Textbox(
            label="Ask a Question",
            placeholder="Enter your question here...",
            lines=1
        )
        submit_btn = gr.Button("Submit Question")

        footer = gr.Markdown("""
            <div style='display: flex; justify-content: space-between; font-size: 12px; color: #777;'>
                <p style='margin: 0;'>Trained using: bert-base-uncased</p>
                <p style='margin: 0;'>Prepared by: Ravi Teja Kothuru, Soumi Ray and Anwesha Sarangi</p>
            </div>
        """)

        def set_context(context):
            """
            Set the provided context for future question-answering.

            Args:
                context (str): The context to set.

            Returns:
                tuple: A tuple of updated UI components after setting the context.
            """
            if not context.strip():
                return gr.update(), "Please enter a valid context.", None
            return gr.update(visible=False), "Context has been set. You can now ask questions.", context

        def clear_context():
            """
            Clear the current context.

            Returns:
                tuple: A tuple of updated UI components after clearing the context.
            """
            return gr.update(visible=True), "Context has been cleared. Please set a new context.", None

        def handle_question(question, history, context):
            """
            Handle the question by generating an answer based on the context.

            Args:
                question (str): The question to answer.
                history (list): The conversation history.
                context (str): The context for generating the answer.

            Returns:
                tuple: Updated conversation history and the cleared question input.
            """
            if not context:
                return history, "Please set the context before asking questions."
            if not question.strip():
                return history, "Please enter a valid question."

            answer = generate_answer(context, question)
            history = history + [[f"👤: {question}", f"🤖: {answer}"]]
            return history, ""

        set_context_btn.click(set_context, inputs=context_input, outputs=[context_input, status_message, context_state])
        clear_context_btn.click(clear_context, inputs=None, outputs=[context_input, status_message, context_state])
        submit_btn.click(
            handle_question,
            inputs=[question_input, chatbot, context_state],
            outputs=[chatbot, question_input]
        )

    return demo


if __name__ == "__main__":
    demo = chatbot_interface()
    demo.launch()
