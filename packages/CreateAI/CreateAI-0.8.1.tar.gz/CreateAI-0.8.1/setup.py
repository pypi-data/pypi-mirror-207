import setuptools
with open(r'C:\MyUse\code\python\EasyPack\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='CreateAI',
	version='0.8.1',
	author='R0fael',
	author_email='roslobodchikov@gmail.com',
	description='Easy tool for creating AI in python',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/R0fael/CreateAI',
	packages=['CreateAI'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)