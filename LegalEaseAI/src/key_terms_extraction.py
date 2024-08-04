from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from ai71_config import AI71_API_KEY, AI71_BASE_URL

chat = ChatOpenAI(
    model="tiiuae/falcon-180B-chat",
    api_key=AI71_API_KEY,
    base_url=AI71_BASE_URL,
    streaming=False
)

def extract_key_terms(text: str) -> str:
    prompt = (
        "You are an expert in legal document analysis. Extract the most important legal terms and jargon from the following document. "
        "These should include legal terms, clauses, and phrases that are significant in the context of the document. "
        "Provide these terms as a comma-separated list.\n\n" + text
    )
    try:
        response = chat.invoke(
            [
                SystemMessage(content="You are an expert in legal document analysis."),
                HumanMessage(content=prompt)
            ]
        )
        key_terms = response['choices'][0]['message']['content'].strip()
        return key_terms
    except Exception as e:
        print(f"Error extracting key terms: {e}")
        return "Error: Could not extract key terms."
