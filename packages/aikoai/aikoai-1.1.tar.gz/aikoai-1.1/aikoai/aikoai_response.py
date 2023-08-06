from typing import Optional


class AikoAIResponse:
    def __init__(self, data, headers):
        self._headers = headers
        self.data = data

    @property
    def request_id(self) -> Optional[str]:
        return self._headers.get("request-id")

    @property
    def organization(self) -> Optional[str]:
        return self._headers.get("AikoAI-Organization")

    @property
    def response_ms(self) -> Optional[int]:
        h = self._headers.get("AikoAI-Processing-Ms")
        return None if h is None else round(float(h))
