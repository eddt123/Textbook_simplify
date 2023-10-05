import os
import PyPDF2
from llama_cpp import Llama

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

def prompt_and_simplify(model, text):
    prompt = (f"The following is an extract from a book, I want you to simplify the "
              f"language slightly and reduce the word count slightly, only reply with "
              f"the simplified extract: {text}")
    # Generate a response using the Llama model
    output = model(prompt, max_tokens=0)  # No limit on response size
    return output["choices"][0]["text"]

def save_text_to_file(text, filename, folder='processed_data'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, filename)
    with open(file_path, "w") as file:
        file.write(text)

if __name__ == '__main__':
    # Load Llama 2 model
    LLM = Llama(model_path="./model/llama-2-7b-chat.ggmlv3.q2_K.bin", n_ctx=2048)

    # Iterate over all PDFs in the 'data' folder
    data_folder = 'data'
    for filename in os.listdir(data_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(data_folder, filename)
            extracted_text = extract_text_from_pdf(pdf_path)
            
            # Splitting the extracted text into 1500-word chunks
            words = extracted_text.split()
            for i in range(0, len(words), 1500):
                chunk = " ".join(words[i:i+1500])
                simplified_text = prompt_and_simplify(LLM, chunk)
                
                # Construct the filename for the simplified chunk
                output_filename = f"{os.path.splitext(filename)[0]}-{(i // 1500) + 1}.txt"
                
                # Save the simplified text to the 'processed_data' folder
                save_text_to_file(simplified_text, output_filename)




