import os
import urllib.request

directory = r"e:\ui-ux-pro-max-skill\preview"
assets_dir = os.path.join(directory, "assets")

img_url = "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=2075&auto=format&fit=crop"
img_path = os.path.join(assets_dir, "bds_flycam.jpg")

try:
    urllib.request.urlretrieve(img_url, img_path)
    print("Downloaded image successfully.")
except Exception as e:
    print(f"Failed to download image: {e}")
