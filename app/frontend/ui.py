import streamlit as st
import requests
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

st.set_page_config(page_title="Langgraph Agent", layout="centered")
st.title("AI Agent using Langgraph")

system_prompt = st.text_area("Define your AI Agent: ", height=70, 
                            placeholder="Example: You are a helpful assistant specialized in...")
selected_model = st.selectbox("Select your AI model: ", settings.ALLOWED_MODEL_NAMES)

allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area("Enter your query: ", height=150, 
                         placeholder="Type your question here...")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent") and user_query.strip():
    # Display user query in a nice box using Streamlit's native containers
    with st.container():
        st.markdown("### Your Query")
        st.info(user_query)
    
    payload = {
        "model_name": selected_model,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }

    try:
        logger.info("Sending request to backend")

        with st.spinner("Agent is thinking..."):
            response = requests.post(API_URL, json=payload, timeout=60)
        
        if response.status_code == 200:
            agent_response = response.json().get("response", "")
            logger.info("Successfully received response from backend")

            # Display the response in a clean, formatted way
            st.subheader("Agent Response")
            
            # Use Streamlit's success container for the response
            with st.container():
                st.success(agent_response)
            
            # Add some metadata
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"**Model:** {selected_model}")
            with col2:
                st.caption(f"**Web Search:** {'Enabled' if allow_web_search else 'Disabled'}")

        else:
            logger.error(f"Backend error: {response.status_code} - {response.text}")
            st.error(f"Backend error: {response.status_code}")
            if response.text:
                st.code(response.text, language="json")

    except requests.exceptions.Timeout:
        logger.error("Request timeout")
        st.error("The request took too long. Please try again.")
    
    except requests.exceptions.ConnectionError:
        logger.error("Connection error")
        st.error("Cannot connect to the backend. Make sure the server is running.")
    
    except Exception as e:
        logger.error(f"Error occurred while sending request to backend: {str(e)}")
        st.error(f"Error: {str(e)}")