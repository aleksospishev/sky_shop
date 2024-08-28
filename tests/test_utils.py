from unittest.mock import patch

from src.utils import create_class_objects, read_json_file

data_test_json = {"key_1": ["test", "test_1"], "key_2": ["AB", "CD", "DG"]}


@patch("src.utils.json.load")
def test_read_json_file(mock_json_load) -> None:
    """Тест read_json."""
    mock_json_load.return_value = data_test_json
    res = read_json_file("./data_test/test.json")
    expected = {"key_1": ["test", "test_1"], "key_2": ["AB", "CD", "DG"]}
    assert res == expected


def test_create_class_objects(data_test):
    """Тест create_class."""
    res = create_class_objects(data_test)
    assert res[0].name == "Смартфоны"
