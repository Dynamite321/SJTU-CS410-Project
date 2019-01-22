import torch
from model import Net
from dataset import GeneDataset
from torch import nn, optim
from torch.autograd import Variable
from torch.utils.data import DataLoader
import numpy as np
from torchvision import datasets, transforms

max_epochs = 300
learning_rate = 0.01
batch_size = 64

train_dataset = GeneDataset(True)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataset = GeneDataset(False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
model = Net(453,7)

if torch.cuda.is_available():
    model = model.cuda()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate,momentum=0.9)

best = -1
for epoch in range(max_epochs):
    corrects = []
    total = 0
    train_num = len(train_loader.sampler)
    for data in train_loader:
        model.train()
        gene, label = data
        total += label.size(0)
        if torch.cuda.is_available():
            gene = gene.cuda()
            label = label.cuda()
        else:
            gene = Variable(gene)
            label = Variable(label)
        out = model(gene)
        #print(label)
        #print(out)
        optimizer.zero_grad()
        loss = criterion(out, label)
        print_loss = loss.data.item()
        pred_choice = out.data.max(1)[1]
        correct = pred_choice.eq(label.data).cpu().sum()
        corrects.append(correct)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print('epoch: {}, loss: {:.4}, acc: {:.4}'.format(epoch, loss.data.item(), np.sum(corrects)/train_num))

    test_correct = 0
    test_num = len(test_loader.sampler)
    for data, label in test_loader:
        model.eval()
        if torch.cuda.is_available():
            data = data.cuda()
            label = label.cuda()
        optimizer.zero_grad()
        output = model(data)

        pred = output.max(1, keepdim=True)[1]
        test_correct += int(
            pred.eq(label.view_as(pred)).sum()
        )
    if (test_correct / float(test_num) > best):
        best = test_correct / float(test_num)
    print(
        "Test Accuracy: {}/{} ({:.2f}%)".format(test_correct, test_num, 100.0 * test_correct / test_num))
    print("best:", best)

