from setuptools import setup, find_packages

with open('requirements.txt') as f:
	requirements = f.readlines()

long_description = 'Sample Package made for a demo \
	of its making for the GeeksforGeeks Article.'

setup(
		name ='deep-clone-gfg-test',
		version ='1.0.0',
		author ='rajan gupta',
		author_email ='96rajangupta@gmail.com',
		url ='https://github.com/rajan-personal/deep-clone-gfg-test',
		description ='Demo Package for GfG Article.',
		long_description = long_description,
		long_description_content_type ="text/markdown",
		license ='MIT',
		packages = find_packages(),
		entry_points ={
			'console_scripts': [
				'gfg = gfg.gfg:main'
			]
		},
		classifiers =(
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		),
		keywords ='geeksforgeeks gfg article python package',
		install_requires = requirements,
		zip_safe = False
)
