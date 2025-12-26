from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

#Fetch the model and initialize a tokeniser
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

#Keeping track of conversation history

conversation_history = []

#Encoding the conversation history

history_string = "\n".join(conversation_history)

