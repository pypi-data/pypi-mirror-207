import requests

from typing import Optional, TypedDict

class ModelConfig(TypedDict):
    model: str
    provider: str
    temperature: float
    max_tokens: int

class EventType(TypedDict):
    api_key: str
    inputs: dict[str, str]
    output: str
    model_config: Optional[ModelConfig]
    task_id: str
    person_id: Optional[str]
    total_tokens: Optional[int]

class Wale:
    def __init__(self, api_root: str, api_key: str) -> None:
        if not api_root:
            api_root = "https://api.trywale.com"
        if not api_key:
            raise ValueError("api_key is required. Get one at https://ide.trywale.com/")
        self.api_root = api_root
        self.api_key = api_key

    def log(
        self, 
        inputs: dict[str, str], 
        output: str,
        task_id: str,
        model_config: Optional[ModelConfig] = None,
        person_id: Optional[str] = None,
        total_tokens: Optional[int] = None,
    ) -> bool:
        data = {
            "api_key": self.api_key,
            "inputs": inputs,
            "output": output,
            "model_config": model_config,
            "task_id": task_id,
            "person_id": person_id,
            "total_tokens": total_tokens,
        }
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(f"{self.api_root}/logger", json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(error.response.text)
            return False
