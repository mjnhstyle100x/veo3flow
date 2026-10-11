import os

directory = r"e:\ui-ux-pro-max-skill\preview"
target_files = [
    os.path.join(directory, "veo3-flow-landing.html"),
    os.path.join(directory, "index.html")
]

old_js_text = "Cinematic 8k aerial drone shot over beautiful green valleys and land plots at golden sunrise, morning mist rolling over emerald hills, sun rays piercing through clouds, slow dolly forward, 24fps filmic…"
new_js_text = "Cinematic 8k aerial drone shot flying over a luxury modern coastal villa with a swimming pool, minimalist white architecture, bright sunny day, real estate commercial photography, slow dolly forward, 4k 60fps…"

old_tab_name = "🚁 Flycam Đất Nền"
new_tab_name = "🚁 Flycam Biệt Thự"

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_js_text, new_js_text)
    content = content.replace(old_tab_name, new_tab_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated JS prompt and tab name successfully.")
