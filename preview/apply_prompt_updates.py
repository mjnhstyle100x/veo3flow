import os

directory = r"e:\ui-ux-pro-max-skill\preview"
target_files = [
    os.path.join(directory, "huong-dan-veo3-flow.html"),
    os.path.join(directory, "huong-dan-vip-149k.html"),
    os.path.join(directory, "huong-dan-co-ban.html")
]

replacements = {
    "Cyberpunk Car": "Nội Thất & Kiến Trúc",
    "Góc máy bám sát mặt đường, bánh xe đua bốc khói mịt mù, drift cực gắt qua ngã tư ngập ánh đèn neon rực rỡ, hạt mưa bắn tung tóe lên ống kính.": "Máy quay lướt chậm qua phòng khách thiết kế phong cách Minimalism sang trọng, sofa da rọi nắng ban mai, rèm cửa lụa mỏng bay nhẹ, tầm nhìn toàn cảnh thành phố qua cửa kính lớn.",
    "Low angle tracking shot chasing a drift car's tires smoking heavily, sharp drift through a neon-lit cyberpunk intersection, rain droplets splashing on the camera lens, 8k cinematic.": "Smooth slow dolly through a luxurious minimalist penthouse living room, premium leather sofa bathed in warm morning sunlight, sheer silk curtains blowing gently, panoramic city skyline view through floor-to-ceiling windows, architectural photography, 4k 60fps.",

    "3D Pixar Animation": "Thẩm Mỹ & Spa",
    "Cận cảnh một chú mèo con lông xù kiểu 3D hoạt hình Pixar, đôi mắt to tròn long lanh ngước nhìn quả bóng len đang lăn. Ánh sáng mềm mại, màu sắc tươi sáng.": "Góc quay cận cảnh bàn tay mềm mại đang massage bằng tinh dầu và đá nóng trên lưng, sương mỏng lơ lửng, hoa lan hồ điệp trắng rung rinh, ánh sáng vàng ấm áp tạo cảm giác thư giãn tuyệt đối.",
    "Extreme close-up of a fluffy 3D Pixar-style animated kitten, big glassy eyes looking up at a rolling yarn ball. Soft studio lighting, vibrant colors, 4k render.": "Extreme close-up shot of soft hands massaging hot stones with essential oils on a back, gentle mist floating in the air, white phalaenopsis orchids trembling slightly, warm golden healing light, tranquil spa atmosphere, cinematic macro video, 4k.",

    "FPV Action Drone": "Trang Sức Cao Cấp",
    "Góc nhìn thứ nhất (FPV) từ một chiếc drone bay xuyên qua một tòa nhà bỏ hoang, len lỏi qua các khung cửa sổ vỡ, khói bụi mịt mù, rượt đuổi theo một bóng người đang chạy trốn.": "Cận cảnh tuyệt đẹp chiếc nhẫn kim cương 2 carat phản chiếu ánh sáng lấp lánh như cầu vồng, nằm kiêu hãnh trên lớp nhung đỏ đô. Camera xoay tròn chậm khoe trọn từng giác cắt tinh xảo.",
    "Fast FPV drone POV flying through an abandoned warehouse, weaving through broken windows, dusty atmosphere, chasing a hooded figure running away, intense motion blur, 4k 60fps.": "Stunning macro shot of a 2-carat diamond engagement ring sparkling with rainbow light reflections, resting proudly on deep burgundy velvet. Smooth slow circular camera orbit revealing intricate diamond cuts, premium jewelry commercial lighting, 8k resolution.",

    "Nature Macro": "Review F&B",
    "Cận cảnh siêu sắc nét một giọt sương mai rớt từ mép lá sen xuống mặt hồ tĩnh lặng, tạo ra những gợn sóng hoàn hảo, bắt sáng lấp lánh như pha lê.": "Cận cảnh siêu sắc nét ly cà phê Espresso đang được rót từ máy pha, lớp crema màu nâu vàng óng ả sủi bọt, hơi nóng bốc lên nghi ngút trong ánh sáng ban mai.",
    "Ultra macro shot of a perfect morning dewdrop falling from a lotus leaf into a still pond, creating perfect ripples, catching the light like a crystal, 1000fps slow motion, 8k.": "Ultra macro shot of rich Espresso coffee being poured from a portafilter into a ceramic cup, thick golden-brown crema bubbling, hot steam rising against warm morning sunlight, commercial food photography, 4k 120fps slow motion."
}

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated Guide Prompts successfully.")
