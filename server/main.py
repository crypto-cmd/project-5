# Importing required packages
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pinecone import Pinecone
import os

from setup_rag import setup_rag
from inference import infer
from embed import embed

# Initiating a Flask application
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

def main(query):

    
    index = pc.Index('rag')
    query_results = index.query(
    namespace="ns1",
    vector=embed(query).tolist(),
    top_k=3,
    include_values=False,
    include_metadata=True
    )
    newQuery = f"Here are the top 3 professors that are related to my query: ```{query_results}```. Hence respond to my query as accurate as possible: {query}"
    response = infer(newQuery)
    return response




# The endpoint of our flask app
@app.route(rule="/ask", methods=["POST"])
@cross_origin()
def handle_request():
    query = request.args.get('query')
    res = main(query)
    return res
    
    

# Running the API
if __name__ == "__main__":
    setup_rag()
    app.run(debug=True)
