import gradio as gr
from typing import List
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
import torch
from .utils import logger


class Text2Sql:
    
    def __init__(self, model_name: str, max_token_limit: int= 1024):
        
        self._device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.max_token_limit = max_token_limit
        
        self.tokenizer = AutoTokenizer.from_pretrained( f"{model_name}-tokenizer" )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self._device)
        
        print('\n\n\n')
        logger.info(f"Using {(self._device).upper()} ...\n\n\n")
            
    def tokenize(self, input_prompt: str) -> List[int]:
        input_prompt = input_prompt.lower()
        return self.tokenizer.encode(input_prompt, return_tensors= 'pt')
    
    def predict(self, input_ids: List[int]) -> str:
        
        input_ids = input_ids.to(self._device)
        
        output = self.model.generate(input_ids, max_length = self.max_token_limit, do_sample=True)
        generated_query = self.tokenizer.decode(output[0], skip_special_tokens= True)
        return generated_query


llm = Text2Sql('fine-tuned-FLAN-T5')    