import torch
import torch.nn as nn
import torch.optim as optim
import torch.optim.lr_scheduler as lr_scheduler

import numpy as np

import random

from models import Model, get_model
from loss import get_loss
from metric import get_metric
from dataloader import BaseDataset, BaseDataLoader
from utils import parse_config

def arg_parse():
    import argparse
    parser = argparse.ArgumentParser()
    add_arg = parser.add_argument
    add_arg('--config', default='config/config.toml', help='path to config file')
    
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = arg_parse()
    config = parse_config(args.config)

    random.seed(1000) # random
    np.random.seed(1000) # np.random
    torch.manual_seed(1000) # torch cpu
    torch.cuda.manual_seed_all(1000) # torch gpu
    # torch.backends.cudnn.deterministic = True # cudnn. *CAUTION* this will make it slow to learn.

    '''suggested format
    dataset = Dataset()
    dataloader = Dataloader()
    len_train = len(dataset) * 8 // 10
    len_val = len(dataset) - len_train
    train_dataloader, val_dataloader = dataloader.split([len_train, len_val])

    net = Net()
    if args.gpu:
        net = net.cuda()
        net = nn.DataParallel(net)
    
    criterion = get_loss(config)
    metric = get_metric(config)
    optimizer = get_optimizer(filter(lambda p:p.requires_grad, net.parameters()), config)
    scheduler = lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)

    model = Model(net)
    model.summary(input_size=(3, 1024, 1024), use_gpu=args.gpu)
    model.compile(optimizer, criterion, metric, scheduler)
    model.fit(train_dataloader=train_dataloader,
              val_dataloader=val_dataloader,
              epoch=args.epochs,
              use_gpu=args.gpu,
              pth='ckpt/models.pth',
              log='logs/first')
    '''