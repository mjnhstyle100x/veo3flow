import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = r"e:\ui-ux-pro-max-skill\preview\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Fonts
FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

f_title = get_font(FONT_BOLD, 34)
f_sub = get_font(FONT_REG, 23)
f_btn = get_font(FONT_BOLD, 24)
f_callout = get_font(FONT_BOLD, 26)
f_callout_sm = get_font(FONT_BOLD, 21)
f_code = get_font(FONT_BOLD, 21)
f_badge = get_font(FONT_BOLD, 18)

W, H = 1200, 675

def draw_browser_chrome(draw, title_text, url_text):
    # Top chrome background
    draw.rectangle([0, 0, W, 80], fill="#070A12")
    draw.line([0, 80, W, 80], fill="#1E293B", width=2)
    # Traffic light dots
    draw.ellipse([24, 34, 38, 48], fill="#EF4444")
    draw.ellipse([46, 34, 60, 48], fill="#F59E0B")
    draw.ellipse([68, 34, 82, 48], fill="#10B981")
    # URL bar
    draw.rounded_rectangle([110, 22, 750, 60], radius=8, fill="#0F172A", outline="#334155", width=1)
    draw.text((125, 28), f"[URL]  {url_text}", font=f_code, fill="#94A3B8")
    # Title badge
    draw.rounded_rectangle([W - 320, 22, W - 20, 60], radius=8, fill="#1E1B4B", outline="#4338CA", width=1)
    draw.text((W - 300, 28), "GOOGLE VEO 3 FLOW", font=f_code, fill="#818CF8")

# ==========================================
# STEP 1: SIGN IN GUIDE
# ==========================================
def create_step1():
    img = Image.new("RGB", (W, H), "#0B0F19")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "Google Flow - Đăng Nhập", "https://labs.google/fx/tools/flow")

    # App header inside page
    draw.rectangle([0, 82, W, 165], fill="#0F172A")
    draw.line([0, 165, W, 165], fill="#1E293B", width=2)
    
    # App Logo
    draw.rounded_rectangle([40, 98, 85, 145], radius=10, fill="#4F46E5")
    draw.text((54, 104), "F", font=get_font(FONT_BOLD, 30), fill="#FFFFFF")
    draw.text((100, 108), "Google Labs", font=f_btn, fill="#F8FAFC")
    draw.text((255, 110), "- VideoFX Flow Studio", font=f_sub, fill="#64748B")

    # SIGN IN BUTTON at top right - widened so text never clips!
    btn_x1, btn_y1, btn_x2, btn_y2 = W - 350, 96, W - 30, 150
    draw.rounded_rectangle([btn_x1, btn_y1, btn_x2, btn_y2], radius=10, fill="#2563EB", outline="#60A5FA", width=2)
    draw.text((btn_x1 + 22, btn_y1 + 13), "Sign In (Đăng Nhập)", font=get_font(FONT_BOLD, 22), fill="#FFFFFF")

    # Red pulsing highlight box around Sign In button
    draw.rounded_rectangle([btn_x1 - 8, btn_y1 - 8, btn_x2 + 8, btn_y2 + 8], radius=14, outline="#EF4444", width=4)

    # Big red arrow pointing up to the button
    draw.line([W - 190, 175, W - 190, 235], fill="#EF4444", width=6)
    draw.polygon([(W - 190, 162), (W - 205, 185), (W - 175, 185)], fill="#EF4444")

    # Callout card
    draw.rounded_rectangle([W - 640, 240, W - 30, 385], radius=14, fill="#1E293B", outline="#EF4444", width=3)
    # Badge inside callout
    draw.rounded_rectangle([W - 620, 255, W - 50, 302], radius=8, fill="#EF4444")
    draw.text((W - 605, 265), "BUOC 1: BAM VAO DAY DE DANG NHAP", font=get_font(FONT_BOLD, 22), fill="#FFFFFF")
    draw.text((W - 610, 325), "Dien Email & Mat khau duoc cap khi mua goi.", font=f_sub, fill="#F1F5F9")

    # Main page mockup illustration
    draw.rounded_rectangle([40, 200, 500, 620], radius=16, fill="#0F172A", outline="#1E293B", width=2)
    draw.text((70, 235), "Chao mung ban den voi Google Flow", font=f_btn, fill="#FFFFFF")
    draw.text((70, 280), "He thong tao video AI dien anh bang mo hinh Veo 3.", font=f_sub, fill="#94A3B8")
    draw.text((70, 335), "[+] Tu dong tao chuyen dong muot ma", font=f_sub, fill="#CBD5E1")
    draw.text((70, 380), "[+] Khoa net khuon mat va san pham", font=f_sub, fill="#CBD5E1")
    draw.text((70, 425), "[+] Xuat video chuan sac net 4K", font=f_sub, fill="#CBD5E1")

    # Helper banner at bottom
    draw.rounded_rectangle([40, 520, 470, 595], radius=10, fill="#1E1B4B", outline="#6366F1", width=1)
    draw.text((60, 545), "Luu y: Nho luu mat khau vao trinh duyet de tien dung!", font=get_font(FONT_REG, 17), fill="#C7D2FE")

    img.save(os.path.join(ASSETS_DIR, "step1_signin.png"), quality=95)
    print("Saved step1_signin.png")

