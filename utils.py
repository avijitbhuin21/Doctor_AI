import re
import openai
import json
from dotenv import load_dotenv
import os
from mistralai import Mistral
import random


load_dotenv()
DEBUG = False

def log_debug(data):
    if DEBUG:
        print(f"DEBUG: {data}")


#PROMPTS
##############################################################################################################################################################################################################################
DIAGONOSING_PROMPT = """Based on this data if you can guess the disease then answer in this JSON format:
{"status": "success", "content": name of the disease(str)}

If you want to ask the patient question to get more context answer in this JSON format:
{"status": "pending", "content": question(str)}

Note that you can ask maximum of 5 questions.
try to ask least number of questions.
You may only ask one question at a time."""

DECIDING_PROMPT = """Based on this data You have to guess the disease and generate a mesage for the user telling him the disease and probable medications for that.
Also mention the next step the user should take.
Generate this is MARKDOWN format.
Also You Must Mention that the patient is advised to consult a doctor before taking any of those meds."""

MEDS_PROMPT = """Based on this data generate a mesage for the user telling him the disease and probable medications for that.
Also mention the next step the user should take.
Generate this is MARKDOWN format.
Also You Must Mention that the patient is advised to consult a doctor before taking any of those meds."""


##############################################################################################################################################################################################################################
class LLM:
    def extract_query(self, text: str) -> str:
        pattern = r"```(.*?)```"
        matches = re.findall(pattern, text, re.DOTALL)
        return matches[0] if matches else text

    def ask_llama(self, query, api_key = random.choice(os.getenv('Sambanova_Api_Key').split()), model = "Meta-Llama-3.1-405B-Instruct", JSON = False):
        for i in range(5):
            SambaNova_Client = openai.OpenAI(
                    api_key=api_key,
                    base_url="https://api.sambanova.ai/v1",
                )
            response = SambaNova_Client.chat.completions.create(
                model=model,
                messages=[{"role":"system","content": "You're a Doctor-AI with 20 years of experience."},{"role":"user","content":query}],
                temperature =  0.1,
                top_p = 0.1,
            )
            ans = response.choices[0].message.content
            if not JSON:
                return ans
            try:
                data = json.loads(self.extract_query(ans))
                return data
            except Exception as e:
                print(e)
                print(response.choices[0].message.content)

    def ask_Mistral(self, question, sys="You're a Doctor-AI with 20 years of experience.", JSON= False, model = "mistral-large-2407"):
        try:
            self.Mistral_Client = Mistral(
                    api_key=random.choice(os.getenv('Mistral_Api_Key').split()),
                )
            for i in range(10):
                try:
                    if JSON:
                        response = self.Mistral_Client.chat.complete(
                        model=model,
                        messages=[{"role":"system","content":sys},{"role":"user","content":question}],
                        temperature =  0.1,
                        top_p = 0.1,
                        response_format = {
                                "type": "json_object",
                            }
                    )
                        return json.loads(response.choices[0].message.content)
                    else:
                        response = self.Mistral_Client.chat.complete(
                        model=model,
                        messages=[{"role":"system","content":sys},{"role":"user","content":question}],
                        temperature =  0.1,
                        top_p = 0.1
                    )
                        return response.choices[0].message.content
                    
                except Exception as e:
                    print(e)
                    print(response.choices[0].message.content)

        except Exception as e:
            print(e)

class Helper:
    def __init__(self):
        self.llm = LLM()

    def get_prompt(self, patient_data, conversation):
        base_prompt = """This is the patient Profile:\n"""
        for i in patient_data:
            if patient_data[i] != '':
                base_prompt += f'''{i}: {patient_data[i]}\n'''

        formatted_conversation = "Chat History:\n"
        question_count = 0

        for i, message in enumerate(conversation):
            if message['role'] == 'assistant':
                question_count += 1
                formatted_conversation += f"Assistant: {message['content']}\n"
                if i + 1 < len(conversation) and conversation[i + 1]['role'] == 'user':
                    formatted_conversation += f"User: {conversation[i + 1]['content']}\n\n"
                else:
                    formatted_conversation += "\n"
            elif message['role'] == 'assistant' and (i == 0 or conversation[i - 1]['role'] != 'user'):
                formatted_conversation += f"Assistant: {message['content']}\n\n"
        if question_count == 0:
            temp = ''
        if question_count == 1:
            temp = f"This is your 1st question."
        if question_count == 2:
            temp = f"This is your 2nd question."
        if question_count == 3:
            temp = f"This is your 3rd question."
        if question_count > 3:
            temp = f"this is your {question_count}th question."

        main = formatted_conversation + "\n" + temp
        if conversation == []:
            return (base_prompt, None, question_count)
        else:
            return (base_prompt, main, question_count)
    
    def ask_doctor(self, patient_data, conversation):
        patient_profile, history, question_count = self.get_prompt(patient_data= patient_data, conversation= conversation)

        if history == None:
            prompt = patient_profile + "\n" + DIAGONOSING_PROMPT + "\n" + 'Also Greet the user first then ask the question, as this is the start of our conversation with the patient.'
            log_debug(prompt)
            ai_ans = self.llm.ask_Mistral(question= prompt, JSON= True)
        else:
            if question_count > 6:
                prompt = patient_profile + "\n" + history + "\n" + DECIDING_PROMPT
                log_debug(prompt)
                return self.llm.ask_llama(query= prompt, JSON= False)

            else:
                prompt = patient_profile + "\n" + history + "\n" + DIAGONOSING_PROMPT
                log_debug(prompt)
                ai_ans = self.llm.ask_Mistral(question= prompt, JSON= True)

        if ai_ans['status'] == 'success':
            prompt = patient_profile + "\n" + history + "\n" + f"The Most Probable Disease is: {ai_ans['content']}" + "\n" + MEDS_PROMPT
            log_debug(prompt)
            return self.llm.ask_llama(query= prompt, JSON= False)
        
        log_debug(ai_ans)
        return ai_ans['content']






        
            
        