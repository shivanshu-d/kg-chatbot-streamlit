Knowledge-Graph-Powered Chatbot for eBay User Agreement
This project is a Streamlit-based chatbot that uses a Knowledge Graph (KG) constructed from the eBay User Agreement. It answers user questions based on factual, graph-grounded triples using an open-source LLM.
Project Architecture
graph TD
 A[PDF Document] --> B[Text Cleaning]
 B --> C[NER + RE Extraction]
 C --> D[Entity-Relation Triples]
 D --> E[Knowledge Graph (NetworkX)]
 F[User Question] --> G[Graph Querying]
 E --> G
 G --> H[Inject into LLM Prompt]
 H --> I[Open-source LLM Response (TinyLlama)]
 I --> J[Answer to User]

Folder Structure
knowledge-graph-chatbot/
├── data/                
├── triples/              
├── kg/                   
├── notebooks/            
├── src/                  
│   ├── graph_builder_nx.py
│   ├── retriever_nx.py
│   └── llm_prompt.py
├── app.py                
├── requirements.txt      
├── README.md             
└── report.pdf            
 
Setup Instructions
# Step 1: Clone repo
$ git clone https://github.com/shivanshu-d/kg-chatbot-streamlit
$ cd kg-chatbot-ebay
 
# Step 2: Install dependencies
$ pip install -r requirements.txt
 
# Step 3: Build the Knowledge Graph
$ python src/graph_builder.py
 
# Step 4: Run the chatbot
$ streamlit run app.py
Prompting Strategy
Context:
- eBay requires sellers to follow policies.
- Sellers must comply with verification requirements.
 
Q: What does eBay require from sellers?
A: eBay requires sellers to follow policies and complete verification.

Sample Questions
* What is the responsibility of a seller?
* What does eBay offer?
* What happens if a user violates the terms?
Credits
* Developed for Amlgo Labs Junior AI Engineer Assignment
* Built by: Shivanshu