# section_retrieval_task.py

from crewai import Task
from agents.section_retrieval import section_retrieval_agent
from tasks.case_intaker_task import case_intaker_task

section_retrieval_task = Task(
    agent=section_retrieval_agent,
    context=[case_intaker_task],
    description=(
        "You are provided with a structured summary of the user's legal issue, generated by the previous task.\n\n"
        "Your task is to identify and retrieve the most relevant legal sections from Indian laws — including IPC, CrPC, CPC, IEA, MVA, etc. — that apply to the situation.\n\n"
        "Use the tool named **Sections Search Tool** to search the vector database. The tool will return 5 candidate sections using Maximal Marginal Relevance (MMR). You must evaluate and select the **top 3 most relevant sections** from this list.\n\n"
        "Each result must include:\n"
        "- `act`: The full name of the Act\n"
        "- `chapter`: Chapter number (Only if available)\n"
        "- `section`: Section number\n"
        "- `section_title`: Title of the section\n"
        "- `section_desc`: Full text or explanation of the section"
    ),
    expected_output=(
        """
        ```json
        [
        {
            "act": "Indian Penal Code, 1860",
            "chapter": 6,
            "section": 73,
            "section_title": "Compensation for breach of contract",
            "section_desc": "When a contract has been broken..."
        },
        {
            "act": "Indian Evidence Act, 1872",
            "chapter": 8,
            "section": 114,
            "section_title": "Presumptions as to certain facts",
            "section_desc": "The Court may presume the existence of any fact..."
        },
        {
            "act": "Code of Criminal Procedure, 1973",
            "chapter": 12,
            "section": 154,
            "section_title": "Information in cognizable cases",
            "section_desc": "Every information relating to the commission of a cognizable offence..."
        }
        ]
        ```
        """
    )
)
