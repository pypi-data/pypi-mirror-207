from tempfile import NamedTemporaryFile

import pytest

import aikoai
from aikoai import util


@pytest.fixture(scope="function")
def api_key_file():
    saved_path = aikoai.api_key_path
    try:
        with NamedTemporaryFile(prefix="aikoai-api-key", mode="wt") as tmp:
            aikoai.api_key_path = tmp.name
            yield tmp
    finally:
        aikoai.api_key_path = saved_path


def test_aikoai_api_key_path(api_key_file) -> None:
    print("sk-foo", file=api_key_file)
    api_key_file.flush()
    assert util.default_api_key() == "sk-foo"


def test_aikoai_api_key_path_with_malformed_key(api_key_file) -> None:
    print("malformed-api-key", file=api_key_file)
    api_key_file.flush()
    with pytest.raises(ValueError, match="Malformed API key"):
        util.default_api_key()
