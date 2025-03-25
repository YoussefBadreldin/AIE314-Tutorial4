from langchain.memory import ConversationBufferMemory

class SupportMemory:
    def __init__(self):
        self.memory = ConversationBufferMemory(return_messages=True)
    
    def add_message(self, role, content):
        if role == "user":
            self.memory.chat_memory.add_user_message(content)
        else:
            self.memory.chat_memory.add_ai_message(content)
    
    def get_history(self):
        return self.memory.load_memory_variables({})