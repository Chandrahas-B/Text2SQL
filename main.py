from text2sql.app import llm
import gradio as gr

def main(input_prompt, history):
    
    input_ids = llm.tokenize(input_prompt)
    query = llm.predict(input_ids)
    
    return f"{query}"

if __name__ == '__main__':
    demo = gr.ChatInterface(fn= main, title= "Text 2 SQL", chatbot=gr.Chatbot(height= 500))
    demo.launch()