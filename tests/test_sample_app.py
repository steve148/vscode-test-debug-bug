from datetime import UTC

from sample_app import now_local


def test_num_dragon_characters():
    result = now_local()
    assert result.tzinfo != UTC
