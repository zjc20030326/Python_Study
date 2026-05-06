import torch
from d2l import torch as d2l

x = torch.arange(12)
print(x)
print(x.shape)
print(torch.cuda.is_available())
