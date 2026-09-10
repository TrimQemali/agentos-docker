

from os import getenv

from agno.models.openai.like import OpenAILike

ZAI_BASE_URL = getenv("ZAI_BASE_URL", "https://api.z.ai/api/coding/paas/v4")
ZAI_MODEL_ID = getenv("ZAI_MODEL_ID", "glm-4.7")


def default_model() -> OpenAILike:
    """Fresh model instance per agent — avoids shared-state footguns.

    Reads ZAI_API_KEY (not OPENAI_API_KEY) — OpenAILike takes any OpenAI-compatible
    provider; api_key=None falls through to OpenAILike's own env lookup only if it
    matches OPENAI_API_KEY, so it's passed explicitly here instead.
    """
    return OpenAILike(id=ZAI_MODEL_ID, base_url=ZAI_BASE_URL, api_key=getenv("ZAI_API_KEY"))
