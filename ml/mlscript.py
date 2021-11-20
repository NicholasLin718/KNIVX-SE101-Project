import torch
import torchvision
from torchvision import transforms, datasets
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
from pathlib import Path
from PIL import Image

classes = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','del',
           'nothing', 'space']
num_classes=29
class ASLTestDataset(torch.utils.data.Dataset):
    def __init__(self, root_path, transforms=None):
        super().__init__()
        
        self.transforms = transforms
        self.imgs = sorted(list(Path(root_path).glob('*.jpg')))
        
    def __len__(self):
        return len(self.imgs)
    
    def __getitem__(self, idx):
        img_path = self.imgs[idx]
        img = Image.open(img_path).convert('RGB')
        
        label = img_path.parts[-1].split('_')[0]
        if self.transforms:
            img = self.transforms(img)
        
        return img, label

test_transforms = transforms.Compose([
    transforms.Resize(224), 
    transforms.ToTensor()
])




def predict(demo_data_path):
    demo_dataset = ASLTestDataset(demo_data_path, transforms=test_transforms)

    model = torchvision.models.resnet50(pretrained=False)
    in_features = model.fc.in_features
    model.fc = torch.nn.Linear(in_features, num_classes)

    model.load_state_dict(torch.load('model!', map_location=torch.device('cpu')))
    prediction = []
    for img, label in demo_dataset:
        img = torch.Tensor(img)
        img = img.to(device)
        model.eval()
        pred = model(img[None])
        
        prediction.append(classes[torch.max(pred, dim=1)[1]])
    return prediction
