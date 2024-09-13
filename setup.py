from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='santhosh',
    author_email='santhoshkaruppusamy55@gmail.com',
    install_requires=["openai","groq","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)