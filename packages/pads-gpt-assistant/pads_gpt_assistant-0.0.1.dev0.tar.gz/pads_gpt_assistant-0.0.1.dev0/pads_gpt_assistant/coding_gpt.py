#%% Setting the openai
import os
import openai
from openai import ChatCompletion
from collections import defaultdict
from typing import List, Union, Dict, Tuple
from IPython.display import Markdown
from IPython import get_ipython
from datetime import datetime
from dataclasses import dataclass
# To get the config, we need to add a current path into sys.path
import sys
from pathlib import Path
path_root = Path(__file__).parents[0]
sys.path.append(str(path_root))
from config import openai_config


wrong_code = """import numpy as np

array1 = np.array(1,2,3)
array2 = np.array([2,3,4]).reshape(-1,1)

result = np.concatenate([array1, array2])
return result"""


# #%% configuration
# from dataclasses import dataclass

# @dataclass
# class openai_config:
#     api_key:str
#     organization:str
#     language:str = 'python'
#     model:str = "gpt-3.5-turbo-0301"

#     @classmethod
#     def from_file(cls, language = 'python'):
#         assert os.path.exists('openai_config')
#         with open('openai_config') as f:
#             kwargs = {}
#             for line in f.readlines():
#                 texts = [text.strip() for text in line.split("=")]
#                 if texts[0] == 'organization':
#                     kwargs['organization'] = texts[1]
#                 elif texts[0] == 'api_key':
#                     kwargs['api_key'] = texts[1]
#         kwargs['language'] = language
#         return cls(**kwargs)




#%% class inheriting openai

