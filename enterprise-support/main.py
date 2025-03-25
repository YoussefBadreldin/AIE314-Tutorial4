from langchain.agents import initialize_agent
from llm_manager import load_hf_llm
from tools import support_tools
from memory_manager import SupportMemory
from data_loader import load_knowledge_base

class EnterpriseSupportSystem:
    def __init__(self):
        self.llm = load_hf_llm()
        self.memory = SupportMemory()
        self.vectorstores = {
            "product_a": load_knowledge_base("product_a"),
            "product_b": load_knowledge_base("product_b"),
            "product_c": load_knowledge_base("product_c"),
        }
        self.agent = initialize_agent(
            tools=support_tools,
            llm=self.llm,
            agent="chat-conversational-react-description",
            memory=self.memory.memory,
            verbose=True,
        )
    
    def handle_query(self, query):
        try:
            response = self.agent.run(query)
            return {
                "response": response,
                "sources": ["product_a", "product_b"],
                "context": self.memory.get_history(),
            }
        except Exception as e:
            return {"error": str(e), "fallback": "Please try again later."}