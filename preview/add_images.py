import os
import shutil

# Paths
brain_dir = r"C:\Users\Admin\.gemini\antigravity-ide\brain\ae5b4bbc-9134-4b5c-8d72-1101953fa233"
assets_dir = r"e:\ui-ux-pro-max-skill\preview\assets"
target_files = [
    r"e:\ui-ux-pro-max-skill\preview\huong-dan-veo3-flow.html",
    r"e:\ui-ux-pro-max-skill\preview\huong-dan-vip-149k.html"
]

images = {
    "real_estate_penthouse_1791474136816.jpg": "real_estate_penthouse.jpg",
    "fashion_runway_red_1791474161865.jpg": "fashion_runway_red.jpg",
    "fb_espresso_crema_1791474187114.jpg": "fb_espresso_crema.jpg"
}

# Ensure assets dir exists
os.makedirs(assets_dir, exist_ok=True)

# Copy files
for src, dst in images.items():
    src_path = os.path.join(brain_dir, src)
    dst_path = os.path.join(assets_dir, dst)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
    else:
        print(f"Warning: {src_path} not found.")

# HTML modifications for huong-dan-veo3-flow.html
with open(target_files[0], 'r', encoding='utf-8') as f:
    content = f.read()

# Update PROMPT 3 image
content = content.replace('src="assets/cyberpunk_car.jpg"', 'src="assets/real_estate_penthouse.jpg"')

# Inject for PROMPT 6
fashion_media = """
        <div class="prompt-card-media">
          <img class="prompt-card-img" src="assets/fashion_runway_red.jpg" alt="Người mẫu thời trang trên sàn diễn từ Google Veo 3" loading="lazy">
          <div class="prompt-card-badge"><span class="dot"></span> THÀNH PHẨM THỰC TẾ · GOOGLE VEO 3 4K</div>
        </div>
        <div class="prompt-card-body">"""
content = content.replace('<!-- PROMPT 6: Fashion Runway -->\n      <div class="prompt-card">\n        <div class="prompt-card-body">', f'<!-- PROMPT 6: Fashion Runway -->\n      <div class="prompt-card">{fashion_media}')

# Inject for PROMPT 10
fb_media = """
        <div class="prompt-card-media">
          <img class="prompt-card-img" src="assets/fb_espresso_crema.jpg" alt="Ly Espresso siêu nét từ Google Veo 3" loading="lazy">
          <div class="prompt-card-badge"><span class="dot"></span> THÀNH PHẨM THỰC TẾ · GOOGLE VEO 3 4K</div>
        </div>
        <div class="prompt-card-body">"""
content = content.replace('<!-- PROMPT 10: Review F&B -->\n      <div class="prompt-card">\n        <div class="prompt-card-body">', f'<!-- PROMPT 10: Review F&B -->\n      <div class="prompt-card">{fb_media}')
content = content.replace('<!-- PROMPT 10: Nature Macro -->\n      <div class="prompt-card">\n        <div class="prompt-card-body">', f'<!-- PROMPT 10: Nature Macro -->\n      <div class="prompt-card">{fb_media}')

with open(target_files[0], 'w', encoding='utf-8') as f:
    f.write(content)

# For VIP guide
with open(target_files[1], 'r', encoding='utf-8') as f:
    vip_content = f.read()

vip_content = vip_content.replace('src="assets/cyberpunk_car.jpg"', 'src="assets/real_estate_penthouse.jpg"')

# Inject for KICH BAN 06
vip_content = vip_content.replace('<!-- KỊCH BẢN 06: Fashion Runway -->\n      <div class="prompt-card">\n        <div class="prompt-card-body">', f'<!-- KỊCH BẢN 06: Fashion Runway -->\n      <div class="prompt-card">{fashion_media}')

# Inject for KICH BAN 10
vip_content = vip_content.replace('<!-- KỊCH BẢN 10: Lotus Healing Macro -->\n      <div class="prompt-card">\n        <div class="prompt-card-body">', f'<!-- KỊCH BẢN 10: Lotus Healing Macro -->\n      <div class="prompt-card">{fb_media}')

with open(target_files[1], 'w', encoding='utf-8') as f:
    f.write(vip_content)

print("Images copied and HTML updated.")
