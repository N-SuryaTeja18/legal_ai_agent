# crew.py

from crewai import Crew

from agents.case_intaker import case_intaker
from agents.section_retrieval import section_retrieval_agent
from agents.legal_precedent_agent import legal_precedent_agent
from agents.drafter import legal_drafter_agent
from tasks.case_intaker_task import case_intaker_task
from tasks.section_retriever_task import section_retrieval_task
from tasks.legal_precedent_task import legal_precedent_task
from tasks.drafter_task import legal_drafter_task


legal_assistant_crew = Crew(
    agents=[case_intaker, section_retrieval_agent, legal_precedent_agent, legal_drafter_agent],
    tasks=[case_intaker_task, section_retrieval_task, legal_precedent_task, legal_drafter_task],
    verbose=True
)