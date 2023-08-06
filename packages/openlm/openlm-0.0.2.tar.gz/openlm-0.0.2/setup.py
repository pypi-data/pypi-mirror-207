# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openlm', 'openlm.llm']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.30.0,<3.0.0']

setup_kwargs = {
    'name': 'openlm',
    'version': '0.0.2',
    'description': 'Drop-in OpenAI-compatible that can call LLMs from other providers',
    'long_description': '# OpenLM\n\nDrop-in OpenAI-compatible library that can call LLMs from other providers (e.g., HuggingFace, Cohere, and more). \n\n```diff\n1c1\n< import openai\n---\n> import openlm as openai\n\ncompletion = openai.Completion.create(\n    model=["bloom-560m", "cohere.ai/command"], \n    prompt=["Hello world", "second prompt and then"]\n)\nprint(completion)\n```\n### Features\n* Takes in the same parameters as OpenAI\'s Completion API and returns a similarly structured response. \n* Call models from HuggingFace\'s inference endpoint API, Cohere.ai, OpenAI, or your custom implementation. \n* Complete multiple prompts on multiple models in the same request. \n* Very small footprint: OpenLM calls the inference APIs directly rather than using multiple SDKs.\n\n\n### Installation\n```bash\npip install openlm\n```\n\n### Examples\n\n- [Import as OpenAI](examples/as_openai.py)\n- [Set up API keys via environment variables or pass a dict](examples/api_keys.py)\n- [Add a custom model or provider](examples/custom_provider.py)\n- [Complete multiple prompts on multiple models](examples/multiplex.py)\n\nOpenLM currently supports the Completion endpoint, but over time will support more standardized endpoints that make sense. \n\n### Other Languages\n[r2d4/llm.ts](https://github.com/r2d4/llm.ts) is a TypeScript library that has a similar API that sits on top of multiple language models.\n\n### Roadmap\n- [ ] Streaming API\n- [ ] Embeddings API\n\n### Contributing\nContributions are welcome! Please open an issue or submit a PR.\n\n### License\n[MIT](LICENSE)\n\n',
    'author': 'Matt Rickard',
    'author_email': 'pypi@matt-rickard.com',
    'maintainer': 'Matt Rickard',
    'maintainer_email': 'pypi@matt-rickard.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
