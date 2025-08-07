from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools.extrator_de_pdf import ExtratorDeTexto


#LLM do GPT
llm = LLM(
    model="openai/gpt-4",
)

@CrewBase
class CriadorBlog:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    #Agente Leitor de pdf
    @agent
    def agente_leitor_pdf(self) -> Agent:
        return Agent(
            config=self.agents_config["agente_leitor_pdf"],
            tools=[ExtratorDeTexto()],
            verbose=True,
            
        )
    
    #Agente que analiza o conteudo colhido
    @agent
    def agente_analista(self) -> Agent:
        return Agent(
            config=self.agents_config["agente_analista"],
            verbose=True,
            llm=llm,
        )

    #Agente que resume o conteudo analizado
    @agent
    def agente_resumo(self) -> Agent:
        return Agent(
            config=self.agents_config["agente_resumo"],
            verbose=True,
            llm=llm,
        )
    
    #Agente que transforma o resumo em artigo
    @agent
    def agente_artigo(self) -> Agent:
        return Agent(
            config=self.agents_config["agente_artigo"],
            verbose=True,
            llm=llm,
        )
    

    #Task de ler os pdfs
    @task
    def task_ler_pdf(self) -> Task:
        return Task(
            config=self.tasks_config["task_ler_pdf"],
        )
    
    #Task de analizar o texto colhido
    @task
    def task_analizar_texto(self) -> Task:
        return Task(
            config=self.tasks_config["task_analizar_texto"],
            context=[self.task_ler_pdf()],
        )
    
    #Task de resumir o texto analizado
    @task
    def task_resumir_texto(self) -> Task:
        return Task(
            config=self.tasks_config["task_resumir_texto"],
            context=[self.task_analizar_texto()],
        )
    
    #Task de formatar o resumo em artigo
    @task
    def task_formatar_artigo(self) -> Task:
        return Task(
            config=self.tasks_config["task_formatar_artigo"],
            context=[self.task_resumir_texto()],
            output_file="artigo.pdf"
        )
    


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            process=Process.sequential,
        )