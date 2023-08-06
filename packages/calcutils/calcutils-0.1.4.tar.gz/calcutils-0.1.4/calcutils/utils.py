import json
import math
import os

import torch
from torch import nn
import torch.nn.functional as F
from transformers.activations import gelu_new, silu
import matplotlib.pyplot as plt
import numpy as np

import pickle


def save_stat(data, name='weight', part='test', use=True):
    if use:
        path = "{}_{}.json".format(part, name)
        if os.path.exists(path):
            with open(path, 'r') as f:
                temp = json.load(f)
        else:
            temp = []
        temp.extend(data)
        with open(path, 'w') as f:
            json.dump(temp, f)
    else:
        pass


class PositionalEncoding(nn.Module):
    r"""Inject some information about the relative or absolute position of the tokens
        in the sequence. The positional encodings have the same dimension as
        the embeddings, so that the two can be summed. Here, we use sine and cosine
        functions of different frequencies.
    .. math::
        \text{PosEncoder}(pos, 2i) = sin(pos/10000^(2i/d_model))
        \text{PosEncoder}(pos, 2i+1) = cos(pos/10000^(2i/d_model))
        \text{where pos is the word position and i is the embed idx)
    Args:
        d_model: the embed dim (required).
        dropout: the dropout value (default=0.1).
        max_len: the max. length of the incoming sequence (default=5000).
    Examples:
        >>> pos_encoder = PositionalEncoding(d_model)
    """

    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super(PositionalEncoding, self).__init__()
        if d_model % 2 != 0:
            raise ValueError("Cannot use sin/cos positional encoding with "
                             "odd dim (got dim={:d})".format(d_model))
        self.dropout = nn.Dropout(p=dropout)

        pe = torch.zeros(max_len, d_model)  # [max_len, d_model]
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)  # [max_len,1]
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)

    def forward(self, x, plus=True):
        r"""Inputs of forward function
        Args:
            x: the sequence fed to the positional encoder model (required).
        Shape:
            x: [sequence length, batch size, embed dim]
            output: [sequence length, batch size, embed dim]
        Examples:
            >>> output = pos_encoder(x)
        """
        if plus:
            x = x + self.pe[:x.size(0), :]
            return self.dropout(x)
        else:
            return self.pe[:x.size(0), :]


def load_ca(tar='i', ind=-1):
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    with open('{}/calcu.p'.format(absolute_path), 'rb') as f:
        a = pickle.load(f)
    return a[tar][ind]


class FeedForward(nn.Module):
    def __init__(self, config):
        super().__init__()
        if config.base_model == "LSTM":
            self.in_dim = config.hidden_dim
            self.hidden_dim = config.hidden_dim * 2
        else:
            self.in_dim = config.in_dim
            self.hidden_dim = config.hidden_dim
        self.layer_norm = nn.LayerNorm(self.in_dim, eps=config.eps)
        self.layer_1 = nn.Linear(self.in_dim, self.hidden_dim)
        self.layer_2 = nn.Linear(self.hidden_dim, self.in_dim)
        self.dropout = nn.Dropout(config.dropout)
        ACT2FN = {"gelu": gelu_new, "relu": torch.nn.functional.relu, "swish": silu}
        if isinstance(config.ff_activation, str):
            self.activation_function = ACT2FN[config.ff_activation]
        else:
            self.activation_function = config.ff_activation

    def forward(self, inp):
        output = inp
        output = self.layer_1(output)
        output = self.activation_function(output)
        output = self.dropout(output)
        output = self.layer_2(output)
        output = self.dropout(output)
        output = self.layer_norm(output + inp)
        return output


class MaskedNLLLoss(nn.Module):

    def __init__(self, weight=None):
        super(MaskedNLLLoss, self).__init__()
        self.weight = weight
        self.loss = nn.NLLLoss(weight=weight, reduction='sum')

    def forward(self, pred, target, mask):
        """
        pred -> batch*seq_len, n_classes
        target -> batch*seq_len
        mask -> batch, seq_len
        """
        mask_ = mask.view(-1, 1)  # batch*seq_len, 1
        if type(self.weight) == type(None):
            loss = self.loss(pred * mask_, target) / torch.sum(mask)
        else:
            loss = self.loss(pred * mask_, target) / torch.sum(self.weight[target] * mask_.squeeze())
        return loss


def get_labelsi(target):
    t = target.dataset_name[0].lower()
    m = target.name[1].lower()
    if m == 't':
        ind = 0
    elif m == 'i':
        ind = -1
    else:
        ind = 1
    return t, ind


class MaskedMSELoss(nn.Module):
    def __init__(self):
        super(MaskedMSELoss, self).__init__()
        self.loss = nn.MSELoss(reduction='sum')

    def forward(self, pred, target, mask):
        """
        pred -> batch*seq_len
        target -> batch*seq_len
        mask -> batch*seq_len
        """
        loss = self.loss(pred * mask, target) / torch.sum(mask)
        return loss


class Heat_map():
    def __init__(self, dataset_name='IEMOCAP'):
        if dataset_name == 'IEMOCAP':
            self.classes = ['happiness', 'sadness', 'neutral', 'anger', 'excited', 'frustrated']
        elif dataset_name == 'MELD':
            self.classes = ['neutral', 'surprise', 'fear', 'sadness', 'joy', 'disgust', 'anger']
        elif dataset_name == 'DailyDialog':
            self.classes = ['none', 'anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise']
        else:  # EmoryNLP
            self.classes = ['Joyful', 'Neutral', 'Powerful', 'Mad', 'Sad', 'Scared', 'Peaceful']

    def paint(self, data: np.ndarray, show_data=True, show_colorbar=False):
        '''
        Draw heat maps, which can be used to draw confusion matrices or attention weights
        :param data: np.ndarray, [y_len, x_len],Note that in the heat map, the x-axis extends horizontally to the right,
                and the y-axis extends vertically to the top. Note the correspondence with the elements in ndarray
        :param show_data: Whether to display the corresponding data in the center of the corresponding block
        :param show_colorbar: Whether to draw the heat indicator on the right side of the image
                (i.e. the corresponding scale indicating the value and color)
        :return:
        '''

        plt.imshow(data, cmap=plt.cm.Blues)

        len_y, len_x = data.shape
        indices_x = range(len_x)
        indices_y = range(len_y)

        plt.xticks(indices_x, self.classes)
        plt.yticks(indices_y, self.classes)

        if show_colorbar:
            plt.colorbar()

        plt.xlabel('pred')
        plt.ylabel('label')

        if show_data:
            for index_y in range(len_y):
                for index_x in range(len_x):
                    plt.text(index_x, index_y, data[index_y][index_x], va='center', ha='center')
        plt.show()


def get_labels(res, target=None):
    res = load_ca(*get_labelsi(target))
    count = [sum(i) for i in res]
    labels = []
    preds = []
    for ind, c in enumerate(count):
        labels.extend([ind for i in range(c)])
        for ind_l, l in enumerate(res[ind]):
            preds.extend([ind_l for j in range(l)])
    return labels, preds
