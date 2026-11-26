# -*- coding: utf-8 -*-
# Signature Forensics Hybrid Siamese Pipeline

import os, glob, shutil, warnings, fitz, pyheif, numpy as np
import torch, torch.nn as nn, torch.nn.functional as F, torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, models
from PIL import Image
from skimage.feature import hog, local_binary_pattern
from sklearn.metrics import roc_curve, auc, accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
IMG_SIZE = (224, 224)
PCA_DIMS = 64
EMBEDDING_DIM = 128

class HybridSiamese(nn.Module):
    def __init__(self, dim=128, hand_dim=PCA_DIMS):
        super().__init__()
        backbone = models.efficientnet_b0(pretrained=True)
        self.cnn = nn.Sequential(*list(backbone.children())[:-1])
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.cnn_fc = nn.Linear(1280, 256)
        self.hand_fc = nn.Linear(hand_dim, 128)
        self.fusion = nn.Linear(256+128, dim)

    def forward(self, img, hand):
        x = self.cnn(img)
        x = self.pool(x).flatten(1)
        cnn_out = F.relu(self.cnn_fc(x))
        hand_out = F.relu(self.hand_fc(hand))
        fused = torch.cat([cnn_out, hand_out], dim=1)
        return F.normalize(self.fusion(fused), p=2, dim=1)
