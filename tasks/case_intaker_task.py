from crewai import Task
from agents.case_intaker import case_intaker

case_intaker_task = Task(
    agent = case_intaker,

    description = (
        '''
        You are given a user's legal concern expressed in plain English:

        {user_input}

        Your task is to analyze the query, extract the core legal issue, classify the legal domain
        (such as Criminal, Civil, Labor, Family, Property, or Corporate), and organize the response in a structured JSON format.

        Your output must include:
        - `case_type`: a short label for the legal issue (e.g., Breach of Contract, Theft, Harassment)
        - `legal_domain`: the broader category of law
        - `summary`: 1–2 sentence explanation of the situation
        - `relevant_entities`: key actors (e.g., user, employer, landlord, police)
        '''
    ),

    expected_output = (
        '''
        Format your response as:
        ```json
        {
            "case_type": "Wrongful Termination",
            "legal_domain": "Labor Law",
            "summary": "The user was terminated after refusing to work unpaid overtime beyond legal limits.",
            "relevant_entities": ["user", "employer"]
        }
        ```
        '''
    )
)