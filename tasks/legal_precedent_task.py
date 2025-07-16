# legal_precedent_task.py

from crewai import Task
from agents.legal_precedent_agent import legal_precedent_agent
from tasks.case_intaker_task import case_intaker_task
from tasks.section_retriever_task import section_retrieval_task

legal_precedent_task = Task(
    agent=legal_precedent_agent,
    context=[case_intaker_task, section_retrieval_task],
    description=(
        "You are provided with structured context describing the user's legal issue, including key facts and applicable statutory sections.\n\n"
        "Based on this, search for **relevant precedent judgments from trusted Indian legal sources** (such as indiankanoon.org).\n\n"
        "Use your tool to retrieve up to 3 landmark or highly relevant case summaries. Then, write a single, well-structured paragraph that:\n"
        "- Mentions the case titles\n"
        "- Summarizes each ruling briefly\n"
        "- Explains how these rulings support or relate to the current legal issue"
    ),
    expected_output=(
        """
        A cohesive paragraph that summarizes up to 3 relevant Indian precedent cases, explaining their legal context and relevance to the user's issue, based on the case summary and retrieved law sections.
        """
    )
)