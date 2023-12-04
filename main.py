from langchain.chains import create_extraction_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredFileLoader

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key="YOUR_OPENAI_API_KEY")

schema = {
    "properties": {
        "relevant_companies": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
                "company_name": {"type": "string"},
                "company_domain": {"type": "string"},
            },
            "required": ["company_name", "company_domain"],

          }
        },
        "topic": {"type": "string"}
    },
    "required": ["relevant_companies", "topic"],
}

txt_file_path = UnstructuredFileLoader("./output.txt")


def extract(content: str, schema: dict):
  return create_extraction_chain(schema=schema, llm=llm).run(content)

def load_output_file(txt_file_path):
  data = txt_file_path.load()
  return data[0].page_content

if __name__ == "__main__":
  print(extract(schema=schema, content=load_output_file(txt_file_path=txt_file_path)))