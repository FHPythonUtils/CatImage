"""Do setup for uploading to pypi
"""
import setuptools

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="catimage",
	version="2020.4",
	author="FredHappyface",
	description="Use to cat an image to the terminal",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/FredHappyface/Python.CatImage",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	entry_points={
		'console_scripts': [
			'catimage=catimage.catimage:cli',
		],
	},
	package_data={
		'catimage': ['program_icon.png'],
	},
	python_requires='>=3.0',
)