class coding_assistant(ChatCompletion):
    def __init__(self, 
                 config:dataclass = None,
                 record_history:bool = False,
                 continue_conversation:bool = True,
                 ):
        super().__init__()
        if config is None:
            config = openai_config.from_file()
        self._assistant_config = config
        os.environ['OPENAI_API_KEY'] = config.api_key
        openai.organization = config.organization
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.language = config.language
        self.model = config.model
        if record_history:
            if os.path.exists('history.txt'):
                self.chat_history_file = open('history.txt', 'a')
                initial_message = f"""
************************************************************
********************* BEGIN NEW ****************************
************************************************************

Datetime: {str(datetime.now())}
=================================================

"""
                self.chat_history_file.write(initial_message)
            else:
                self.chat_history_file = open('history.txt', 'w')
        if continue_conversation:
            self.past_conversation = defaultdict(list)

    def like_it(self):
        if hasattr(self, 'past_conversation'):
            assert self._most_recent_question
            self.record_past_conversation(self._most_recent_question, self._most_recent_resp[0])
            return None
        else:
            return None
        
    def record_past_conversation(self, user_message:str, assistant_message:str):
        self.past_conversation['questions'].append(user_message)
        self.past_conversation['assistant_message'].append(assistant_message)
        return None

    def gen_past_conversation(self,
            say_good_job:bool = True)-> List[Dict]:
        
        question = self.past_conversation['questions']
        answer = self.past_conversation['assistant_message']
        
        # first check if both question and answer are the same data type
        assert len(question) == len(answer)
        default_question_dict = {'role': 'system', 'name':'user'}
        default_answer_dict = {'role': 'system', 'name':'assistant'}
        message = []
        if isinstance(question, list):
            for q, a in zip(question, answer):
                default_question_dict.update({'content':q})
                default_answer_dict.update({'content':a})
                message.append(default_question_dict.copy())
                message.append(default_answer_dict.copy())
        else:
            default_question_dict.update({'content':question})
            default_answer_dict.update({'content':answer})
            message.append(default_question_dict.copy())
            message.append(default_answer_dict.copy())

        if say_good_job:
            default_question_dict.update({'content':'Great job so far, these have been perfect'})
            message.append(default_question_dict.copy())
        
        return message


    @property
    def is_IPython(self):
        if hasattr(self, '_is_ipython'):
            pass
        else:
            try:
                if isinstance(get_ipython().config, dict):
                    if 'IPKernelApp' in get_ipython().config:
                        self._is_ipython = True
                    else:
                        self._is_ipython = False
                else:
                    self._is_ipython = False
            except:
                self._is_ipython = False
        return self._is_ipython

    @property
    def system_message(self):
        if hasattr(self, '_system_message'):
            pass
        else:
            self._system_message = self.gen_system_message()
        return self._system_message

    def gen_system_message(self, language:str = None)-> Dict:
        if language is not None:
            language = self.language
        default_message = lambda: 'You are a friendly and helpful assistant'
        system_message = defaultdict(default_message)
        system_message['role'] = 'system'
        if language:
            system_message['content'] += f' suggesting {language} codes.'
        else:
            system_message['content'] += '.'
        return dict(system_message)

    @staticmethod
    def gen_example_conversation(self,
            question:Union[List[str], str], 
            answer:Union[List[str], str], 
            say_good_job:bool = True)-> List[Dict]:
        
        # first check if both question and answer are the same data type
        if isinstance(question, list):
            assert isinstance(answer, list)
            assert len(question) == len(answer)
        elif isinstance(question, str):
            assert isinstance(answer, str)
        default_question_dict = {'role': 'system', 'name':'example_user'}
        default_answer_dict = {'role': 'system', 'name':'example_assistant'}
        message = []
        if isinstance(question, list):
            for q, a in zip(question, answer):
                default_question_dict.update({'content':q})
                default_answer_dict.update({'content':a})
                message.append(default_question_dict.copy())
                message.append(default_answer_dict.copy())
        else:
            default_question_dict.update({'content':question})
            default_answer_dict.update({'content':answer})
            message.append(default_question_dict.copy())
            message.append(default_answer_dict.copy())

        if say_good_job:
            default_question_dict.update({'content':'Great job so far, these have been perfect'})
            message.append(default_question_dict.copy())
        
        return message

    def gen_chat_kwargs(self,
            codes:str = None, 
            error_message:str = None,
            task:str = 'code_completion', 
            examples: Tuple[List[Dict]] = None,
            model:str = None,
            **kwargs
            )->List[Dict]:
        
        if model is None:
            model = self.model

        if codes is None:
            from pandas.io.clipboard import clipboard_get
            if clipboard_get() == 'clipboard_get':
                raise AttributeError("Please copy the codes into the clipboard first")
            else:
                codes = clipboard_get()


        kwarg_dict = {'model': model, 'temperature': 0}
        if len(kwargs):
            for key, val in kwargs.items():
                if key in ['max_tokens', 'temperature', 'top_p', 'n','echo']:
                    kwarg_dict.update({key:val})
                
        # step 1: get the system message (definining the characteristics of the ChatGPT)
        system_message = self.system_message
        messages = []
        messages.append(system_message)

        # step 1-2 add examples
        if examples:
            assert len(examples) == 2
            if 'say_good_job' in kwargs.keys():
                say_good_job = True
            else:
                say_good_job = False
            messages += self.gen_example_conversation(examples[0], examples[1], say_good_job = say_good_job)


        # step 1-3: add past conversations if there is any
        if hasattr(self, 'past_conversation'):
            if len(self.past_conversation):
                messages+= self.gen_past_conversation()

        # step 2: depending on the tasks, append the messages
        if task == 'code_completion':
            task_message = """
            From the following codes do the following tasks:
            if they are not incomplete, please finish the remaining codes;
            if you find any error, please inform me of any errors you may find and provide me with suggestions as well;
            Lastly, if the codes are both comprehensive and free of errors, please clarify the actual function of the codes.

            Codes: 
            """
            task_message += codes
            task_message += "\n\nPlease pay the most attention on finding and informing me of any possible errors."
            messages.append({'role':'user', 'content': task_message})

        elif task == 'qna':
            if error_message:
                task_message = f"""I received an error message from my {self.language} code which reads as follows: {args.error_message}
                
                As a result, I have a question regarding the following code that caused the error: {codes}
                """

            else:
                task_message = codes

            messages.append({'role':'user', 'content': task_message})

        elif task == 'errors': # it may require error message and the codes
            task_message = f"""
            Please find where the error is originated in the {self.language} codes provided below:

            """
            if error_message:
                task_message += f"Error Message :\n{error_message}\n\n"
            
            task_message += f"{self.language} Codes :\n{codes}"
            messages.append({'role':'user', 'content': task_message})

        kwarg_dict.update({'messages': messages})

        return kwarg_dict
    

    def get_chat_response(self,
            codes:str = None , 
            error_message: str = None,
            task:str = 'code_completion', 
            examples: Tuple[List[Dict]] = None,
            samples:int = 1,
            top_k:int = 1,
            display_markdown = True,
            **kwargs):
        

        if error_message is not None:
            if task not in ['errors','qna']:
                import logging
                logging.warning('The task will be categorized as "errors" based on the provided error message and codes.')
            task = 'errors'

        chat_kwargs = self.gen_chat_kwargs(codes, error_message, task, examples, **kwargs)
        assert top_k <= samples
        chat_kwargs.update({'n':samples})
        self._most_recent_question = chat_kwargs['messages'][-1]['content']
        resp = self.create(**chat_kwargs)
        if hasattr(self, 'chat_history_file'):
            self.chat_history_file.write(str(resp))
            self.chat_history_file.write('\n-------------------------------------------\n')
        self._most_recent_resp = [resp['choices'][i]['message']['content'] for i in range(len(resp['choices']))]
                
        if len(resp['choices']) == 1:
            resp_text = self._most_recent_resp[0]
        else:
            if top_k == 1:
                return Markdown(self._most_recent_resp[0])
            else:
                sep = """
                
                ###########################################
                ###########################################
                
                """
                resp_text = sep.join(self._most_recent_resp[:top_k])

        if self.is_IPython:
            return Markdown(resp_text)
        else:
            print(resp_text.replace('. ','.\n'))




#%% argparse
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Coding GPT')
    parser.add_argument('--user_message', default = None, required = False, type = str)
    parser.add_argument('--error_message', default = None, required = False, type = str)
    parser.add_argument('--num_result', default = 1, required = False, type = int) #
    parser.add_argument('--save_result', default = False, required = False, type = bool) #
    parser.add_argument('--language', default = 'python', required = False, type = str) #
    parser.add_argument('--only_question', default = False, required = False, type = bool) #
    args = parser.parse_args()
    if args.language != 'python':
        config = openai_config.from_file(language = args.language)
        assistant = coding_assistant(config = config, record_history = args.save_result)
    else:
        assistant = coding_assistant(record_history = args.save_result)
    
    kwargs = {}
    assert args.num_result > 0 # args.num_result must be a positive integer
    if args.num_result > 1:
        kwargs['samples'] = args.num_result
        kwargs['top_k'] = args.num_result
    if args.error_message is not None:
        kwargs['error_message'] = args.error_message
    if args.user_message is not None:
        kwargs['codes'] = args.user_message
    if args.only_question:
        kwargs['task'] = 'qna'

    if len(kwargs):
        assistant.get_chat_response(**kwargs)
    else:
        assistant.get_chat_response()

