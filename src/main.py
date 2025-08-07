from crew import CriadorBlog
from dotenv import load_dotenv
import os

#Carrega a API_KEY da openai no arquivo .env
load_dotenv()
os.environ["OPENAI_API_KEY"]

criador_blog = CriadorBlog()

def run_criador_artigo(pergunta):
    artigo = criador_blog.gerar_artigo(pergunta)
    return artigo
