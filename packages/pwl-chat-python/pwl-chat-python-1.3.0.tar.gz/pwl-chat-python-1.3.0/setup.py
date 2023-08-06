from setuptools import setup

setup(
    name='pwl-chat-python',
    version='1.3.0',
    description='摸鱼派聊天室python客户端',
    author='gakkiyomi',
    author_email='gakkiyomi@gmail.com',
    url='https://github.com/gakkiyomi/pwl-chat-python',
    packages=['src'],
    install_requires=[
        'rel',
        'requests',
        'websocket_client',
        'schedule',
        'click'
    ],
    python_requires='>=3.10.8',
)
