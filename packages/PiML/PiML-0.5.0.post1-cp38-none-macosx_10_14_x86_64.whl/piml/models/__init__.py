from .gaminet import GAMINetClassifier, GAMINetRegressor
from .ebm import ExplainableBoostingRegressor, ExplainableBoostingClassifier, EBMExplainer
from .reludnn import ReluDNNClassifier, ReluDNNRegressor, UnwrapperRegressor, UnwrapperClassifier
from .gam import GAMRegressor, GAMClassifier
from .glm import GLMRegressor, GLMClassifier
from .tree import TreeClassifier, TreeRegressor
from .xgb1 import XGB1Classifier, XGB1Regressor
from .xgb2 import XGB2Classifier, XGB2Regressor
from .figs import FIGSClassifier, FIGSRegressor

__all__ = ["UnwrapperRegressor", "UnwrapperClassifier", 'GAMINetClassifier', 'GAMINetRegressor',
            'ExplainableBoostingRegressor', 'ExplainableBoostingClassifier', 'EBMExplainer',
            'ReluDNNClassifier', 'ReluDNNRegressor', "GAMRegressor", "GAMClassifier", "GLMRegressor",
            "GLMClassifier", 'TreeClassifier', 'TreeRegressor',
            'XGB1Classifier', 'XGB1Regressor', 'XGB2Classifier', 'XGB2Regressor',
             'FIGSClassifier', 'FIGSRegressor']


def get_all_supported_models():
    return sorted(__all__)
