from setuptools import setup, find_packages

setup(
    name='my_module_goto95',
    version='1.0',
    author='GoTo95',
    author_email='uraprudnikov@yandex.ru',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
        # и так далее
    ],
)
