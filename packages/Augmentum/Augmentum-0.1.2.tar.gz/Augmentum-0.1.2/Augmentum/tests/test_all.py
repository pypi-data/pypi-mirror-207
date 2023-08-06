import Augmentum
import unittest
import numpy as np


class TestMethods(unittest.TestCase):
    # UNIT TESTS

    def test_is_matrix_square(self):
        non_square_matrix = [[1, 1, 1], [1, 1, 1]]
        assert Augmentum.augment_image(non_square_matrix) == None

    def test_rotate(self):
        square_matrix = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        rotate_matrix = Augmentum.rotate(square_matrix)
        assert rotate_matrix == [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

    def test_reflect(self):
        square_matrix = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        reflect_matrix = Augmentum.reflect(square_matrix)
        assert reflect_matrix == [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

    def test_right_shift(self):
        square_matrix = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
        rs_matrix = Augmentum.right_shift(square_matrix, 1)
        assert rs_matrix == [[0, 1, 1], [0, 1, 0], [0, 1, 0]]

    def test_upsample_scaling(self):
        square_matrix = [[1, 0], [0, 1]]
        us_matrix = Augmentum.upsample_scaling(np.array(square_matrix)).tolist()
        assert us_matrix == [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]

    # INTEGRATION TEST

    def test_rotate_shift(self):
        square_matrix = [[0, 0, 0], [0, 0, 0], [1, 0, 1]]
        rotate_matrix = Augmentum.rotate(square_matrix)
        rs_matrix = Augmentum.right_shift(rotate_matrix, 1)
        final_matrix = Augmentum.reflect(rs_matrix)
        assert final_matrix == [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
