import torch


def test_model():
    with open('tests/model_best.model', 'rb') as f:
        model = torch.load(f, map_location=torch.device('cpu'))
        print(model)
        model('hello')
