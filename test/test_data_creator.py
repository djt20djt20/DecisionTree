import unittest
from src.data_creator import DataCreator
import pandas as pd

class TestDataCreator(unittest.TestCase):
    def setUp(self):
        self.data_creator = DataCreator()

    def test_fetch_breast_cancer_data(self):
        self.data_creator.fetch_breast_cancer_data()
    
        expected_keys = ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']
        self.assertTrue(all((key in self.data_creator.data.keys() for key in expected_keys)), 'Not all expected keys are present')

        self.assertEqual(self.data_creator.data.data.shape, (569, 30), 'Data shape should be (569, 30)')
        self.assertEqual(len(self.data_creator.data.target), 569, 'Target length should be 569')

        expected_feature_names = [
            'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
            'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
            'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error',
            'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
            'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness',
            'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension'
        ]
        self.assertListEqual(self.data_creator.data.feature_names.tolist(), expected_feature_names, "Feature names do not match expected values")

    def return_data_frame(self):
        df = self.return_data_frame()
        feature_columns = df.columns[:-1]
        expected_feature_names = [
            'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
            'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
            'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error',
            'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
            'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness',
            'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension'
        ]
        feature_types = [dtype == pd.api.types.pandas_dtype('float64') for dtype in df[feature_columns].dtypes]
        self.assertTrue(all(feature_types), "All feature columns should be of type float64")
        self.assertTrue(feature_columns,expected_feature_names)
        self.assertTrue(df.target == pd.api.pandas_dtype('int64'), 'target should be int_64')