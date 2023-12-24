import pytest
from functions import add_mempal, create_mempal, view_edit_mempal, minigame
from unittest.mock import patch, mock_open

@patch('builtins.input')
@patch('builtins.open', new_callable=mock_open)
def test_view_edit_mempal(mock_file, mock_input):
    # Arrange
    mock_input.side_effect = ['1', 'n']
    mock_file.return_value.__enter__.return_value.__iter__.return_value = iter([['Count', '11', '22', '33', '44', '55', '66', '77', '88', '99', '100', '0', '0']])

    # Act
    view_edit_mempal('Mempal.csv')

    # Assert
    mock_file.assert_called_once_with('Mempal.csv', 'r')
