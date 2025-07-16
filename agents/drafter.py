from crewai import Agent, LLM

llm = LLM(
    model="gemini/gemini-1.5-pro",
    temperature=0.3,
)

legal_drafter_agent = Agent(
    role="Legal Document Drafting Agent",
    goal="Draft well-structured, legally sound documents using the user's case summary, relevant statutory sections, and supporting precedents.",
    backstory=(
        "You are a seasoned legal drafting specialist with deep knowledge of Indian legal procedures and formal documentation. "
        "You prepare professional legal documents such as complaints, FIRs, and legal notices. "
        "Your drafts are context-aware, structured, and written in clear, formal legal language compliant with Indian law."
    ),
    tools=[],  # All inputs come from prior agents
    llm=llm,
    verbose=True,
)
