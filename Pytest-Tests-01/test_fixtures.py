import pytest;

@pytest.fixture()
def setup_names():
    print("=" * 15);
    print("\n ... Setup From Fixtures ...\n");
    print("=" * 15);

    return ["Jafar", "Loka", "Jafar-Loka-01"];

def test_len_of_names(setup_names):
    assert len(setup_names) == 3;

@pytest.mark.usefixtures("setup_names")
def test_use_fixtures():
    assert 1 == 1;