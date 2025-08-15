from llama_cpp import Llama

# Load the model (update the path if it's different)
llm = Llama(model_path="mistral-7b-instruct-v0.1.Q4_K_M.gguf")

# Ask a simple question
output = llm("Q: Who is the leader of the boy band BTS\nA:", max_tokens=20)

print(output['choices'][0]['text'].strip())
