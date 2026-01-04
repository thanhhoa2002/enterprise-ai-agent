SYSTEM_PROMPT = """
You are an AI assistant designed to help with enterprise-level tasks.
Your role is to provide accurate, efficient, and secure responses while adhering to company policies and best practices.
Always prioritize the user's needs and ensure your responses are clear, concise, and actionable.
"""

def build_prompt(query: str, context: str | None) -> str:
    if context:
        return f"""
            {SYSTEM_PROMPT}
            
            Internal Document Context:
            {context}
            
            User Query:
            {query}
            
            Please provide a detailed and accurate response based on the above context.
            """ 
    
    else:
        return f"""
            {SYSTEM_PROMPT}
            
            User Query:
            {query}
            
            Please provide a general response, without using insider information.
            """