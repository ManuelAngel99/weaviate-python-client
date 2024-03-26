from typing import Dict, Optional, cast
from pydantic import BaseModel, ConfigDict, Field


class _IntegrationConfig(BaseModel):
    model_config = ConfigDict(strict=True)

    def _to_header(self) -> Dict[str, str]:
        # headers have to be strings
        return_dict = cast(dict, self.model_dump(by_alias=True, exclude_none=True))
        for key, value in return_dict.items():
            return_dict[key] = str(value)

        return return_dict


class _IntegrationConfigCohere(_IntegrationConfig):
    api_key: str = Field(serialization_alias="X-Cohere-Api-Key")
    request_per_minute_embeddings: Optional[int] = Field(
        serialization_alias="X-Cohere-Ratelimit-RequestPM-Embedding"
    )
    base_url: Optional[str] = Field(serialization_alias="X-Cohere-Baseurl")


class _IntegrationConfigOpenAi(_IntegrationConfig):
    api_key: str = Field(serialization_alias="X-Openai-Api-Key")
    organization: Optional[str] = Field(serialization_alias="X-Openai-Organization")
    request_per_minute_embeddings: Optional[int] = Field(
        serialization_alias="X-Openai-Ratelimit-RequestPM-Embedding"
    )
    tokens_per_minute_embeddings: Optional[int] = Field(
        serialization_alias="X-Openai-Ratelimit-TokenPM-Embedding"
    )
    base_url: Optional[str] = Field(serialization_alias="X-Openai-Baseurl")


class Integrations:
    @staticmethod
    def cohere(
        *,
        api_key: str,
        base_url: Optional[str] = None,
        request_per_minute_embeddings: Optional[int] = None
    ) -> _IntegrationConfig:
        return _IntegrationConfigCohere(
            api_key=api_key,
            request_per_minute_embeddings=request_per_minute_embeddings,
            base_url=base_url,
        )

    @staticmethod
    def openai(
        *,
        api_key: str,
        request_per_minute_embeddings: Optional[int] = None,
        tokens_per_minute_embeddings: Optional[int] = None,
        organization: Optional[str] = None,
        base_url: Optional[str] = None
    ) -> _IntegrationConfig:
        return _IntegrationConfigOpenAi(
            api_key=api_key,
            request_per_minute_embeddings=request_per_minute_embeddings,
            tokens_per_minute_embeddings=tokens_per_minute_embeddings,
            organization=organization,
            base_url=base_url,
        )