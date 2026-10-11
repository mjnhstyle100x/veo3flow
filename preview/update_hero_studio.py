import os

directory = r"e:\ui-ux-pro-max-skill\preview"
target_files = [
    os.path.join(directory, "veo3-flow-landing.html"),
    os.path.join(directory, "index.html")
]

# HTML Replacements
old_tabs = """          <div class="scene-tabs" role="tablist" aria-label="Chọn mẫu video minh hoạ">
            <button class="scene-tab active" data-scene="0" role="tab" aria-selected="true" type="button">
              <span class="tab-dot"></span>
              <span>🌾 Flycam Sa Pa</span>
            </button>
            <button class="scene-tab" data-scene="1" role="tab" aria-selected="false" type="button">
              <span class="tab-dot"></span>
              <span>🏎️ Tokyo Drift</span>
            </button>
            <button class="scene-tab" data-scene="2" role="tab" aria-selected="false" type="button">
              <span class="tab-dot"></span>
              <span>✨ TVC Nước Hoa</span>
            </button>
          </div>"""

new_tabs = """          <div class="scene-tabs" role="tablist" aria-label="Chọn mẫu video minh hoạ">
            <button class="scene-tab active" data-scene="0" role="tab" aria-selected="true" type="button">
              <span class="tab-dot"></span>
              <span>🏢 Bất Động Sản</span>
            </button>
            <button class="scene-tab" data-scene="1" role="tab" aria-selected="false" type="button">
              <span class="tab-dot"></span>
              <span>👗 Thời Trang</span>
            </button>
            <button class="scene-tab" data-scene="2" role="tab" aria-selected="false" type="button">
              <span class="tab-dot"></span>
              <span>☕ F&B</span>
            </button>
          </div>"""

old_images = """              <div class="cinema-slide active" style="--bg: url('assets/sapa_drone.jpg')">
                <div class="cinema-img ken-burns-1"></div>
                <div class="cinema-overlay"></div>
              </div>
              <div class="cinema-slide" style="--bg: url('assets/cyberpunk_car.jpg')">
                <div class="cinema-img ken-burns-2"></div>
                <div class="cinema-overlay"></div>
              </div>
              <div class="cinema-slide" style="--bg: url('assets/perfume_cinematic.jpg')">
                <div class="cinema-img ken-burns-3"></div>
                <div class="cinema-overlay"></div>
              </div>"""

new_images = """              <div class="cinema-slide active" style="--bg: url('assets/real_estate_penthouse.jpg')">
                <div class="cinema-img ken-burns-1"></div>
                <div class="cinema-overlay"></div>
              </div>
              <div class="cinema-slide" style="--bg: url('assets/fashion_runway_red.jpg')">
                <div class="cinema-img ken-burns-2"></div>
                <div class="cinema-overlay"></div>
              </div>
              <div class="cinema-slide" style="--bg: url('assets/fb_espresso_crema.jpg')">
                <div class="cinema-img ken-burns-3"></div>
                <div class="cinema-overlay"></div>
              </div>"""

old_js = """    const demos = [
      {
        title: 'Flycam Sa Pa',
        text: 'Cinematic 8k aerial drone shot over Sapa terraced rice fields at golden sunrise, morning mist rolling over emerald valleys, sun rays piercing through clouds, slow dolly forward, 24fps filmic…',
        cam: 'CAM: slow aerial dolly'
      },
      {
        title: 'Tokyo Drift',
        text: 'Cinematic tracking shot of Nissan GT-R sports car drifting through neon-lit Shinjuku rain streets at night, wet asphalt puddles reflecting cyan and pink neon signs, shallow depth of field, 24fps…',
        cam: 'CAM: low-angle street tracking'
      },
      {
        title: 'TVC Nước Hoa',
        text: 'Macro commercial shot of luxury perfume bottle "NOIR ÉCLAT" on dark reflective marble surface, fine water droplets, warm golden rim backlight, soft cinematic bokeh, 24fps high-end TVC…',
        cam: 'CAM: macro slow-motion focus'
      }
    ];"""

new_js = """    const demos = [
      {
        title: '🏢 Bất Động Sản',
        text: 'Smooth slow dolly through a luxurious minimalist penthouse living room, premium leather sofa bathed in warm morning sunlight, panoramic city skyline view through floor-to-ceiling windows, 8k…',
        cam: 'CAM: slow architectural dolly'
      },
      {
        title: '👗 Thời Trang',
        text: 'Medium tracking shot of an elegant female supermodel walking down a Paris runway wearing a flowing crimson silk dress, subtle camera flashes from audience, Vogue editorial aesthetic, 4k 60fps…',
        cam: 'CAM: runway tracking'
      },
      {
        title: '☕ F&B',
        text: 'Ultra macro slow motion shot of rich Espresso coffee being poured into a ceramic cup, thick golden-brown crema bubbling, hot steam rising against warm morning sunlight, 4k 120fps…',
        cam: 'CAM: extreme macro slow-mo'
      }
    ];"""

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_tabs, new_tabs)
    content = content.replace(old_images, new_images)
    content = content.replace(old_js, new_js)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated Hero Studio successfully.")
