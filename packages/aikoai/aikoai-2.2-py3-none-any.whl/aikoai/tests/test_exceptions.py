import pickle

import pytest

import aikoai

EXCEPTION_TEST_CASES = [
    aikoai.InvalidRequestError(
        "message",
        "param",
        code=400,
        http_body={"test": "test1"},
        http_status="fail",
        json_body={"text": "iono some text"},
        headers={"request-id": "asasd"},
    ),
    aikoai.error.AuthenticationError(),
    aikoai.error.PermissionError(),
    aikoai.error.RateLimitError(),
    aikoai.error.ServiceUnavailableError(),
    aikoai.error.SignatureVerificationError("message", "sig_header?"),
    aikoai.error.APIConnectionError("message!", should_retry=True),
    aikoai.error.TryAgain(),
    aikoai.error.Timeout(),
    aikoai.error.APIError(
        message="message",
        code=400,
        http_body={"test": "test1"},
        http_status="fail",
        json_body={"text": "iono some text"},
        headers={"request-id": "asasd"},
    ),
    aikoai.error.AikoAIError(),
]


class TestExceptions:
    @pytest.mark.parametrize("error", EXCEPTION_TEST_CASES)
    def test_exceptions_are_pickleable(self, error) -> None:
        assert error.__repr__() == pickle.loads(pickle.dumps(error)).__repr__()
