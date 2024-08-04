from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from ai71_config import AI71_API_KEY, AI71_BASE_URL

chat = ChatOpenAI(
    model="tiiuae/falcon-180B-chat",
    api_key=AI71_API_KEY,
    base_url=AI71_BASE_URL,
    streaming=False
)

def categorize_document(text: str) -> str:
    prompt = (
        "You are an expert in legal document classification. Based on the content of the following document, "
        "please categorize it into one of the following types: contract, court ruling, legal brief, or legal opinion. "
        "If the document does not fit any of these categories, indicate 'Other' and provide a brief explanation. "
        "Here is the document:\n\n" + text
    )
    try:
        response = chat.invoke(
            [
                SystemMessage(content="You are an expert in legal document classification."),
                HumanMessage(content=prompt)
            ]
        )
        category = response['choices'][0]['message']['content'].strip()
        return category
    except Exception as e:
        print(f"Error categorizing document: {e}")
        return "Error: Could not categorize the document."
