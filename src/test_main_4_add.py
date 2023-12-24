import pytest
from functions import add_mempal, create_mempal, view_edit_mempal, minigame
from unittest.mock import patch, mock_open

@patch('builtins.input')
def test_add_mempal(mock_input):
    # Arrange
    mock_input.side_effect = ['11', 'y', '22', 'y', '33', 'y', '44', 'y', '55', 'y', '66', 'y', '77', 'y', '88', 'y', '99', 'y', '100', 'n']

    # Act
    loci = add_mempal()

    # Assert
    assert loci == ['11', '22', '33', '44', '55', '66', '77', '88', '99', '100']
    assert mock_input.call_count == 20  # The input function is called 20 times: 10 times for entering the loci and 10 times for choosing to add next or finish