# ==========================================
# STEP 2: ASPECT RATIO GUIDE
# ==========================================
def create_step2():
    img = Image.new("RGB", (W, H), "#0B0F19")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "Google Flow - Chọn Tỉ Lệ", "https://labs.google/fx/tools/flow")

    # Big Header Banner
    draw.rounded_rectangle([40, 100, W - 40, 185], radius=12, fill="#1E293B", outline="#334155", width=2)
    draw.text((65, 115), "BUOC 2: CHON KHUNG HINH (DOC DIEN THOAI HOAC NGANG MAY TINH)", font=f_callout, fill="#38BDF8")
    draw.text((65, 150), "Nhan chuot chon 1 trong 2 nut truoc khi bam tao video:", font=f_sub, fill="#CBD5E1")

    # BOX 1: 9:16 DỌC (TIKTOK)
    b1_x1, b1_y1, b1_x2, b1_y2 = 60, 215, 560, 635
    draw.rounded_rectangle([b1_x1, b1_y1, b1_x2, b1_y2], radius=16, fill="#0F172A", outline="#EF4444", width=3)
    
    # Phone shape inside
    draw.rounded_rectangle([100, 255, 230, 495], radius=16, fill="#1E293B", outline="#64748B", width=2)
    draw.rounded_rectangle([110, 275, 220, 475], radius=10, fill="#000000")
    draw.text((125, 360), "9:16", font=f_btn, fill="#F43F5E")

    draw.text((260, 260), "NUT 1: CHON 9:16", font=get_font(FONT_BOLD, 28), fill="#F43F5E")
    draw.text((260, 310), "Khung hinh DOC", font=f_btn, fill="#FFFFFF")
    draw.text((260, 360), "Phu hop dang:", font=f_sub, fill="#94A3B8")
    draw.text((260, 400), "[+] TikTok Trieu View", font=f_btn, fill="#E2E8F0")
    draw.text((260, 440), "[+] Facebook / Reels", font=f_btn, fill="#E2E8F0")
    draw.text((260, 480), "[+] YouTube Shorts", font=f_btn, fill="#E2E8F0")

    draw.rounded_rectangle([b1_x1 + 30, 545, b1_x2 - 30, 605], radius=10, fill="#EF4444")
    draw.text((b1_x1 + 65, 565), "BAM CHON 9:16 DE LAM VIDEO DOC", font=f_callout_sm, fill="#FFFFFF")

    # BOX 2: 16:9 NGANG (YOUTUBE)
    b2_x1, b2_y1, b2_x2, b2_y2 = 640, 215, 1140, 635
    draw.rounded_rectangle([b2_x1, b2_y1, b2_x2, b2_y2], radius=16, fill="#0F172A", outline="#3B82F6", width=3)

    # Monitor shape inside
    draw.rounded_rectangle([680, 285, 860, 405], radius=10, fill="#000000", outline="#64748B", width=2)
    draw.text((735, 330), "16:9", font=f_btn, fill="#38BDF8")
    draw.rectangle([760, 405, 780, 455], fill="#64748B")
    draw.rectangle([735, 455, 805, 465], fill="#64748B")

    draw.text((890, 260), "NUT 2: CHON 16:9", font=get_font(FONT_BOLD, 28), fill="#38BDF8")
    draw.text((890, 310), "Khung hinh NGANG", font=f_btn, fill="#FFFFFF")
    draw.text((890, 360), "Phu hop dang:", font=f_sub, fill="#94A3B8")
    draw.text((890, 400), "[+] YouTube Phim Dai", font=f_btn, fill="#E2E8F0")
    draw.text((890, 440), "[+] Man hinh Tivi / Laptop", font=f_btn, fill="#E2E8F0")
    draw.text((890, 480), "[+] Trinh chieu quang cao", font=f_btn, fill="#E2E8F0")

    draw.rounded_rectangle([b2_x1 + 30, 545, b2_x2 - 30, 605], radius=10, fill="#2563EB")
    draw.text((b2_x1 + 55, 565), "BAM CHON 16:9 DE LAM VIDEO NGANG", font=f_callout_sm, fill="#FFFFFF")

    img.save(os.path.join(ASSETS_DIR, "step2_aspect_ratio.png"), quality=95)
    print("Saved step2_aspect_ratio.png")

