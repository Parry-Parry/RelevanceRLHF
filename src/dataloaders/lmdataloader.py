import torch 
import ir_datasets
from . import read_tsv

class LMDataset():
    def __init__(self, irds_root : str = None, rootpath : str = None, **kwargs) -> None:

        self.triples = None
        self.collection = None 
        self.queries = None

        if not irds_root:
            assert rootpath, 'Must define either an irds:<> dataset or a root path to follow'
            self.load_root(rootpath)
        else: self.load_irds(irds_root)

    def load_irds(self, name):
        ds = ir_datasets.load(name)

    def load_root(self, root):
        pass 
        
    def __len__(self):
        return len(self.triples)
    
    def __getitem__(self, idx):
        return self.triples[idx]

