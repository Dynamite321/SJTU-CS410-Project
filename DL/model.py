import torch
import torch.nn as nn

class Net(nn.Module):

    def __init__(self, input_dim, output_dim):
        super(Net, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.layer1 = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(inplace=True),
        )
        self.layer2 = nn.Sequential(
            #nn.Dropout(),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(inplace=True),
        )

        self.layer3 = nn.Sequential(
            #nn.Dropout(),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(inplace=True),
        )
        self.layer4 = nn.Sequential(
            #nn.Dropout(),
            nn.Linear(256, output_dim),
        )

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        return x
