from setuptools import setup, find_packages

setup(
	name='Tomaatti for i3',
	version='0.1',
	description='Pomodoro timer with i3 integration',
	long_description='Pomodoro timer with i3 integration',
	url='https://github.com/thuetz/i3-tomaatti',
	author='Tim Hütz',
	author_email='tim@huetz.biz',
	license='GPLv3',
	packages=find_packages(),
	install_requires=[],
	zip_safe=False,
	platforms=['linux']
)
