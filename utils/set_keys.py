import os
from openai import OpenAI
client = OpenAI()
from elevenlabs import set_api_key

key_url_dict = {
    "openai": "https://platform.openai.com/account/api-keys",
    "elevenlabs": "https://elevenlabs.io/subscription (then click display picture -> Profile)"
}

key_dir = os.path.expanduser("~/Desktop/Workbench Keys")


def set_or_get_api_key(api_name):
    assert api_name in [
        "openai", "elevenlabs"], f'API "{api_name}" not recognized'
    try:
        with open(f"{key_dir}/{api_name}_api_key.txt") as f:
            api_key = f.read()
            os.environ[f"{api_name.upper()}_API_KEY"] = api_key
    except FileNotFoundError:
        save_api_key(api_name)
        return
    print(api_name, api_key)


def save_api_key(api_name):
    print(
        f"Your API key can be found at the following address: {key_url_dict[api_name]} (CMD + click to open in browser)")
    api_key = input(f"Enter your {api_name} API key: ")
    os.makedirs(key_dir, exist_ok=True)
    # save to file in keys folder
    with open(f"{key_dir}/{api_name}_api_key.txt", "x") as f:
        # with open(f"~/Desktop/Workbench Keys/{api_name}_api_key.txt", "x") as f:
        f.write(api_key)
    print(
        f"Saved {api_name} API key to {key_dir}/{api_name}_api_key.txt")
