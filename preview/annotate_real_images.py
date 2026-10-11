import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = r"e:\ui-ux-pro-max-skill\preview\assets"
FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

f_tag = get_font(FONT_BOLD, 18)
f_desc = get_font(FONT_REG, 15)
f_sub = get_font(FONT_BOLD, 14)

def draw_callout_box(draw, box, text_lines, bg="#EF4444", text_color="#FFFFFF"):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle([x1, y1, x2, y2], radius=8, fill=bg, outline="#FFFFFF", width=2)
    # text
    cur_y = y1 + 8
    for line, font in text_lines:
        draw.text((x1 + 14, cur_y), line, font=font, fill=text_color)
        cur_y += 24

# ==========================================
# 1. STEP 1: HOME PAGE -> "Tạo bằng Google Flow"
# ==========================================
def annotate_step1():
    img = Image.open(os.path.join(ASSETS_DIR, "real_step1_home.png")).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # Button "Tao bang Google Flow" around x: 395, y: 350 to x: 625, y: 405
    bx1, by1, bx2, by2 = 390, 350, 630, 410
    draw.rounded_rectangle([bx1 - 4, by1 - 4, bx2 + 4, by2 + 4], radius=30, outline="#EF4444", width=4)
    
    # Arrow from top
    draw.line([510, 245, 510, 340], fill="#EF4444", width=5)
    draw.polygon([(510, 348), (498, 328), (522, 328)], fill="#EF4444")
    
    # Callout card
    draw_callout_box(draw, [320, 160, 700, 240], [
        ("BUOC 1: BAM VAO NUT NAY DE BAT DAU", f_tag),
        ("Nut 'Tao bang Google Flow' ngay giua man hinh", f_desc)
    ])
    
    img.save(os.path.join(ASSETS_DIR, "guide_step1_home.png"), quality=95)
    print("Saved guide_step1_home.png")

# ==========================================
# 2. STEP 2: GOOGLE SIGN IN
# ==========================================
def annotate_step2():
    img = Image.open(os.path.join(ASSETS_DIR, "real_step2_login.png")).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # Email input box around x: 525, y: 160 to x: 850, y: 215
    ix1, iy1, ix2, iy2 = 525, 160, 850, 215
    draw.rounded_rectangle([ix1 - 4, iy1 - 4, ix2 + 4, iy2 + 4], radius=6, outline="#EF4444", width=4)
    
    # Next button around x: 760, y: 330 to x: 850, y: 368
    nx1, ny1, nx2, ny2 = 760, 330, 850, 368
    draw.rounded_rectangle([nx1 - 3, ny1 - 3, nx2 + 3, ny2 + 3], radius=20, outline="#22C55E", width=4)
    
    # Callout for Email
    draw_callout_box(draw, [140, 145, 480, 230], [
        ("BUOC 2A: DIEN EMAIL DUOC CAP", f_tag),
        ("Nhap dia chi Gmail vao o mau xanh nay", f_desc)
    ])
    draw.line([482, 185, 518, 185], fill="#EF4444", width=4)
    draw.polygon([(522, 185), (510, 177), (510, 193)], fill="#EF4444")
    
    # Callout for Next button
    draw_callout_box(draw, [480, 310, 740, 385], [
        ("BUOC 2B: BAM 'TIEP THEO'", f_tag),
        ("Sau do dien Mat khau de vao tool", f_desc)
    ], bg="#16A34A")
    draw.line([742, 348, 755, 348], fill="#16A34A", width=4)
    draw.polygon([(758, 348), (748, 340), (748, 356)], fill="#16A34A")
    
    img.save(os.path.join(ASSETS_DIR, "guide_step2_login.png"), quality=95)
    print("Saved guide_step2_login.png")

# ==========================================
# 3. STEP 3: NEW PROJECT BUTTON
# ==========================================
def annotate_step3():
    img = Image.open(os.path.join(ASSETS_DIR, "real_step3_new_project.png")).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # Button "+ Du an moi" around x: 435, y: 320 to x: 585, y: 410
    px1, py1, px2, py2 = 435, 320, 585, 410
    draw.rounded_rectangle([px1 - 4, py1 - 4, px2 + 4, py2 + 4], radius=16, outline="#EF4444", width=4)
    
    # Arrow from top
    draw.line([510, 220, 510, 310], fill="#EF4444", width=5)
    draw.polygon([(510, 316), (498, 296), (522, 296)], fill="#EF4444")
    
    # Callout card
    draw_callout_box(draw, [310, 130, 710, 215], [
        ("BUOC 3: BAM VAO '+ DU AN MOI'", f_tag),
        ("De mo phong lam viec va bat dau sang tao", f_desc)
    ])
    
    img.save(os.path.join(ASSETS_DIR, "guide_step3_new_project.png"), quality=95)
    print("Saved guide_step3_new_project.png")

