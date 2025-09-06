from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.tools import Tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from langchain_core.messages.human import HumanMessage
from langchain_core.messages.system import SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):
    
    llm = ChatGroq(model=llm_id)

    if allow_search:
        # Create the search tool manually
        search = GoogleSerperAPIWrapper()
        search_tool = Tool(
            name="Search",
            func=search.run,
            description="Useful for when you need to answer questions about current events"
        )
        tools = [search_tool]
    else:
        tools = []

    # Create agent without state_modifier parameter
    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Prepare messages with system prompt
    messages = []
    
    # Add system prompt if provided
    if system_prompt:
        messages.append(SystemMessage(content=system_prompt))
    
    # Add user messages
    if isinstance(query, list):
        for msg in query:
            messages.append(HumanMessage(content=msg))
    else:
        messages.append(HumanMessage(content=query))

    state = {"messages": messages}

    response = agent.invoke(state)

    messages = response.get("messages", [])

    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_messages[-1] if ai_messages else "No response generated"