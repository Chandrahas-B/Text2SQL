from text2sql import model
import gradio as gr

def main(input_prompt, history):
    
    input_ids = model.tokenize(input_prompt)
    query = model.predict(input_ids)
    
    return f"{query}"

if __name__ == '__main__':
    demo = gr.ChatInterface(fn= main, title= "Text 2 SQL", chatbot=gr.Chatbot(height= 500))
    demo.launch(server_name="0.0.0.0", server_port= 7861)