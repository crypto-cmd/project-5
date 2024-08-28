from dotenv import load_dotenv
load_dotenv()
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
import os
import json

from embed import embed



# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

def setup_rag():
    index_name = "rag"
    if index_name not in pc.list_indexes().names():
        # Create a Pinecone index
        pc.create_index(
        name="rag",
        dimension=768, # Dimension of the embeddings of m3e-base
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        # Load the review data
        data = json.load(open("reviews.json"))
        processed_data = []

        # Create embeddings for each review
        for review in data["reviews"]:

            embedding = embed(review['review'])
            processed_data.append(
                {
                    "values": embedding,
                    "id": review["professor"],
                    "metadata":{
                        "review": review["review"],
                        "subject": review["subject"],
                        "stars": review["stars"],
                    }
                }
            )

        # Insert the embeddings into the Pinecone index
        index = pc.Index("rag")
        upsert_response = index.upsert(
            vectors=processed_data,
            namespace="ns1",
        )
        print(f"Upserted count: {upsert_response['upserted_count']}")

        # Print index statistics
        print(index.describe_index_stats())