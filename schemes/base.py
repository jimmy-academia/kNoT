import ast
import openai
import logging
from collections import defaultdict
from utils import readf, user_struct, system_struct, dumpj
from debug import *

class BaseScheme(object):
    def __init__(self, args, task_loader):
        super(BaseScheme, self).__init__()
        self.args = args
        self.task_loader = task_loader
        if 'gpt' in self.args.planner_llm or 'gpt' in self.args.worker_llm:
            self.check_openai_api()

        self.prep_const_prompt()
        self.system_servent = "You follow orders strictly. Output the answer without any additional information."

    def check_openai_api(self):
        self.client = openai.OpenAI(api_key=readf('.openaiapi_key'))
    
    def operate(self):
        results = defaultdict(list)
        results['accuracy'] = 0
        correct = total = 0
        for row in self.task_loader:

            if self.args.task == 'intersection':
                set1, set2, answer = row
                query = f"Set1 is {set1}. Set2 is {set2}."
            else:
                query, answer = row

            output = self.solve_query(query)

            if self.args.task == 'arithmetic':
                answer = float(answer)
                output = float(output)
            elif self.args.task == 'review':
                query = ast.literal_eval(query)
            
            results['output'].append(output)
            results['answer'].append(answer)
            correct += int(output == answer)
            total += 1
            results['accuracy'] = correct/total
            dumpj(results, self.args.record_path)

        results['info'] = f"Correct: {correct}/Total: {total}"
        dumpj(results, self.args.record_path)

    def llm_answer(self, prompt, planner=False):
        model = self.args.planner_llm if planner else self.args.worker_llm
        if 'gpt' in model:
            message = [system_struct(self.system_servent), user_struct(prompt)]
            logging.info(" <<<< input prompt")
            logging.info(message)
            response = self.client.chat.completions.create(
                        model = model,
                        messages = message,
                        temperature = 0,
                    )
            response = response.choices[0].message.content
            logging.info(" >>>> \n" + response)
        else:
            print('llama!')

        return response
