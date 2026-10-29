# CC Chart — website

Trang GitHub Pages dùng cho App Store / Google Play.

- Trang chủ: https://thientran2910.github.io/cc-chart-site/
- Hỗ trợ (Support URL của store): https://thientran2910.github.io/cc-chart-site/support.html
- Privacy: https://thientran2910.github.io/cc-chart-site/privacy.html
- Điều khoản: https://thientran2910.github.io/cc-chart-site/terms.html

## Sửa trang

Các file `.html` ở gốc repo (`index`, `support`, `privacy`, `terms`, `404`) là file **sinh ra**, đừng sửa tay. Sửa trong `src/` rồi chạy:

```sh
python3 src/build.py
```

| File trong `src/` | Nội dung |
|---|---|
| `shared.css`, `shared.js` | Token màu (tối/sáng), header, footer, nút EN/VI và sáng/tối |
| `support.body.html`, `support.css`, `candles.js` | Trang Hỗ trợ (biểu đồ nến minh hoạ) |
| `home.body.html`, `home.css` | Trang chủ, ảnh app trong khung iPhone (`assets/shots/`) |
| `privacy.body.html`, `privacy.css`, `toc.js` | Trang Quyền riêng tư (mục lục bám cuộn) |
| `terms.body.html` | Điều khoản sử dụng (dùng chung `privacy.css`) |
| `404.body.html` | Trang 404 (link tuyệt đối `/cc-chart-site/`) |
| `build.py` | Ghép trang, icon SVG, header/footer; cũng sinh bản xem trước Artifact vào `build/` |
| `icon128.png` | Icon app, nhúng base64 làm logo và favicon |

Văn bản song ngữ: phần tiếng Anh bọc `class="en"`, tiếng Việt `class="vi"`. Mặc định tiếng Anh, nền tối.

Email liên hệ công khai: điền `SUPPORT_EMAIL` trong `src/build.py` rồi build lại; để trống thì mọi dòng email bị ẩn.

Ảnh app (`assets/shots/*.jpg`, 720×1565) chụp từ simulator iPhone bằng dữ liệu thật.
