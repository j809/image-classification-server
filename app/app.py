from flask import Flask
from flask import request
import torch
from PIL import Image
from torchvision import transforms
import json
app = Flask(__name__)

@app.route("/predict",methods=["POST"])
def predict():
    model = torch.hub.load('pytorch/vision:v0.4.2', 'densenet121', pretrained=True)
    model.eval()
    filename = request.files['file']
    input_image = Image.open(filename)
    data_preprocessing = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    scores = model(data_preprocessing(input_image).unsqueeze(0))
    class_prob = torch.nn.functional.softmax(scores[0], dim=0)
    class_ids = json.load(open("app/imagenet_class_index.json"))
    labels = [class_ids[str(k)][1] for k in range(len(class_ids))]
    predicted_labels = {}
    count = 1
    for id in class_prob.sort()[1][-10:]:
        predicted_labels[count] = labels[id]
        count += 1
    return predicted_labels

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)