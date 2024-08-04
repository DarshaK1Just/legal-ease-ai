from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from ai71_config import AI71_API_KEY, AI71_BASE_URL

chat = ChatOpenAI(
    model="tiiuae/falcon-180B-chat",
    api_key=AI71_API_KEY,
    base_url=AI71_BASE_URL,
    streaming=False,
    max_tokens=4096
)

def summarize_document(text: str) -> str:
    prompt = (
        "You are a legal expert tasked with summarizing a legal document. "
        "Please provide a concise summary of the document's main points. "
        "Focus on capturing the key arguments, conclusions, or findings in a single paragraph. "
        "Avoid unnecessary details and ensure the summary reflects the core content of the document. "
        "Here is the document:\n\n" + text
    )
    try:
        response = chat.invoke(
            [
                SystemMessage(content="You are a legal expert and assistant."),
                HumanMessage(content=prompt)
            ]
        )
        summary = response['choices'][0]['message']['content'].strip()
        return summary
    except Exception as e:
        print(f"Error summarizing document: {e}")
        return "Error: Could not summarize the document."
