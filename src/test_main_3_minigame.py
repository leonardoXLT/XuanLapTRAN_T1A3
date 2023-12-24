import pytest
from functions import add_mempal, create_mempal, view_edit_mempal, minigame
from unittest.mock import patch, mock_open


@patch('builtins.input')
@patch('builtins.open', new_callable=mock_open)
def test_minigame(mock_file, mock_input):
    # Arrange
    mock_input.side_effect = ['1', '11', '22', '33', '44', '55', '66', '77', '88', '99', '100']
    mock_file.return_value.__enter__.return_value.__iter__.return_value = iter([['Count', '11', '22', '33', '44', '55', '66', '77', '88', '99', '100', '0', '0']])

    # Act
    minigame('Mempal.csv')

    # Assert
    assert mock_file.call_count == 2  # The file is opened twice: once for reading and once for writing