# ==========================================
# STEP 3: PROMPT & GENERATE GUIDE
# ==========================================
def create_step3():
    img = Image.new("RGB", (W, H), "#0B0F19")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "Google Flow - Nhập Lệnh & Tạo", "https://labs.google/fx/tools/flow")

    # Header Card
    draw.rounded_rectangle([40, 100, W - 40, 175], radius=12, fill="#1E293B", outline="#334155", width=2)
    draw.text((65, 115), "BUOC 3: DAN CAU LENH VA BAM NUT MAU TIM DE TAO VIDEO", font=f_callout, fill="#A855F7")
    draw.text((65, 145), "Dan cau lenh tieng Anh vao o duoi roi bam nut Generate ben phai:", font=f_sub, fill="#CBD5E1")

    # Studio Mockup Background (empty canvas)
    draw.rounded_rectangle([40, 195, W - 40, 455], radius=16, fill="#05070E", outline="#1E293B", width=2)
    draw.text((W//2 - 240, 305), "[Khung hinh video se hien ra tai day sau khi may tao xong]", font=f_btn, fill="#475569")

    # PROMPT DOCK AT BOTTOM
    dock_y1 = 475
    draw.rounded_rectangle([40, dock_y1, W - 40, 645], radius=16, fill="#0F172A", outline="#4F46E5", width=2)

    # 1. Prompt Input Bar
    p_x1, p_y1, p_x2, p_y2 = 60, dock_y1 + 45, W - 340, dock_y1 + 120
    draw.rounded_rectangle([p_x1, p_y1, p_x2, p_y2], radius=10, fill="#000000", outline="#EF4444", width=3)
    draw.text((p_x1 + 18, p_y1 + 12), "PROMPT (O nhap lenh):", font=get_font(FONT_BOLD, 17), fill="#38BDF8")
    draw.text((p_x1 + 18, p_y1 + 40), "Close-up shot of a luxury perfume bottle, cinematic lighting, 4k 60fps...", font=f_sub, fill="#F8FAFC")

    # Callout for Prompt Input
    draw.rounded_rectangle([60, dock_y1 - 65, 460, dock_y1 - 10], radius=8, fill="#EF4444")
    draw.text((80, dock_y1 - 55), "1. DAN CAU LENH VAO O NAY", font=f_callout_sm, fill="#FFFFFF")
    draw.polygon([(200, dock_y1 - 10), (220, dock_y1 + 15), (240, dock_y1 - 10)], fill="#EF4444")

    # 2. Big Purple Generate Button
    g_x1, g_y1, g_x2, g_y2 = W - 320, dock_y1 + 40, W - 60, dock_y1 + 125
    draw.rounded_rectangle([g_x1, g_y1, g_x2, g_y2], radius=12, fill="#7C3AED", outline="#A855F7", width=2)
    draw.text((g_x1 + 25, g_y1 + 28), "GENERATE VIDEO", font=f_btn, fill="#FFFFFF")

    # Red border & Callout for Generate Button
    draw.rounded_rectangle([g_x1 - 6, g_y1 - 6, g_x2 + 6, g_y2 + 6], radius=16, outline="#EF4444", width=4)
    draw.rounded_rectangle([W - 480, dock_y1 - 65, W - 60, dock_y1 - 10], radius=8, fill="#EF4444")
    draw.text((W - 460, dock_y1 - 55), "2. BAM NUT NAY -> DOI KHOANG 60s", font=f_callout_sm, fill="#FFFFFF")
    draw.polygon([(W - 190, dock_y1 - 10), (W - 170, dock_y1 + 15), (W - 150, dock_y1 - 10)], fill="#EF4444")

    img.save(os.path.join(ASSETS_DIR, "step3_prompt_generate.png"), quality=95)
    print("Saved step3_prompt_generate.png")

# ==========================================
# STEP 4: DOWNLOAD & EXTEND GUIDE
# ==========================================
def create_step4():
    # Load real generated perfume image as the background canvas!
    perfume_path = os.path.join(ASSETS_DIR, "perfume_cinematic.jpg")
    if os.path.exists(perfume_path):
        bg = Image.open(perfume_path).resize((W, H))
    else:
        bg = Image.new("RGB", (W, H), "#0B0F19")

    # Dark overlay to keep text super readable
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 110))
    bg.paste(overlay, (0, 0), overlay)

    draw = ImageDraw.Draw(bg)
    draw_browser_chrome(draw, "Google Flow - Video Hoàn Tất", "https://labs.google/fx/tools/flow")

    # Success Top Badge
    draw.rounded_rectangle([40, 100, 360, 155], radius=10, fill="#065F46", outline="#34D399", width=2)
    draw.text((60, 115), "[OK] VIDEO TAO XONG 100%!", font=f_callout_sm, fill="#A7F3D0")

    # ACTIONS AT TOP RIGHT OF VIDEO
    # 1. Extend Button
    ext_x1, ext_y1, ext_x2, ext_y2 = W - 530, 95, W - 320, 155
    draw.rounded_rectangle([ext_x1, ext_y1, ext_x2, ext_y2], radius=10, fill="#1E293B", outline="#F59E0B", width=3)
    draw.text((ext_x1 + 18, ext_y1 + 14), "[+] Extend (+5s)", font=f_code, fill="#FCD34D")

    # Callout for Extend
    draw.rounded_rectangle([W - 610, 175, W - 250, 245], radius=8, fill="#F59E0B")
    draw.text((W - 595, 185), "MEO: BAM DAY DE NOI DAI VIDEO", font=get_font(FONT_BOLD, 18), fill="#000000")
    draw.text((W - 595, 212), "(Tu dong ve them 5 giay hanh dong tiep)", font=get_font(FONT_REG, 15), fill="#000000")
    draw.polygon([(W - 425, 175), (W - 415, 158), (W - 405, 175)], fill="#F59E0B")

    # 2. Download Button
    dl_x1, dl_y1, dl_x2, dl_y2 = W - 290, 95, W - 40, 155
    draw.rounded_rectangle([dl_x1, dl_y1, dl_x2, dl_y2], radius=12, fill="#10B981", outline="#FFFFFF", width=3)
    draw.text((dl_x1 + 25, dl_y1 + 16), "Download 4K", font=f_btn, fill="#FFFFFF")

    # Big Red Highlight for Download Button
    draw.rounded_rectangle([dl_x1 - 6, dl_y1 - 6, dl_x2 + 6, dl_y2 + 6], radius=16, outline="#EF4444", width=4)

    # Big Callout for Download
    draw.rounded_rectangle([W - 560, 270, W - 40, 385], radius=12, fill="#0F172A", outline="#EF4444", width=3)
    draw.text((W - 535, 285), "BUOC 4: BAM VAO DAY DE TAI VE!", font=f_callout, fill="#FCA5A5")
    draw.text((W - 535, 330), "Luu file video mp4 goc 4K ve may tinh/dt.", font=f_sub, fill="#F1F5F9")
    draw.line([W - 165, 165, W - 165, 268], fill="#EF4444", width=6)
    draw.polygon([(W - 165, 160), (W - 178, 185), (W - 152, 185)], fill="#EF4444")

    # Player controls at bottom
    draw.rounded_rectangle([40, H - 90, W - 40, H - 30], radius=12, fill="#0F172A", outline="#334155", width=1)
    draw.text((70, H - 72), "[>] DANG PHAT: 00:04 / 00:08", font=f_code, fill="#E2E8F0")
    draw.rounded_rectangle([390, H - 65, W - 200, H - 55], radius=5, fill="#334155")
    draw.rounded_rectangle([390, H - 65, 760, H - 55], radius=5, fill="#22D3EE")
    draw.text((W - 170, H - 72), "Lap lai: BAT", font=f_code, fill="#22D3EE")

    bg.save(os.path.join(ASSETS_DIR, "step4_download.png"), quality=95)
    print("Saved step4_download.png")

if __name__ == "__main__":
    create_step1()
    create_step2()
    create_step3()
    create_step4()
    print("All 4 step images generated successfully without glyph errors!")
