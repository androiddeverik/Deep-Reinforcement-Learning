import torch
import torch.nn as nn
import torch.nn.functional as F

# Network with only two layers was last tested version.
# Optimal number of layers and hidden neurons should be determined via hyper parameter search


class QNetwork_FC(nn.Module):
    def __init__(self, state_size, action_size,  hidsize1 = 64, hidsize2 = 64):
        super(QNetwork_FC, self).__init__()
        self.fc1_val = nn.Linear(state_size, hidsize1)
        self.fc2_val = nn.Linear(hidsize1, hidsize2)
        self.fc3_val = nn.Linear(hidsize2, 1)

        self.fc1_adv = nn.Linear(state_size, hidsize1)
        self.fc2_adv = nn.Linear(hidsize1, hidsize2)
        self.fc3_adv = nn.Linear(hidsize2, action_size)

    def forward(self, x):
        # Value net
        val = F.relu(self.fc1_val(x))
        val = F.relu(self.fc2_val(val))
        val = self.fc3_val(val)

        # Advantage net
        adv = F.relu(self.fc1_adv(x))
        adv = F.relu(self.fc2_adv(adv))
        adv = self.fc3_adv(adv)


        return adv + val - adv.mean()