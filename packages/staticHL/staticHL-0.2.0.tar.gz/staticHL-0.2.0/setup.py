from setuptools import setup

setup(
    name='staticHL',
    description='Convert dynamically styled code and syntax highlighting to static html+css.',
    url='https://gitlab.com/jackaaron/statichl/',
    version='0.2.0',
    license='MIT',
    packages=['statichl'],
    install_requires=[
        "async-generator==1.10",
        "attrs==23.1.0",
        "certifi==2022.12.7",
        "exceptiongroup==1.1.1",
        "h11==0.14.0",
        "idna==3.4",
        "lxml==4.9.2",
        "networkx==3.1",
        "outcome==1.2.0",
        "progress==1.6",
        "PySocks==1.7.1",
        "selenium==4.9.0",
        "sniffio==1.3.0",
        "sortedcontainers==2.4.0",
        "trio==0.22.0",
        "trio-websocket==0.10.2",
        "urllib3==1.26.15",
        "wsproto==1.2.0"
    ],
    entry_points={
        "console_scripts": [
            "statichl = statichl.__main__:main"
        ]
    }
)
