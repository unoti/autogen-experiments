import json

class Config:
    def __init__(self, filename: str = 'local/config/config.json'):
        with open(filename, 'r') as f:
            content = f.read()
        data = json.loads(content)
        self.api_key = data['openai']['api_key']

def default_config() -> Config:
    return Config()
