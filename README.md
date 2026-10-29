# CC Chart — trang hỗ trợ và chính sách quyền riêng tư

Trang GitHub Pages dùng cho App Store / Google Play.

- Hỗ trợ: https://thientran2910.github.io/cc-chart-site/
- Privacy: https://thientran2910.github.io/cc-chart-site/privacy.html

## Sửa trang

`index.html` và `privacy.html` ở gốc repo là file **sinh ra**, đừng sửa tay. Sửa trong `src/` rồi chạy:

```sh
python3 src/build.py
```

| File trong `src/` | Nội dung |
|---|---|
| `shared.css`, `shared.js` | Token màu (tối/sáng), header, footer, nút EN/VI và sáng/tối |
| `support.body.html`, `support.css`, `candles.js` | Trang Hỗ trợ (biểu đồ nến minh hoạ) |
| `privacy.body.html`, `privacy.css`, `toc.js` | Trang Quyền riêng tư (mục lục bám cuộn) |
| `build.py` | Ghép trang, icon SVG, header/footer; cũng sinh bản xem trước Artifact vào `build/` |
| `icon128.png` | Icon app, nhúng base64 làm logo và favicon |

Văn bản song ngữ: phần tiếng Anh bọc `class="en"`, tiếng Việt `class="vi"`. Mặc định tiếng Anh, nền tối.
