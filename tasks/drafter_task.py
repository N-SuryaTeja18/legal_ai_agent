# drafter_task.py

from crewai import Task
from agents.drafter import legal_drafter_agent
from tasks.case_intaker_task import case_intaker_task
from tasks.section_retriever_task import section_retrieval_task
from tasks.legal_precedent_task import legal_precedent_task

legal_drafter_task = Task(
    agent=legal_drafter_agent,
    context=[case_intaker_task, section_retrieval_task, legal_precedent_task],
    description=(
        "You are provided with a structured case summary, relevant Indian legal sections (from IPC, CrPC, CPC, etc.), and supporting precedent case summaries.\n\n"
        "Your task is to draft a formal legal document—such as a complaint, FIR, or legal notice—based on this context.\n\n"
        "The document must be written in formal legal language, formatted professionally, and should follow the Indian legal framework. "
        "It should be suitable for submission to legal authorities, employers, courts, or any concerned party."
    ),
    expected_output=(
        """
        A formal legal document with the following structure:
        - **Title** (e.g., LEGAL COMPLAINT or LEGAL NOTICE)
        - **Date**
        - **To** (Respondent / Opposing party)
        - **From** (Complainant / User)
        - **Subject** (Brief title of the issue)
        - **Factual Summary** (Chronological and legally relevant events)
        - **Applicable Legal Sections** (Clearly cited)
        - **Relevant Precedents** (If applicable, summarized briefly)
        - **Formal Request or Legal Demand** (What the sender expects)
        - **Closing** (Signature, contact details, etc.)
        """
    )
)