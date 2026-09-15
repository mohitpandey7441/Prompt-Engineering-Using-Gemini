import streamlit as st
from google import genai
from google.genai import types

# -------------------------------
# CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="Gemini App",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Prompt Engineering Using Gemini")

# -------------------------------
# GEMINI API KEY
# -------------------------------
api_key = st.text_input(
    "🔑 Enter your Gemini API Key",
    type="password"
)

if api_key:

    client = genai.Client(api_key=api_key)

    # -------------------------------
    # DUMMY RETRIEVER
    # -------------------------------
    def retriever_info(query):
        # Replace this later with:
        # - Vector database
        # - PDF search
        # - Document retrieval
        # - Database lookup
        return "Explain about India's economy."

    # -------------------------------
    # RAG FUNCTION
    # -------------------------------
    def rag_query(query):

        retrieved_info = retriever_info(query)

        augmented_prompt = f"""
User query:
{query}

Retrieved information:
{retrieved_info}

Using the retrieved information, provide a clear and useful answer
to the user's query.
"""

        # Current Google Gen AI SDK
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=augmented_prompt,
            config=types.GenerateContentConfig(
                temperature=1.0,
                max_output_tokens=1000,
                top_p=1.0,
                top_k=50,
                stop_sequences=["End"]
            )
        )

        return response.text.strip()

    # -------------------------------
    # UI SECTION
    # -------------------------------
    query = st.text_area(
        "💬 I am bot:",
        "How may I help you?"
    )

    if st.button("🔍 Generate Response"):

        if not query.strip():
            st.warning("Please enter a query first.")

        else:
            with st.spinner("Generating response..."):

                try:
                    answer = rag_query(query)

                    st.success("✅ Response Generated!")

                    st.markdown(
                        f"**Answer:**\n\n{answer}"
                    )

                except Exception as e:
                    st.error(f"Error: {e}")

else:
    st.info("Please enter your Gemini API key to start.")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit + Google Gemini API + mohit"
)
