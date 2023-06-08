import os

import vecpot
import pytest

VP_API_KEY = os.getenv("VP_API_KEY")
vp = vecpot.VecPot(api_key=VP_API_KEY)

def test_simple_embedding_for_data_types():
    embedding_response = vp.embed(text="data")
    
    assert isinstance(embedding_response, dict)
    assert "embeddings" in embedding_response.keys()
    assert "token_len" in embedding_response.keys()
    assert "response_status" in embedding_response.keys()
    
def test_instructor_embedding():
    embedding_response = vp.embed(text="data", model="instructor_large")
    
    assert isinstance(embedding_response["embeddings"], list)
    assert isinstance(embedding_response["embeddings"][0], list)
    assert len(embedding_response["embeddings"][0]) == 768
    
    assert isinstance(embedding_response["token_len"], int)
    assert embedding_response["response_status"] == "SUCCESS"
    
def test_bulk_embedding():
    embedding_response = vp.bulk_embed(data=[{"text": "data"}, {"text": "data"}], model="instructor_large")
    
    assert isinstance(embedding_response, dict)
    assert "embeddings" in embedding_response.keys()
    assert "token_len" in embedding_response.keys()
    assert "response_status" in embedding_response.keys()