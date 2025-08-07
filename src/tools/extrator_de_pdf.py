from crewai.tools import BaseTool
import PyPDF2
import os

class ExtratorDeTexto(BaseTool):
    name: str = "Extrator de texto"
    description: str = (
        "Funcao que extrai o texto do arquivo pdf e o transforma em texto que pode ser manipulado."
    )

    def _run(self):
        texto = ""

        pdf_dir = os.path.join(os.getcwd(), "../pdf_path")

        if not os.listdir(pdf_dir):
            return "ERRO: A pasta pdf_path nao existe"

        try:
            caminho_arquivo = [os.path.join(pdf_dir, caminho) for caminho in os.listdir(pdf_dir)]
            for arquivo in caminho_arquivo:
                with open(arquivo,"rb") as arquivo:
                    leitor_pdf = PyPDF2.PdfReader(arquivo)
                    for pagina in leitor_pdf.pages:
                        texto += pagina.extract_text()

        except Exception as e:
            texto += f"Erro ao processar arquivo: {e}"

        return texto