# simple pytorch network
import torch
import torch.nn as nn
import torch.utils.data
from torch.nn.parameter import Parameter

class LearnedSwish(nn.Module):
    def __init__(self, slope = 1.0):
        super(LearnedSwish, self).__init__()
        self.slope = Parameter(torch.tensor(slope), requires_grad=True)# * (torch.ones(1))
        self.slope.requiresGrad = True
    def forward(self, x):
        return self.slope * x * torch.sigmoid(x) 
    

