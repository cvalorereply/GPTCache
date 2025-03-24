from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Union

import numpy as np

from model.metadata_def import CacheMetadata


@dataclass
class VectorData:
    id: int
    data: np.ndarray
    metadata: Optional[List[CacheMetadata]]


class VectorBase(ABC):
    """VectorBase: base vector store interface"""

    @abstractmethod
    def mul_add(self, datas: List[VectorData]):
        pass

    @abstractmethod
    def search(self, data: np.ndarray, top_k: int, metadata: Optional[List[CacheMetadata]]):
        pass

    @abstractmethod
    def rebuild(self, ids=None) -> bool:
        pass

    @abstractmethod
    def delete(self, ids) -> bool:
        pass

    def flush(self):
        pass

    def close(self):
        pass

    def get_embeddings(self, data_id: Union[int, str]) -> Optional[np.ndarray]:
        raise NotImplementedError

    def update_embeddings(self, data_id: Union[int, str], emb: np.ndarray):
        pass
