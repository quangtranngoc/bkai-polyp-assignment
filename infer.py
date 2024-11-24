import sys
import torch
from PIL import Image
import torch.nn.functional as F
from torchvision.transforms import Resize, PILToTensor, ToPILImage, Compose, InterpolationMode
import segmentation_models_pytorch as smp

def main(img_path, to_path):
    model = smp.UnetPlusPlus(encoder_name="resnet34", encoder_weights="imagenet", in_channels=3, classes=3)
    model.load_state_dict(torch.load("model/unet.pth", map_location=torch.device("cpu"), weights_only=True))
    transform = Compose([Resize((256, 256), interpolation=InterpolationMode.BILINEAR),PILToTensor()])
    
    img = Image.open(img_path)
    data = transform(img).to(torch.float32).unsqueeze(0)
    
    with torch.no_grad():
        predicted_mask = model(data)
        
    resize = Resize((img.size[1], img.size[0]), interpolation=InterpolationMode.NEAREST)
    final_mask = F.one_hot(torch.argmax(predicted_mask[0], 0)).permute(2, 0, 1).float()
    final_mask[2, :, :] = 0
    mask2img = resize(ToPILImage()(final_mask))
    
    mask2img.save(to_path)
    
if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Expect 2 agruments, got {}".format(len(sys.argv) - 1))