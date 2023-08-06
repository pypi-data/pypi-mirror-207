import setuptools


install_requires = [
    'pyqt5'
]
setuptools.setup(
	name="pysbapi", 
	version="0.0.1",
	author="TechFree AdamKim",
	author_email="4_2@naver.com",
	description="sbapi test package",
	packages=setuptools.find_packages(),
    install_requires=install_requires
)
	