from crew import CriadorBlog
from dotenv import load_dotenv
import os

#Carrega a API_KEY da openai no arquivo .env
load_dotenv()
os.environ["OPENAI_API_KEY"]


CriadorBlog().crew().kickoff()