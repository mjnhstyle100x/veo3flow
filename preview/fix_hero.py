import os
import urllib.request

directory = r"e:\ui-ux-pro-max-skill\preview"
assets_dir = os.path.join(directory, "assets")
target_files = [
    os.path.join(directory, "veo3-flow-landing.html"),
    os.path.join(directory, "index.html")
]

# Download an Unsplash image for BĐS Flycam
img_url = "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=2075&auto=format&fit=crop"
img_path = os.path.join(assets_dir, "bds_flycam.jpg")

try:
    urllib.request.urlretrieve(img_url, img_path)
    print(f"Downloaded BĐS image to {img_path}")
except Exception as e:
    print(f"Failed to download image: {e}")

# HTML Replacements
old_title = '          <h1>Tự Tay Tạo Video AI Bằng <span class="grad">GOOGLE VEO 3</span><br>Chỉ Từ <span class="grad-warm">19.000đ</span></h1>'
new_title = '          <h1>Vũ Khí Chốt Deal: Tạo Video BĐS Với <span class="grad">VEO 3</span><br>Chỉ Từ <span class="grad-warm">19.000đ</span></h1>'

old_bg = "style=\"--bg: url('assets/sapa_drone.jpg')\""
new_bg = "style=\"--bg: url('assets/bds_flycam.jpg')\""

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_title, new_title)
    content = content.replace(old_bg, new_bg)
    
    # Also fix the Prompt card image at the bottom
    content = content.replace('src="assets/sapa_drone.jpg" alt="Flycam phong cảnh Sa Pa từ Google Veo 3"', 'src="assets/bds_flycam.jpg" alt="Flycam dự án Bất động sản từ Google Veo 3"')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Fixed hero title and image successfully.")
