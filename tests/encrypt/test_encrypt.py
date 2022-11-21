from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("AABBCC", "1")
    with pytest.raises(TypeError):
        encrypt_message(None, 3)
    with pytest.raises(TypeError):
        encrypt_message(3, 3)
    assert encrypt_message("AABBCC", 1) == "A_CCBBA"
    assert encrypt_message("ABBCCA", 2) == "CCBB_AA"
    assert encrypt_message("AABBCC", -1) == "CCBBAA"
