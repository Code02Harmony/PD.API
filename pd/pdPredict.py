from PIL import Image
import requests
from io import BytesIO

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

# Example usage
url = "https://example.com/image.jpg"
pillow_image = url_to_pillow_object(url)

if pillow_image:
    # Now you can work with the Pillow image object
    pillow_image.show()



def predictPd(data):
    imgUrl = data["retinalScan"]
    name = data["name"]
    age = data["age"]
    sex = data["sex"]
    country = data["country"]

    img = url_to_pillow_object(imgUrl)

    if not img:
        return None
    
    print(img)

    # Predict Using ML model


    return [False,0.4]