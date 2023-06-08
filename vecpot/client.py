import requests
import os
from typing import Dict, List

from vecpot import exceptions

class VecPot:
    def __init__(
        self,
        api_key: str = None,
        timeout: int = 120,
    ):
        self.api_key = api_key or os.getenv("VECPOT_API_KEY")
        self.timeout = timeout
        self.api_url = "https://api.vecpot.com"
        self.api_version = "v0.1"
        
        
    def embed(
        self,
        text: str,
        domain: str = "general text",
        text_type: str = "document",
        task_objective: str = "retrieval",
        model: str = "instructor_large"
    ):
        json_data = {
            "text": text,
            "metadata": {
                "domain": domain,
                "text_type": text_type,
                "task_objective": task_objective,
            },
            "model": model
        }

        response = self._request(endpoint="embedding", json=json_data)
        
        return response
        
    def bulk_embed(
        self,
        data: List[Dict],
        model: str = "instructor_large"
    ):
        try:
            json_data = {
                "body": [
                    {
                        "text": d["text"],
                        "metadata": {
                            "domain": d["domain"] if "domain" in d.keys() else "general text",
                            "text_type": d["text_type"] if "text_type" in d.keys() else "document",
                            "task_objective": d["task_objective"] if "task_objective" in d.keys() else "retrieval"
                        }
                    }
                    for d in data
                ],
                "model": model
            }
        except:
            raise ValueError(f"{data} is invalid format.")

        response = self._request(endpoint="bulk_embedding", json=json_data)
        
        return response
    
    def _check_response(self, json_response: Dict, headers: Dict, status_code: int):
        if 400 <= status_code < 500:
            raise exceptions.CommonError(
                message=f"Unexpected client error (status {status_code}): {json_response}",
            )
        if status_code >= 500:
            raise exceptions.CommonError(message=f"Unexpected server error")


    def _request(self, endpoint, json=None, method="POST"):
        headers = {
            'accept': 'application/json',
            'api-token': self.api_key,
            'Content-Type': 'application/json'
        }

        url = f"{self.api_url}/{self.api_version}/api/{endpoint}"
        
        with requests.Session() as session:
            try:
                response = session.request(
                    method, url, headers=headers, json=json, timeout=self.timeout
                )
                
            except requests.exceptions.ConnectionError as e:
                raise exceptions.ConnectionError(str(e)) from e
            except requests.exceptions.RequestException as e:
                raise exceptions.CommonError(f"Unexpected exception ({e.__class__.__name__}): {e}") from e

            try:
                json_response = response.json()
            except:
                raise exceptions.JSONError("decode json failed")

            self._check_response(json_response, response.headers, response.status_code)
        return json_response
