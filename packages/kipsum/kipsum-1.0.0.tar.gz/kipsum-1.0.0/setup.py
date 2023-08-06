# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kipsum']

package_data = \
{'': ['*'], 'kipsum': ['sources/*']}

setup_kwargs = {
    'name': 'kipsum',
    'version': '1.0.0',
    'description': 'Korean lorem ipsum generator',
    'long_description': "# kipsum\n\nkipsum은 python 코드로 작성된 한글판 lorem ipsum 생성기입니다.\n\n## Installation\n\n```shell\npip install kipsum\n```\n\n## Usage\n\nkipsum은 기본적으로 `Kipsum` 클래스의 인스턴스를 생성하여 사용이 가능합니다.\n\n```python\nimport kipsum\n\nkip = kipsum.Kipsum()\n\n# shortcut\nkip.sentence(6)\n>>> '더운지라 가진 사랑의 밥을 두손을 있는가?'\n\nkip.sentences(3)\n>>> ['찬미를 살 인생의 있는 노년에게서 약동하다.',\n      '얼음 새가 내려온 하였으며, 생의 보라.',\n      '품었기 노년에게서 심장의 보는 때에, 힘있다.']\n\nkip.sentences(3, sep='$')\n>>> '물방아 크고 하여도 목숨을 더운지라 이상!$인도하겠다는 못할 못할 소금이라 곳이 부패뿐이다.$놀이 커다란 설산에서 이것이야말로 거친 아름다우냐?'\n\nkip.paragraph(3)\n>>> '모래뿐일 피어나기 날카로우나 보는 생생하며, 말이다. 따뜻한 기쁘며, 그와 고행을 설레는 힘있다. 동력은 사랑의 없으면 꽃 낙원을 그리하였는가?'\n\nkip.paragraphs(3)\n>>> ['몸이 능히 놀이 인류의 속잎나고, 황금시대다. 크고 방황하여도, 만물은 가진 능히 부패뿐이다. 그것을 관현악이며, 투명하되 피는 위하여 끓는다.',\n      '그림자는 긴지라 살 보배를 앞이 힘있다. 착목한는 있는 하여도 찾아다녀도, 바이며, 피다. 것이 청춘은 길을 원대하고, 풀이 운다.',\n      '천지는 발휘하기 너의 착목한는 이것을 쓸쓸하랴? 따뜻한 긴지라 거친 작고 찾아다녀도, 사막이다. 구할 못하다 끝에 피에 심장은 있는가?']\n```\n\n클래스 인스턴스를 생성하지 않고 shortcut을 이용하는 방법도 있습니다. 매개변수는 동일합니다.\n\n```python\nimport kipsum\n\nkipsum.sentence(6)\n>>> '더운지라 가진 사랑의 밥을 두손을 있는가?'\n\nkipsum.sentences(3)\n>>> ['찬미를 살 인생의 있는 노년에게서 약동하다.',\n     '얼음 새가 내려온 하였으며, 생의 보라.',\n     '품었기 노년에게서 심장의 보는 때에, 힘있다.']\n\nkipsum.paragraph(3)\n>>> '모래뿐일 피어나기 날카로우나 보는 생생하며, 말이다. 따뜻한 기쁘며, 그와 고행을 설레는 힘있다. 동력은 사랑의 없으면 꽃 낙원을 그리하였는가?'\n\nkipsum.paragraphs(3)\n>>> ['몸이 능히 놀이 인류의 속잎나고, 황금시대다. 크고 방황하여도, 만물은 가진 능히 부패뿐이다. 그것을 관현악이며, 투명하되 피는 위하여 끓는다.',\n     '그림자는 긴지라 살 보배를 앞이 힘있다. 착목한는 있는 하여도 찾아다녀도, 바이며, 피다. 것이 청춘은 길을 원대하고, 풀이 운다.',\n     '천지는 발휘하기 너의 착목한는 이것을 쓸쓸하랴? 따뜻한 긴지라 거친 작고 찾아다녀도, 사막이다. 구할 못하다 끝에 피에 심장은 있는가?']\n```\n\n## Methods\n\n### sentence(nb_words: int = 6)\n문장 하나를 생성합니다. 문장 내에서 사용되는 단어의 개수는 `nb_words`로 결정됩니다.\n\n### sentences(nb: int = 3, sep: str = None)\n\n문장 여러개를 생성합니다. 문장의 수는 `nb`에 의해 결정됩니다.\n\n`sep` 값이 주어지지 않았다면 리스트 형태로 반환됩니다. 값이 주어진다면 해당 값으로 문장을 `join` 한 결과를 반환합니다.\n\n\n### paragraph(nb_sentences: int = 3)\n문단 하나를 생성합니다. 문단 내의 문장 개수는 `nb_sentences`로 결정됩니다.\n\n### paragraphs(nb: int = 3, sep: str = None)\n문단 여러개를 생성합니다. 문단의 개수는 `nb`로 결정됩니다.\n\n`sep` 값이 주어지지 않았다면 리스트 형태로 반환됩니다. 값이 주어진다면 해당 값으로 문장을 `join` 한 결과를 반환합니다.\n",
    'author': 'jrog612',
    'author_email': 'wnrhd114@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jrog612/kipsum',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
