"""Top-level package for Pytorch Tabular."""

__author__ = """Manu Joseph"""
__email__ = 'manujosephv@gmail.com'
__version__ = '0.1.0'

# Relative imports
from .tabular_model import TabularModel
from .tabular_datamodule import TabularDatamodule
from .models.category_embedding import CategoryEmbeddingModel, CategoryEmbeddingModelConfig
from .models.node import NodeConfig, NODEModel

__all__ = ["TabularModel","TabularDatamodule", "CategoryEmbeddingModel", "CategoryEmbeddingModelConfig", "NodeConfig", "NODEModel"]

# fix Sphinx issues, see https://bit.ly/2K2eptM
for item in __all__:
    if hasattr(item, "__module__"):
        setattr(item, "__module__", __name__)