# ==========================================
# 4. STEP 4: ASPECT RATIO (9:16 & 16:9)
# ==========================================
def annotate_step4():
    img = Image.open(os.path.join(ASSETS_DIR, "real_step4_aspect_ratio.png")).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # Button 9:16 (Doc TikTok) around x: 575, y: 275 to x: 685, y: 310
    r916_x1, r916_y1, r916_x2, r916_y2 = 575, 275, 685, 310
    draw.rounded_rectangle([r916_x1 - 3, r916_y1 - 3, r916_x2 + 3, r916_y2 + 3], radius=8, outline="#EF4444", width=3)
    
    # Button 16:9 (Ngang YouTube) around x: 465, y: 275 to x: 570, y: 310
    r169_x1, r169_y1, r169_x2, r169_y2 = 465, 275, 570, 310
    draw.rounded_rectangle([r169_x1 - 3, r169_y1 - 3, r169_x2 + 3, r169_y2 + 3], radius=8, outline="#3B82F6", width=3)
    
    # Callout for 9:16 on the right
    draw_callout_box(draw, [710, 250, 1000, 335], [
        ("CHON 9:16: LAM VIDEO DOC", f_tag),
        ("Dang TikTok, Facebook Reels, Shorts", f_desc)
    ], bg="#EF4444")
    draw.line([708, 292, 690, 292], fill="#EF4444", width=3)
    draw.polygon([(688, 292), (696, 286), (696, 298)], fill="#EF4444")

    # Callout for 16:9 on the left
    draw_callout_box(draw, [130, 250, 440, 335], [
        ("CHON 16:9: LAM VIDEO NGANG", f_tag),
        ("Xem man hinh may tinh, YouTube, Tivi", f_desc)
    ], bg="#2563EB")
    draw.line([442, 292, 460, 292], fill="#2563EB", width=3)
    draw.polygon([(462, 292), (454, 286), (454, 298)], fill="#2563EB")
    
    img.save(os.path.join(ASSETS_DIR, "guide_step4_aspect_ratio.png"), quality=95)
    print("Saved guide_step4_aspect_ratio.png")

# ==========================================
# 5. STEP 5: PROMPT INPUT & GENERATE
# ==========================================
def annotate_step5():
    img = Image.open(os.path.join(ASSETS_DIR, "real_step5_prompt_input.png")).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # Prompt dock at bottom around x: 275, y: 360 to x: 730, y: 430
    px1, py1, px2, py2 = 275, 360, 680, 430
    draw.rounded_rectangle([px1 - 4, py1 - 4, px2 + 4, py2 + 4], radius=16, outline="#EF4444", width=3)
    
    # Generate button (arrow) at right of dock: x: 690, y: 395 to x: 725, y: 430
    gx1, gy1, gx2, gy2 = 690, 395, 725, 430
    draw.rounded_rectangle([gx1 - 3, gy1 - 3, gx2 + 3, gy2 + 3], radius=18, outline="#A855F7", width=4)
    
    # Callout for Prompt Input (top left)
    draw_callout_box(draw, [180, 260, 600, 335], [
        ("BUOC 5A: DAN CAU LENH VAO O NAY", f_tag),
        ("O co chu 'Ban muon tao nhung gi?'", f_desc)
    ], bg="#EF4444")
    draw.line([390, 336, 390, 355], fill="#EF4444", width=3)
    draw.polygon([(390, 358), (384, 348), (396, 348)], fill="#EF4444")
    
    # Callout for Generate Button (top right)
    draw_callout_box(draw, [630, 310, 990, 385], [
        ("BUOC 5B: BAM NUT MUI TEN DE TAO!", f_tag),
        ("Cho he thong AI ve video ~60-90s", f_desc)
    ], bg="#7C3AED")
    draw.line([710, 386, 710, 392], fill="#7C3AED", width=3)
    draw.polygon([(710, 394), (704, 386), (716, 386)], fill="#7C3AED")
    
    img.save(os.path.join(ASSETS_DIR, "guide_step5_prompt_input.png"), quality=95)
    print("Saved guide_step5_prompt_input.png")

# ==========================================
# 6. STEP 6: DOWNLOAD VIDEO
# ==========================================
def annotate_step6():
    img = Image.open(os.path.join(ASSETS_DIR, "real_step6_download_video.png")).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # Submenu Download 720p & 1080p around x: 705, y: 235 to x: 885, y: 335
    dx1, dy1, dx2, dy2 = 705, 235, 885, 335
    draw.rounded_rectangle([dx1 - 4, dy1 - 4, dx2 + 4, dy2 + 4], radius=12, outline="#10B981", width=4)
    
    # Callout pointing to 720p / 1080p
    draw_callout_box(draw, [280, 240, 680, 325], [
        ("BUOC 6: CHON 'TAI XUONG' -> 1080P", f_tag),
        ("Bam chuot vao 720p hoac 1080p de luu video ve may", f_desc)
    ], bg="#059669")
    draw.line([682, 285, 700, 285], fill="#059669", width=4)
    draw.polygon([(704, 285), (694, 277), (694, 293)], fill="#059669")
    
    img.save(os.path.join(ASSETS_DIR, "guide_step6_download.png"), quality=95)
    print("Saved guide_step6_download.png")

if __name__ == "__main__":
    annotate_step1()
    annotate_step2()
    annotate_step3()
    annotate_step4()
    annotate_step5()
    annotate_step6()
    print("ALL 6 REAL SCREENSHOTS ANNOTATED SUCCESSFULLY!")
