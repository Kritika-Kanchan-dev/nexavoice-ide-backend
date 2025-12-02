import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



class GeminiAssistant:

    def debug_code(self, code):
        prompt = f"""
You are an expert programmer. Debug the following code and return:
1. Error Explanation
2. Exact Lines Causing Error
3. Corrected Code
4. Suggestions

Code:
{code}
"""
        response = genai.GenerativeModel("gemini-pro-latest").generate_content(prompt)
        return response.text

    def auto_fix_code(self, code):
        prompt = f"""
Fix ALL errors in this code and return ONLY the corrected version:

{code}
"""
        response = genai.GenerativeModel("gemini-pro-latest").generate_content(prompt)
        return response.text

    def generate_testcases(self, code):
        prompt = f"""
Generate comprehensive Python unittest test cases for the following code.
Return ONLY the test code.

Code:
{code}
"""
        response = genai.GenerativeModel("gemini-pro-latest").generate_content(prompt)
        return response.text
    
    def generate_code(self, prompt):
        full_prompt = f"""
You are an expert programmer. Write correct, clean code for the following request.

Request:
{prompt}

Return ONLY the code, no explanation.
"""

        response = genai.GenerativeModel("gemini-pro-latest").generate_content(full_prompt)
        return response.text

