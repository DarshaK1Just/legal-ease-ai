from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from ai71_config import AI71_API_KEY, AI71_BASE_URL

chat = ChatOpenAI(
    model="tiiuae/falcon-180B-chat",
    api_key=AI71_API_KEY,
    base_url=AI71_BASE_URL,
    streaming=False
)

def get_actionable_insights(text: str) -> str:
    prompt = (
        "You are a legal advisor. Based on the content of the following document, provide actionable insights. "
        "This includes recommendations, legal actions to be taken, or decisions that should be made. "
        "Focus on practical advice that a legal professional can use in response to the document. "
        "Here is the document:\n\n" + text
    )
    try:
        response = chat.invoke(
            [
                SystemMessage(content="You are a legal advisor."),
                HumanMessage(content=prompt)
            ]
        )
        insights = response['choices'][0]['message']['content'].strip()
        return insights
    except Exception as e:
        print(f"Error getting actionable insights: {e}")
        return "Error: Could not get actionable insights."
