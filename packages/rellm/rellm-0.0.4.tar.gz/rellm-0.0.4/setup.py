# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rellm']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.3,<2.0.0',
 'regex>=2023.5.5,<2024.0.0',
 'torch>=2.0.0,<3.0.0',
 'transformers>=4.28.1,<5.0.0']

setup_kwargs = {
    'name': 'rellm',
    'version': '0.0.4',
    'description': 'Get exact structure out of any language models with regular expressions.',
    'long_description': '# ReLLM\nRegular Expressions for Language Model Completions.\n\n> *Some people, when confronted with a problem, think\n“I know, I\'ll use regular expressions.”   Now they have two problems.*\n\nExact structure out of any language model completion with regular expressions.\n\nReturn specific syntactic structure (e.g. JSON or XML), or specific semantic structure (e.g. a date or a number), or even complete templates (e.g. a sentence with a blank to fill in).\n\nHow does it work? ReLLM filters non-matching tokens pre-generation. For each token, ReLLM tests every possible completion against a partial regex. For the potential completions that do not match the pattern, ReLLM masks the logits so that the language model does not generate them.\n\n### Installation\n```\npip install rellm\n```\n\nThe preliminary results are interesting -- even for small models, constraining the token space with ReLLM can improve the quality of the completions. Not to mention the ability to more easily parse the output programmatically. Take a look at some of the examples below (you can run them with [example.py](example.py))\n\n```python\nimport regex\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nfrom rellm import complete_re\n\nmodel = AutoModelForCausalLM.from_pretrained("gpt2")\ntokenizer = AutoTokenizer.from_pretrained("gpt2")\n\nprompt = "ReLLM, the best way to get structured data out of LLMs, is an acronym for "\npattern = regex.compile(r\'Re[a-z]+ L[a-z]+ L[a-z]+ M[a-z]+\')\noutput = complete_re(tokenizer=tokenizer, \n                     model=model, \n                     prompt=prompt,\n                     pattern=pattern,\n                     do_sample=True,\n                     max_new_tokens=80)\nprint(output)\n```\n\n```\n> Realized Logistic Logistics Model\n```\n\n\n## Examples using GPT2 (124 million parameters)\n\n#\n\nUsing GPT2 (124m)\n\n**Prompt**: ReLLM, the best way to get structured data out of LLMs, is an acronym for\n\n**Pattern**: Re[a-z]+ L[a-z]+ L[a-z]+ M[a-z]+\n\n**ReLLM**: Realized Logistic Logistics Model\n\n**Without ReLLM**: Largest Largest Address Space (MELSP), which has its roots in the  Internet network, at least when compared\n#\n\n**Prompt**: Return the first three letters of the alphabet in a json array:\n\n**Pattern** \\[\\"[a-z]\\", \\"[a-z]\\", \\"[a-z]\\"\\]\n\n**ReLLM**: ["a", "b", "c"]\n\n**Without ReLLM**: { "index": 0, "id":"1", "description":"", "text": "[{ "id": 0, "name":\n#\n**Prompt**: Fill in the sentence with an interesting story about the dentist:\n\n**Pattern**: Today I\\\'m going to the [a-z]+ to [a-z]+ because ([a-z]+ )*\\.\n\n**ReLLM**: Today I\'m going to the dentist to see because it is a very important day for me\n\n**Without ReLLM**: \'My family bought me an appointment with a dentist when I was 15. The dentist gave me one a year and then I was told on\n#\n\n**Prompt**: Is this a good demo?\n\n**Pattern**: (Yes|No)\n\n**ReLLM**: No.\n\n**Without ReLLM**: I don\'t know, but this is amazing! Even more amazing is how the design can take place on a small stage that uses LEDs.\nAs\n\n#\n\n**Prompt**: Convert the date May 4, 2023 to the format mm/dd/yyyy:\n\n**Pattern**: [0-9]{2}/[0-9]{2}/[0-9]{4}\n\n**ReLLM**: 00/00/0045\n\n**Without ReLLM**:  mm:ss\n\nA-Z, Z-A, W-H (0-9:9:19)\n\nZ-R\n\n#\n\n**Prompt**: Jeff Dean is a\n\n**Pattern** (Programmer|Computer Scientist|AGI)\n\n**ReLLM**: Computer Scientist\n\n**Without ReLLM**: former national basketball champion and a former professional basketball player. He currently serves as general counsel for the NCAA Office of the Vice President for Academic Affairs.\n\n#\n\n**Prompt**: I can eat \n\n**Pattern**: [0-9]{1,10} [a-z]* of [a-z]*\n\n**ReLLM**: 800 calories of coffee\n\n**Without ReLLM**: iced coffee here on the west side and do this, so can you?"\n\n"Why, I don\'t understand. What did you mean by',
    'author': 'Matt Rickard',
    'author_email': 'pypi@matt-rickard.com',
    'maintainer': 'Matt Rickard',
    'maintainer_email': 'pypi@matt-rickard.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
