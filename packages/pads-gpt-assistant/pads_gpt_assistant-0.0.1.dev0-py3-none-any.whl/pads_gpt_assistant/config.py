from dataclasses import dataclass
import os

@dataclass
class openai_config:
    api_key:str
    organization:str
    language:str = 'python'
    model:str = "gpt-3.5-turbo-0301"

    @classmethod
    def from_file(cls, language = 'python'):
        filepath = __file__.replace('config.py','openai_config')
        assert os.path.exists(filepath)
        with open(filepath) as f:
            kwargs = {}
            for line in f.readlines():
                texts = [text.strip() for text in line.split("=")]
                if texts[0] == 'organization':
                    kwargs['organization'] = texts[1]
                elif texts[0] == 'api_key':
                    kwargs['api_key'] = texts[1]
        kwargs['language'] = language
        return cls(**kwargs)
    
def create_openai_config_file(organization, api_key):
    filepath = __file__.replace('config.py','openai_config')
    with open(filepath, 'w') as f:
        message = f"""organization={organization}
api_key={api_key}"""
        f.write(message)
        f.close()


if __name__ == '__main__':
    import argparse
    import argparse
    parser = argparse.ArgumentParser(description='Coding GPT')
    parser.add_argument('--organization', required = True, type = str)
    parser.add_argument('--api_key', required = True, type = str)
    args = parser.parse_args()

    create_openai_config_file(args.organization, args.api_key)