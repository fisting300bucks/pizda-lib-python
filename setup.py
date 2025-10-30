from setuptools import setup

setup(
    name='pizda',                        # имя пакета (будет использоваться при импорте)
    version='1.0.0',                     # версия
    py_modules=['pizda'],                # имя файла без .py
    description='Полярно-комплексная математика',  # краткое описание
    author='fisting300bucks',
    author_email='example@example.com',  # (можно убрать)
    url='https://github.com/fisting300bucks/pizda-lib-python',
    install_requires=['numpy', 'matplotlib'],       # зависимости
)
