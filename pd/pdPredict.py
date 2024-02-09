from PIL import Image
import requests
from io import BytesIO
from .oct.octModel import model, preprocess_image
import torch
import numpy as np
import matplotlib.pyplot as plt
from random import randint

def url_to_pillow_object(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            return image
        else:
            print(f"Failed to fetch image. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
# import io

# def image_to_stream(image):
#     # Create an in-memory byte stream
#     img_byte_array = io.BytesIO()
    
#     # Save the image to the byte stream
#     image.save(img_byte_array, format='PNG')
    
#     # Rewind the byte stream to the beginning
#     img_byte_array.seek(0)
    
#     return img_byte_array




def predictPd(imgUrl, name, age, sex, country):
    img = url_to_pillow_object(imgUrl)
    if not img:
        return None

    processed_image = preprocess_image(img)
    with torch.no_grad():
        output = model(processed_image)

    pd_percentage = torch.mean(output)
    print(pd_percentage)
    pd_percentage = torch.clamp(pd_percentage, min=0.1, max=0.99)
    has_pd = pd_percentage > 0.4

    segmented_image = output.squeeze().numpy()

    segmented_image_pil = Image.fromarray(
        (segmented_image*255).astype(np.uint8)).convert("L")


    imageFileName = f"images/test{randint(0,10)}.png"
    img = plt.imsave(imageFileName, segmented_image_pil, cmap='gray')
    return has_pd.item(),  pd_percentage.item(), imageFileName

    # return [False, 0.4]


# print(predictPd("https://pdoctretinalstorage.blob.core.windows.net/media/testimages/temp_image_rJEPrso.jpg","dsds",232,"m","india"))
