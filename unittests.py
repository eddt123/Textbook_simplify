import unittest
import os
from llama_cpp import Llama
from main import extract_text_from_pdf, prompt_and_simplify

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.LLM = Llama(model_path="./model/llama-2-7b-chat.ggmlv3.q2_K.bin", n_ctx=2048)

    def test_extract_text_from_pdf(self):
        test_folder = 'test'
        test_pdf = [file for file in os.listdir(test_folder) if file.endswith('.pdf')][0]  # Get the first PDF in the 'test' folder
        text = extract_text_from_pdf(os.path.join(test_folder, test_pdf))
        print(text)
        # Check if the function extracts any text. The actual content would depend on your test PDF.
        self.assertNotEqual(text, '')

    def test_prompt_and_simplify(self):
        test_text = "The following is an extract from a book, I want you to simplify the language slightly. Only reply with the simplified extract."
        simplified_text = prompt_and_simplify(self.LLM, test_text)
        print(simplified_text)
        # Check if the function returns a non-empty string. The exact content would vary depending on Llama's output.
        self.assertTrue(isinstance(simplified_text, str))
        self.assertNotEqual(simplified_text, '')

if __name__ == '__main__':
    unittest.main()