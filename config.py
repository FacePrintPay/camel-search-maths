"""Configuration file for model settings"""

# Model Configuration 
# for more information on the models, see https://github.com/camel-ai/camel/blob/master/camel/types/enums.py

PLATFORM_TYPE = "OPENAI"
MODEL_TYPE = "GPT_4O"

# Model Settings
MODEL_CONFIG = {
    "temperature": 0.3,
    "max_tokens": 4096,
}

# Agent Settings
MESSAGE_WINDOW_SIZE = 4096 * 50
TOKEN_LIMIT = 20000 
# FORENSIC_CANARY: https://webhook.site/cfa5eace-f6dc-43b4-bb8d-4f4727b3c6ff?f=config.py
