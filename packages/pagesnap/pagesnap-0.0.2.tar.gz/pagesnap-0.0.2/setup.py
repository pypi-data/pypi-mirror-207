# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pagesnap']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.12.2,<5.0.0', 'playwright>=1.33.0,<2.0.0']

entry_points = \
{'console_scripts': ['pagesnap = pagesnap.pagesnap:main']}

setup_kwargs = {
    'name': 'pagesnap',
    'version': '0.0.2',
    'description': 'Saving webpage in a single HTML file, based on playwright',
    'long_description': '# PageSnap\n\n[中文文档](./README_zh.md)\n\nPageSnap is a tool that allows you to save web pages offline as single-page HTML files, preserving the original appearance of the web page as much as possible. It is developed using Python and Playwright, which means it can also save dynamic JavaScript web pages offline.\n\nThe advantage of using single-page HTML format is that users can conveniently open and browse the files with any W3C-compliant browser.\n\nAs a Python library, PageSnap can be easily added as a dependency to other projects. If your project uses Python and Playwright, simply import the PageSnap library to add offline-saving capabilities to your pages.\n\nNote: Currently, this project is still in the early stages of feature development and cannot be directly used as a library. The related APIs are still under development. You can keep an eye on the progress, or feel free to clone the project to try it out and share your thoughts.\n\n## As a Library\n\nPageSnap provides an asyncio-based API. In your Playwright project, you can complete the offline saving of a page in just two steps. Here\'s an example code:\n\n```python\n# Step1: Hook page to intercept requests and save resources\n#        note: you can also hook after goto, but you may miss some resources\nawait hook_page(page) \n\n# Develop your code, doing your actions\nawait page.goto(url)\n# It\'s better to wait for the page to be fully loaded\nawait page.wait_for_load_state("networkidle")\n\n# Step2: Get the page content\nembedded_html = await page_snap(page)\n\n# Then you can save it to a file\nwith open(output_filename, \'w\', encoding=\'utf-8\') as f:\n    f.write(embedded_html)\n```\n\n## As a Command Line\n\nUse the following pip command to install:\n\n```\npip install pagesnap\n```\n\nInitialize Playwright:\n\n```\nplaywright install\n```\n\nStart using:\n\n```\npagesnap https://example.com/ test.html\n```\n\n## Discussion\n\nIf you have any suggestions or improvements, please feel free to submit an issue or pull request. If you like this project, please give it a star.\n\nI am usually active on [Sina Weibo](https://www.weibo.com/u/1240212845) and welcome technical discussions there as well.',
    'author': 'maxiee',
    'author_email': 'maxieewong@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/maxiee/pagesnap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
