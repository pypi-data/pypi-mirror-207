from .ckpt_pkl import CkptManagerPKL
from .ckpt_safetensor import CkptManagerSafe

def get_manager(ckpt_path:str):
    return CkptManagerSafe if ckpt_path.endswith('.safetensors') else CkptManagerPKL