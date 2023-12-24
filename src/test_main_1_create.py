import pytest
from functions import add_mempal, create_mempal, view_edit_mempal, minigame
from unittest.mock import patch, mock_open

@patch('functions.add_mempal')
@patch('builtins.input')
@patch('builtins.open')
def test_create_mempal(mock_open, mock_input, mock_add_mempal):
    # Arrange
    mock_input.side_effect = ['Count']
    mock_add_mempal.return_value = ['11', '22', '33', '44', '55', '66', '77', '88', '99', '100']

    # Act
    create_mempal('Mempal.csv')

    # Assert
    mock_open.assert_called_once_with('Mempal.csv', 'a', newline='')
    mock_input.assert_called_once_with('Enter the name of this Memory Palace: ')
    mock_add_mempal.assert_called_once_with()