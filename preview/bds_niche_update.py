import os
import re

directory = r"e:\ui-ux-pro-max-skill\preview"
target_files = [
    os.path.join(directory, "veo3-flow-landing.html"),
    os.path.join(directory, "index.html")
]

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Title & Meta
    content = content.replace("<title>XÓA MÙ VIDEO AI — Tạo video bán hàng siêu tốc với Google Veo 3</title>", "<title>VŨ KHÍ CHỐT DEAL — Tạo video BĐS với Google Veo 3 chỉ từ 19.000đ</title>")
    content = content.replace('content="XÓA MÙ VIDEO AI — Ứng dụng ngay cho BĐS, Thời trang, Ẩm thực..."', 'content="Vũ khí chốt deal cho Môi giới BĐS: Tự tạo video Flycam, kiến trúc nội thất siêu thực bằng Google Veo 3. Không cần thuê đội media."')

    # 2. Logo
    content = content.replace('XÓA MÙ <span style="font-style: italic; font-weight: 400; opacity: 0.9;">AI</span>', 'AI CHO <span style="font-style: italic; font-weight: 400; opacity: 0.9;">BĐS</span>')

    # 3. Hero
    content = content.replace("Xóa Mù AI: Tự Tạo Video Đỉnh Cao Bằng <span class=\"grad\">VÀI CLICK CHUỘT</span>", "Vũ Khí Chốt Deal: Tự Tạo Video Bất Động Sản Siêu Thực Chỉ Bằng <span class=\"grad\">VÀI CLICK</span>")
    old_sub = "Dễ như ăn kẹo! Chỉ cần biết đếm 1, 2, 3 là làm được. Copy & Paste lệnh có sẵn để tạo ngay video 4K sắc nét chốt sale cho <b>Bất Động Sản, Thời Trang, F&B</b>... Không cần cài đặt, dùng được ngay trên điện thoại."
    new_sub = "Không cần thuê đội bay Flycam hay quay dựng đắt đỏ. Chỉ cần Copy & Paste lệnh có sẵn để tạo ngay video 4K quay toàn cảnh dự án, nội thất sang trọng. Tự tay làm video chuyên nghiệp gửi khách VIP chốt sale ngay trên điện thoại."
    content = content.replace(old_sub, new_sub)

    # 4. Studio Tabs
    old_tabs = """          <div class="scene-tabs" role="tablist" aria-label="Chọn mẫu video minh hoạ">
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
    new_tabs = """          <div class="scene-tabs" role="tablist" aria-label="Chọn mẫu video minh hoạ">
            <button class="scene-tab active" data-scene="0" role="tab" aria-selected="true" type="button">
              <span class="tab-dot"></span>
              <span>🚁 Flycam Đất Nền</span>
            </button>
            <button class="scene-tab" data-scene="1" role="tab" aria-selected="false" type="button">
              <span class="tab-dot"></span>
              <span>🏢 Penthouse VIP</span>
            </button>
            <button class="scene-tab" data-scene="2" role="tab" aria-selected="false" type="button">
              <span class="tab-dot"></span>
              <span>💎 Tiện Ích 5 Sao</span>
            </button>
          </div>"""
    content = content.replace(old_tabs, new_tabs)

    # 5. Studio Images
    old_imgs = """              <div class="cinema-slide active" style="--bg: url('assets/real_estate_penthouse.jpg')">
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
    new_imgs = """              <div class="cinema-slide active" style="--bg: url('assets/sapa_drone.jpg')">
                <div class="cinema-img ken-burns-1"></div>
                <div class="cinema-overlay"></div>
              </div>
              <div class="cinema-slide" style="--bg: url('assets/real_estate_penthouse.jpg')">
                <div class="cinema-img ken-burns-2"></div>
                <div class="cinema-overlay"></div>
              </div>
              <div class="cinema-slide" style="--bg: url('assets/fb_espresso_crema.jpg')">
                <div class="cinema-img ken-burns-3"></div>
                <div class="cinema-overlay"></div>
              </div>"""
    content = content.replace(old_imgs, new_imgs)

    # 6. Studio JS
    old_js = """    const demos = [
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
    new_js = """    const demos = [
      {
        title: '🚁 Flycam Đất Nền',
        text: 'Cinematic 8k aerial drone shot over beautiful green valleys and land plots at golden sunrise, morning mist rolling over emerald hills, sun rays piercing through clouds, slow dolly forward, 24fps filmic…',
        cam: 'CAM: slow aerial dolly'
      },
      {
        title: '🏢 Penthouse VIP',
        text: 'Smooth slow dolly through a luxurious minimalist penthouse living room, premium leather sofa bathed in warm morning sunlight, panoramic city skyline view through floor-to-ceiling windows, 8k…',
        cam: 'CAM: slow architectural dolly'
      },
      {
        title: '💎 Tiện Ích 5 Sao',
        text: 'Ultra macro slow motion shot of rich Espresso coffee being poured into a ceramic cup at a luxury residential lobby lounge, thick golden-brown crema bubbling, upscale lifestyle, 4k 120fps…',
        cam: 'CAM: extreme macro slow-mo'
      }
    ];"""
    content = content.replace(old_js, new_js)

    # 7. Pain Points
    content = content.replace("3 Rào Cản Khiến Người Mới Dễ Bỏ Cuộc Với Veo 3", "3 Nỗi Đau Của Sales BĐS Khi Làm Video Bán Hàng")
    content = content.replace("Veo 3 rất mạnh mẽ, nhưng rào cản ban đầu khiến phần lớn người mới dừng lại trước khi tạo được video đầu tiên.", "Làm video BĐS truyền thống tốn quá nhiều tiền và công sức, nhưng bỏ qua thì lại mất khách VIP vào tay đối thủ.")
    
    # Pain 1
    content = content.replace("Tiếng Anh Kỹ Thuật Phức Tạp", "Chi Phí Media Quá Đắt Đỏ")
    content = content.replace("Bạn không biết viết prompt (câu lệnh) sao cho đúng. Viết sai thì AI tạo ra những đoạn video biến dạng, ảo ma, tốn thời gian chờ đợi mà không xài được.", "Thuê flycam bay chụp dự án hay thợ xịn quay nội thất ngốn hàng chục triệu mỗi tháng. Chi phí marketing bị đội lên quá cao mà chưa chắc đã chốt được deal.")
    content = content.replace("Giải pháp: Copy & paste lệnh mẫu có sẵn", "Giải pháp: Veo 3 làm video flycam 4K miễn phí")
    
    # Pain 2
    content = content.replace("Đòi Hỏi Máy Tính Khủng", "Sợ Công Nghệ Phức Tạp")
    content = content.replace("Nhiều người lầm tưởng chơi AI Video cần PC vài chục triệu để render. Máy yếu tải về cài đặt xong thì treo máy, giật lag không thể render nổi.", "Môi giới BĐS quá bận rộn để học các phần mềm dựng phim phức tạp như Premiere, After Effects. Đa số chỉ biết dùng điện thoại cơ bản.")
    content = content.replace("Giải pháp: Render trên mây, điện thoại cũng làm được", "Giải pháp: Dùng ngay trên trình duyệt điện thoại")
    
    # Pain 3
    content = content.replace("Không Thể Truy Cập Veo 3", "Thiếu Ý Tưởng Chốt Khách")
    content = content.replace("Google Veo 3 đang giới hạn thử nghiệm, người dùng thông thường rất khó đăng ký tài khoản thành công hoặc bị xếp hàng chờ vài tháng.", "Khách VIP bây giờ rất khó tính, gửi mấy bức ảnh 2D hay video rung lắc quay bằng điện thoại thì khách seen không thèm rep.")
    content = content.replace("Giải pháp: Nhận tài khoản dùng ngay lập tức", "Giải pháp: Gửi video siêu thực chốt cảm xúc ngay")

    # 8. Prompts Cards
    # Card 1 (already BDS)
    content = content.replace("Dự Án Bất Động Sản", "Flycam Đất Nền Nghỉ Dưỡng")
    content = content.replace("Flycam lướt qua hồ bơi vô cực tiến vào biệt thự kính hiện đại, ánh sáng ấm cúng, 8k kiến trúc cinematic.", "Cinematic 8k aerial drone shot over beautiful green valleys and land plots at golden sunrise, morning mist rolling over emerald hills, sun rays piercing through clouds, slow dolly forward, 24fps filmic.")
    
    # Card 2
    content = content.replace("Review Thời Trang", "Penthouse Sang Trọng")
    content = content.replace("Nữ người mẫu chuyên nghiệp mặc váy lụa đỏ đi catwalk tại Paris Fashion Week", "Phòng khách Penthouse phong cách Minimalism, nhìn ra toàn cảnh thành phố")
    content = content.replace("Medium shot người mẫu mặc váy lụa thướt tha, sải bước tự tin, đèn flash máy ảnh chớp nháy phía sau, 4k 60fps.", "Smooth slow dolly through a luxurious minimalist penthouse living room, premium leather sofa bathed in warm morning sunlight, sheer silk curtains blowing gently, panoramic city skyline view through floor-to-ceiling windows, architectural photography, 4k 60fps.")
    
    # Card 3
    content = content.replace("Quảng Cáo F&B", "Tiện Ích Nội Khu 5 Sao")
    content = content.replace("Cận cảnh miếng bò bít tết Wagyu xèo xèo trên chảo gang nóng", "Sảnh Lounge đón khách VIP với ly Espresso sủi bọt sang trọng")
    content = content.replace("Cận cảnh siêu sắc nét ly cà phê Espresso đang được rót từ máy pha, lớp crema màu nâu vàng óng ả sủi bọt, hơi nóng bốc lên nghi ngút trong ánh sáng ban mai.", "Cận cảnh siêu sắc nét ly cà phê Espresso tại sảnh Lounge tiếp khách VIP của khu dân cư cao cấp, lớp crema màu nâu vàng óng ả sủi bọt, phong cách sống thượng lưu.")
    content = content.replace("Extreme macro miếng Wagyu dày đang xèo xèo bốc khói, bơ tan chảy sủi bọt, ánh sáng nhà hàng ấm cúng, 4k macro slow motion.", "Ultra macro shot of rich Espresso coffee being poured into a ceramic cup at a luxury residential lobby lounge, thick golden-brown crema bubbling, hot steam rising, upscale lifestyle, commercial food photography, 4k 120fps slow motion.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Real Estate Niche Update completed.")
