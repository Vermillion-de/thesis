import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

# torch.autograd.set_detect_anomaly(True)

# Positional encoding (section 5.1)
class Embedder(object):
    def __init__(self, **kwargs):
        embed_fns = []
        d = kwargs['input_dims']
        out_dim = 0
        if kwargs['include_input']:
            embed_fns.append(lambda x : x)
            out_dim += d
            
        max_freq = kwargs['max_freq_log2']
        N_freqs = kwargs['num_freqs']
        
        if kwargs['log_sampling']:
            freq_bands = 2.**torch.linspace(0., max_freq, steps=N_freqs)
        else:
            freq_bands = torch.linspace(2.**0., 2.**max_freq, steps=N_freqs)
            
        for freq in freq_bands:
            for p_fn in kwargs['periodic_fns']:
                embed_fns.append(lambda x, p_fn=p_fn, freq=freq : p_fn(x * freq))
                out_dim += d
                    
        self.embed_fns = embed_fns
        self.out_dim = out_dim
        
    def embed(self, inputs):
        return torch.cat([fn(inputs) for fn in self.embed_fns], -1)

def get_embedder(multires=10):    
    embed_kwargs = {
                'include_input' : True,
                'input_dims' : 3,
                'max_freq_log2' : multires-1,
                'num_freqs' : multires,
                'log_sampling' : True,
                'periodic_fns' : [torch.sin, torch.cos],
    }
    embedder_obj = Embedder(**embed_kwargs)
    embed = lambda x, eo=embedder_obj : eo.embed(x)
    return embed, embedder_obj.out_dim