import os
import glob
import re

directory = r"e:\ui-ux-pro-max-skill\preview"
target_files = [
    os.path.join(directory, "veo3-flow-landing.html"),
    os.path.join(directory, "index.html")
]

widget_html = """
  <!-- Floating Contact Widget -->
  <style>
    .float-contact { position: fixed; bottom: 20px; right: 20px; z-index: 900; display: flex; flex-direction: column; gap: 12px; }
    .float-btn { width: 56px; height: 56px; border-radius: 50%; display: grid; place-items: center; cursor: pointer; box-shadow: 0 10px 24px rgba(0,0,0,0.5); transition: all 0.3s; position: relative; }
    .float-btn:hover { transform: scale(1.1); }
    .float-zalo { background: #0068FF; }
    .float-zalo svg { fill: #fff; width: 34px; height: 34px; }
    .float-pulse { position: absolute; inset: 0; border-radius: 50%; border: 2px solid #0068FF; animation: float-pulse 2s infinite; pointer-events: none; }
    @keyframes float-pulse { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(1.6); opacity: 0; } }
    .float-tooltip { position: absolute; right: 100%; top: 50%; transform: translateY(-50%); margin-right: 14px; background: #111827; border: 1px solid var(--border-strong); padding: 8px 12px; border-radius: 8px; white-space: nowrap; font-size: 0.85rem; font-weight: 600; opacity: 0; pointer-events: none; transition: opacity 0.3s; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
    .float-tooltip::after { content: ''; position: absolute; top: 50%; right: -5px; transform: translateY(-50%); border-width: 5px 0 5px 6px; border-style: solid; border-color: transparent transparent transparent var(--border-strong); }
    .float-btn:hover .float-tooltip { opacity: 1; }
    @media (max-width: 768px) { .float-contact { bottom: 90px; right: 14px; } .float-btn { width: 48px; height: 48px; } .float-zalo svg { width: 28px; height: 28px; } .float-tooltip { display: none; } }
  </style>
  <div class="float-contact">
    <a href="https://zalo.me/0347999726" target="_blank" class="float-btn float-zalo">
      <div class="float-pulse"></div>
      <svg viewBox="0 0 24 24"><path d="M21.406 9.172c0-4.004-3.797-7.25-8.469-7.25S4.469 5.168 4.469 9.172c0 2.508 1.484 4.707 3.738 5.961-.266.973-.781 2.809-.816 2.949-.059.199.074.27.215.18 1.109-.691 3.203-2.074 3.773-2.484.504.07 1.027.109 1.559.109 4.672 0 8.469-3.246 8.469-7.25zM10.156 10.422H8.344a.422.422 0 0 1-.422-.422V7.484c0-.234.188-.422.422-.422h1.813c.234 0 .422.188.422.422v2.516c0 .234-.188.422-.422.422zm3.328 0h-1.812a.422.422 0 0 1-.422-.422V7.484c0-.234.188-.422.422-.422h1.812c.234 0 .422.188.422.422v2.516c0 .234-.188.422-.422.422zm3.328 0h-1.812a.422.422 0 0 1-.422-.422V7.484c0-.234.188-.422.422-.422h1.812c.234 0 .422.188.422.422v2.516c0 .234-.188.422-.422.422z"/></svg>
      <div class="float-tooltip">Hỗ trợ & Mua Hàng 24/7</div>
    </a>
  </div>
</body>"""

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Headings & Title
    content = content.replace("<title>VEO3 FLOW — Học tạo video AI với Google Veo 3 chỉ từ 19.000đ</title>", "<title>XÓA MÙ VIDEO AI — Tạo video bán hàng siêu tốc với Google Veo 3</title>")
    content = content.replace('content="VEO3 FLOW — Tạo video AI với Google Veo 3 chỉ từ 19.000đ"', 'content="XÓA MÙ VIDEO AI — Ứng dụng ngay cho BĐS, Thời trang, Ẩm thực..."')
    
    # 2. Update Logo
    content = content.replace('VEO3 <span style="font-style: italic; font-weight: 400; opacity: 0.9;">FLOW</span>', 'XÓA MÙ <span style="font-style: italic; font-weight: 400; opacity: 0.9;">AI</span>')
    
    # 3. Update Hero
    content = content.replace("Tự Tay Tạo Video AI Bằng <span class=\"grad\">GOOGLE VEO 3</span> Chỉ Từ <span class=\"grad-warm\">19.000đ</span>", "Xóa Mù AI: Tự Tạo Video Đỉnh Cao Bằng <span class=\"grad\">VÀI CLICK CHUỘT</span>")
    
    old_subtitle = "Không cần biết kỹ thuật, không cần thẻ Visa. Xem hướng dẫn từng bước, nhận tài khoản dùng ngay và bộ câu lệnh mẫu để ra video đẹp ngay lần đầu."
    new_subtitle = "Dễ như ăn kẹo! Chỉ cần biết đếm 1, 2, 3 là làm được. Copy & Paste lệnh có sẵn để tạo ngay video 4K sắc nét chốt sale cho <b>Bất Động Sản, Thời Trang, F&B</b>... Không cần cài đặt, dùng được ngay trên điện thoại."
    content = content.replace(old_subtitle, new_subtitle)
    
    # 4. Update Prompts to target niches
    content = content.replace("Phố Đêm Cyberpunk", "Dự Án Bất Động Sản")
    content = content.replace("Flycam bay lượn qua thành phố tương lai rực rỡ ánh đèn neon xanh hồng,", "Flycam quay siêu thực toàn cảnh biệt thự nghỉ dưỡng kính tràn viền lúc hoàng hôn,")
    content = content.replace("Flycam lượn qua thành phố tương lai rực rỡ neon xanh hồng, phản chiếu trên mặt đường ướt mưa, 8k cinematic.", "Flycam lướt qua hồ bơi vô cực tiến vào biệt thự kính hiện đại, ánh sáng ấm cúng, 8k kiến trúc cinematic.")
    
    content = content.replace("Cô Gái Anime", "Review Thời Trang")
    content = content.replace("Chân dung cô gái anime cầm ô đỏ dưới trời tuyết", "Nữ người mẫu chuyên nghiệp mặc váy lụa đỏ đi catwalk tại Paris Fashion Week")
    content = content.replace("Chân dung cô gái anime cầm ô đỏ dưới trời rơi tuyết, ánh sáng ven tóc vàng rực rỡ, bokeh lung linh phía sau.", "Medium shot người mẫu mặc váy lụa thướt tha, sải bước tự tin, đèn flash máy ảnh chớp nháy phía sau, 4k 60fps.")
    
    content = content.replace("Hành Động Ô Tô", "Quảng Cáo F&B")
    content = content.replace("Góc máy sát đất quay bánh xe đua bốc khói mịt mù", "Cận cảnh miếng bò bít tết Wagyu xèo xèo trên chảo gang nóng")
    content = content.replace("Camera bám sát đất theo xe đua thể thao drift tạo đám khói lớn trắng xóa, ánh nắng ngược sáng, chuyển động chậm.", "Extreme macro miếng Wagyu dày đang xèo xèo bốc khói, bơ tan chảy sủi bọt, ánh sáng nhà hàng ấm cúng, 4k macro slow motion.")

    # 5. Add Chat Widget before </body> if not present
    if "class=\"float-contact\"" not in content:
        content = content.replace("</body>", widget_html)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied Marketing fixes successfully.")
