# legal_precedent_agent.py

from crewai import Agent, LLM
from tools.legal_precedent_search_tool import search_legal_precedents

llm = LLM(
    model="gemini/gemini-1.5-pro",
    temperature=0.3,
)

legal_precedent_agent = Agent(
    role="Legal Precedent Research Agent",
    goal="Retrieve and summarize precedent judgments relevant to the user's legal issue, supporting the case with real-world judicial reasoning.",
    backstory=(
        "You are a highly experienced legal researcher who specializes in Indian case law. "
        "You are skilled at identifying key precedent judgments that align with the facts and legal domains of a case. "
        "You search only trusted legal databases and provide summaries that strengthen the legal argument using past court rulings."
    ),
    tools=[search_legal_precedents],
    llm=llm,
    verbose=True,
)
