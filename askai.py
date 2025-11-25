import os
import re
from langchain_community.utilities import SQLDatabase
from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_core.prompts import PromptTemplate

def processQuery(query_text):
    try:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            return {
                "answer": "Error: Unable to initialize Ask AI",
                "success": False
            }

        sql_prompt = PromptTemplate.from_template(
            """
            You are a SQL expert. Given the table schema below, write a SQLite query to answer the user's question.
            Do not wrap the query in markdown or code blocks. Return ONLY the raw SQL.
            
            Schema:
            {schema}
            
            Question: {question}
            SQL Query:
            """
        )

        db = SQLDatabase.from_uri("sqlite:///appDatabase.db")
        db_schema = db.get_table_info()

        llm = ChatOpenAI(temperature=0.5, openai_api_key=api_key,
                         model_name="gpt-4o")
        
        raw_sql = llm.invoke(sql_prompt.format(schema=db_schema, question=query_text)).content
        clean_query = re.sub(r"```sql|```", "", raw_sql).strip()
        
        sql_result = db.run(clean_query)

        answer_prompt = PromptTemplate.from_template(
            """
            Given the following user question, corresponding SQL query, and SQL result, answer the user question in max 3 lines in natural language.
            
            Question: {question}
            SQL Query: {query}
            SQL Result: {result}
            
            Answer:
            """
        )

        response = llm.invoke(answer_prompt.format(
            question=query_text,
            query=clean_query,
            result=sql_result
        ))

        return {
            "answer": response.content,
            "success": True
        }
    except Exception as e:
        print(e)
        return {
            "answer": "Encountered error while processing the request. Please try again",
            "success": False
        }
