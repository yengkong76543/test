# Hướng dẫn Deploy - Browser Fingerprinting

## 🚀 Các cách deploy miễn phí

### 1. **Render.com** (Khuyến nghị - Dễ nhất)

#### Bước 1: Chuẩn bị
- Tạo tài khoản tại https://render.com
- Đăng nhập bằng GitHub

#### Bước 2: Deploy
1. Vào Dashboard → **New** → **Web Service**
2. Connect GitHub repository của bạn
3. Chọn repository `phishing`
4. Điền thông tin:
   - **Name**: `law-insight` (hoặc tên bạn muốn)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Port**: `10000` (hoặc để trống, Render tự detect)

5. Click **Create Web Service**
6. Đợi deploy xong (5-10 phút)

#### Bước 3: Xem logs
- Vào **Logs** tab trong dashboard
- Mỗi khi có người truy cập → sẽ thấy: `✅ Logged fingerprint from ...`

#### Bước 4: Xem fingerprint data
- Vào **Shell** tab → chạy:
  ```bash
  cat fingerprints/fingerprints_log.jsonl
  ```
- Hoặc download logs từ dashboard

---

### 2. **Railway.app** (Nhanh nhất)

#### Bước 1: Chuẩn bị
- Tạo tài khoản tại https://railway.app
- Đăng nhập bằng GitHub

#### Bước 2: Deploy
1. Click **New Project** → **Deploy from GitHub repo**
2. Chọn repository `phishing`
3. Railway tự động detect Python và deploy
4. Đợi deploy xong (3-5 phút)

#### Bước 3: Xem logs
- Vào **View Logs** trong dashboard
- Mỗi khi có người truy cập → sẽ thấy fingerprint logs

#### Bước 4: Xem fingerprint data
- Vào **Settings** → **Generate Domain** để có URL công khai
- Xem logs trong dashboard

---

### 3. **Vercel** (Serverless - Có giới hạn)

#### Bước 1: Cài đặt Vercel CLI
```bash
npm install -g vercel
```

#### Bước 2: Deploy
```bash
cd D:\phishing
vercel
```

Làm theo hướng dẫn:
- **Set up and deploy?** → Y
- **Which scope?** → Chọn tài khoản của bạn
- **Link to existing project?** → N
- **Project name?** → `law-insight` (hoặc Enter để dùng mặc định)
- **Directory?** → `.` (Enter)
- **Override settings?** → N

#### Bước 3: Xem logs
```bash
vercel logs
```

**Lưu ý**: Vercel có filesystem read-only, fingerprints sẽ lưu vào `/tmp` và chỉ tồn tại trong thời gian function chạy. Để lưu lâu dài, cần dùng database (MongoDB Atlas).

---

### 4. **GitHub Pages** (Chỉ static - KHÔNG dùng được)

GitHub Pages chỉ hỗ trợ static files, không chạy được Flask/Python.

---

## 📊 Sau khi deploy

### Kiểm tra fingerprinting hoạt động:

1. **Mở website** (URL từ Render/Railway/Vercel)
2. **Mở Developer Tools** (F12) → Tab **Network**
3. Tìm request `POST /api/fingerprint` → Status phải là **200**
4. **Xem logs** trong dashboard của hosting platform

### Xem fingerprint data:

#### Render:
```bash
# Vào Shell tab trong dashboard
cat fingerprints/fingerprints_log.jsonl
```

#### Railway:
- Vào **View Logs** → tìm các dòng có `✅ Logged fingerprint`

#### Vercel:
```bash
vercel logs
```

---

## 🔧 Troubleshooting

### Không thấy logs?
1. Kiểm tra website có chạy không (mở URL)
2. Kiểm tra Console (F12) có lỗi không
3. Kiểm tra Network tab → request `/api/fingerprint` có được gửi không
4. Xem logs trong hosting dashboard

### Fingerprint không được lưu?
- **Render/Railway**: Kiểm tra quyền ghi file (thường tự động)
- **Vercel**: Filesystem read-only, cần dùng database hoặc external storage

### Website không load?
- Kiểm tra build logs trong dashboard
- Kiểm tra `requirements.txt` có đúng không
- Kiểm tra start command có đúng không

---

## 📝 Lưu ý quan trọng

1. **Render/Railway**: 
   - ✅ Files được lưu vĩnh viễn
   - ✅ Có thể xem logs trực tiếp
   - ✅ Dễ deploy nhất

2. **Vercel**:
   - ⚠️ Filesystem read-only
   - ⚠️ Fingerprints lưu vào `/tmp` (tạm thời)
   - ✅ Tốc độ nhanh
   - 💡 Nên dùng MongoDB Atlas để lưu lâu dài

3. **Sau khi deploy**:
   - Share URL cho người khác
   - Mỗi lượt truy cập → fingerprint tự động được ghi
   - Xem logs trong dashboard

---

## 🎯 Quick Start (Render - Khuyến nghị)

1. Push code lên GitHub
2. Vào https://render.com → New Web Service
3. Connect GitHub → Chọn repo
4. Build: `pip install -r requirements.txt`
5. Start: `python app.py`
6. Deploy!
7. Share URL → Mọi người vào → Fingerprint tự động được ghi!

**Xong!** 🎉
