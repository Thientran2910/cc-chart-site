import base64, os, sys

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(SRC, '..')
OUT = os.path.join(ROOT, 'build')
rd = lambda n: open(os.path.join(SRC, n), encoding='utf-8').read()

ICON = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(SRC, 'icon128.png'), 'rb').read()).decode()

def svg(body):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + body + '</svg>')

ICONS = {
    'I_CHAT': svg('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12Z"/><path d="M8.5 12h.01M12 12h.01M15.5 12h.01"/>'),
    'I_SHIELD': svg('<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6L12 3Z"/><path d="m9 12 2 2 4-4"/>'),
    'I_CLOCK': svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    'I_USER': svg('<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>'),
    'I_CANDLE': svg('<path d="M7 3v4M7 15v6M17 3v3M17 14v7"/><rect x="5" y="7" width="4" height="8" rx="1"/><rect x="15" y="6" width="4" height="8" rx="1"/>'),
    'I_WAVE': svg('<path d="M3 17c2.5 0 3-10 6-10s3 10 6 10 3.5-6 6-6"/><path d="M3 21h18"/>'),
    'I_PEN': svg('<path d="m4 20 4.5-1 10-10a2.1 2.1 0 0 0-3-3l-10 10L4 20Z"/><path d="m14 7 3 3"/>'),
    'I_LIST': svg('<path d="M4 6h10M4 12h10M4 18h10"/><path d="m17 8 2-2 2 2M17 16l2 2 2-2"/>'),
    'I_FLASK': svg('<path d="M9 3h6M10 3v6L4.5 18.5A1.7 1.7 0 0 0 6 21h12a1.7 1.7 0 0 0 1.5-2.5L14 9V3"/><path d="M7.5 15h9"/>'),
    'I_SPARK': svg('<path d="M12 3c.6 4.2 2.8 6.4 7 7-4.2.6-6.4 2.8-7 7-.6-4.2-2.8-6.4-7-7 4.2-.6 6.4-2.8 7-7Z"/><path d="M19 17.5c.2 1.3.9 2 2 2.2-1.1.2-1.8.9-2 2.2-.2-1.3-.9-2-2-2.2 1.1-.2 1.8-.9 2-2.2Z"/>'),
    'I_GITHUB': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.7c-2.8.6-3.4-1.3-3.4-1.3-.5-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.6 2.4 1.1 3 .9.1-.7.4-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.8 1a9.6 9.6 0 0 1 5 0c1.9-1.3 2.8-1 2.8-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 3.9-2.4 4.7-4.6 5 .4.3.7.9.7 1.9V21c0 .3.2.6.7.5A10 10 0 0 0 12 2Z"/></svg>',
    'I_APPLE': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.2-1.7-3-1.9-3.6-2-1.5-.2-3 .9-3.8.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.1 2.5-1.8 3.1-.5 7.6 1.3 10.1.8 1.2 1.8 2.6 3.1 2.5 1.2 0 1.7-.8 3.2-.8s1.9.8 3.2.8c1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.4-1-2.4-4.2ZM14 5.3c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1 .1 2.1-.6 2.8-1.4Z"/></svg>',
    'I_CHECK': svg('<circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.5 2.5 4.5-5"/>'),
}
SUN = svg('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>').replace('<svg', '<svg class="i-sun"')
MOON = svg('<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/>').replace('<svg', '<svg class="i-moon"')

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700'
         '&family=Bricolage+Grotesque:opsz,wght@12..96,600..800&family=JetBrains+Mono:wght@500;600;700&display=swap">')

BOOT = ("<script>(function(){var d=document.documentElement,s=null;try{s=window.localStorage}catch(e){}"
        "function g(k){try{return s&&s.getItem(k)}catch(e){return null}}"
        "var l=g('cc-chart-site.lang'),m=g('cc-chart-site.mode');"
        "d.setAttribute('data-lang',l==='vi'?'vi':'en');d.setAttribute('data-mode',m==='light'?'light':'dark');"
        "d.lang=l==='vi'?'vi':'en';})();</script>")

# Public support email; empty hides every email line. Set it, then run this script.
SUPPORT_EMAIL = 'ccchart.support@gmail.com'
ISSUES = 'https://github.com/Thientran2910/cc-chart-site/issues/new'

NAV = [('home', 'HOME', 'Overview', 'Tổng quan'), ('support', 'SUPPORT', 'Support', 'Hỗ trợ'),
       ('privacy', 'PRIVACY', 'Privacy', 'Quyền riêng tư'), ('terms', 'TERMS', 'Terms', 'Điều khoản')]


def header(cur):
    links = '\n'.join(
        '    <a href="{{' + k + '}}"' + (' aria-current="page"' if cur == p else '')
        + f'><span class="en">{en}</span><span class="vi">{vi}</span></a>'
        for p, k, en, vi in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{{{{HOME}}}}"><img src="{ICON}" alt="" width="30" height="30"><span>CC Chart</span></a>
  <nav class="nav" aria-label="Pages">
{links}
  </nav>
  <div class="controls">
    <div class="seg" role="group" aria-label="Language / Ngôn ngữ">
      <button type="button" id="lang-en" data-set-lang="en" aria-pressed="true">EN</button>
      <button type="button" id="lang-vi" data-set-lang="vi" aria-pressed="false">VI</button>
    </div>
    <button type="button" id="mode-toggle" class="icon-btn" data-toggle-mode aria-label="Switch theme">{SUN}{MOON}</button>
  </div>
</div>
<nav class="wrap tabs-m" aria-label="Pages">
{links}
</nav>
</header>'''


FOOTER = '''<footer class="site-footer"><div class="wrap">
  <div class="foot-row">
    <a class="brand" href="{{HOME}}"><img src="''' + ICON + '''" alt="" width="30" height="30"><span>CC Chart</span></a>
    <div class="foot-links">
      <a href="{{SUPPORT}}"><span class="en">Support</span><span class="vi">Hỗ trợ</span></a>
      <a href="{{PRIVACY}}"><span class="en">Privacy Policy</span><span class="vi">Chính sách quyền riêng tư</span></a>
      <a href="{{TERMS}}"><span class="en">Terms of Use</span><span class="vi">Điều khoản sử dụng</span></a>
      <a href="''' + ISSUES + '''" target="_blank" rel="noopener"><span class="en">Contact</span><span class="vi">Liên hệ</span></a>
    </div>
  </div>
  <p class="foot-note"><span class="en">Price data comes from public exchange APIs. CC Chart is not an exchange and never holds user funds. Information in the app is for reference only and is not investment advice.</span><span class="vi">Dữ liệu giá lấy từ API công khai của các sàn. CC Chart không phải sàn giao dịch, không giữ tiền của người dùng. Thông tin trong ứng dụng chỉ để tham khảo, không phải lời khuyên đầu tư.</span></p>
  <p class="copyright">© 2026 Thien Tran</p>
</div></footer>'''

PAGES = {
    'home': dict(out='index.html', body='home.body.html', css='support.css home.css', js=[],
                 t_en='CC Chart', t_vi='CC Chart',
                 desc='CC Chart: real-time crypto charts, 40+ indicators, drawing tools and demo trading for Binance and OKX.'),
    'support': dict(out='support.html', body='support.body.html', css='support.css', js=['candles.js'],
                    t_en='CC Chart Support', t_vi='Hỗ trợ CC Chart',
                    desc='Help, FAQ and contact for CC Chart, a real-time crypto charting app.'),
    'privacy': dict(out='privacy.html', body='privacy.body.html', css='privacy.css', js=['toc.js'],
                    t_en='CC Chart Privacy Policy', t_vi='CC Chart — Chính sách quyền riêng tư',
                    desc='How the CC Chart app handles your data.'),
    'terms': dict(out='terms.html', body='terms.body.html', css='privacy.css', js=['toc.js'],
                  t_en='CC Chart Terms of Use', t_vi='CC Chart — Điều khoản sử dụng',
                  desc='Terms of Use for the CC Chart app.'),
    '404': dict(out='404.html', body='404.body.html', css='support.css', js=[],
                t_en='Page not found · CC Chart', t_vi='Không tìm thấy trang · CC Chart',
                desc='This page does not exist.'),
}


def email_parts():
    if not SUPPORT_EMAIL:
        return {'EMAIL_EN': '', 'EMAIL_VI': '', 'EMAIL_BLOCK': ''}
    e = SUPPORT_EMAIL
    link = f'<a href="mailto:{e}">{e}</a>'
    block = (f'<div class="email-row"><span class="en">Or email</span><span class="vi">Hoặc email</span> '
             f'<code class="mono" id="support-email">{e}</code>'
             '<button type="button" class="copy-btn" data-copy="support-email"><span class="en">Copy</span><span class="vi">Sao chép</span></button></div>')
    return {'EMAIL_EN': f' or email {link}', 'EMAIL_VI': f' hoặc email {link}', 'EMAIL_BLOCK': block}


def render(key, links, full):
    p = PAGES[key]
    head = (f'<title data-en="{p["t_en"]}" data-vi="{p["t_vi"]}">{p["t_en"]}</title>\n'
            f'<meta name="description" content="{p["desc"]}">\n'
            '<meta name="claude:viewport-fit-sides" content="cover">\n'
            f'<meta name="theme-color" content="#090e0c">\n<link rel="icon" href="{ICON}">\n'
            + FONTS + '\n' + BOOT + '\n<style>\n' + rd('shared.css') + '\n' + ''.join(rd(c) + '\n' for c in p['css'].split()) + '\n</style>\n')
    body = (header(key) + '\n' + rd(p['body']) + '\n' + FOOTER + '\n<script>\n' + rd('shared.js') + '\n'
            + ''.join(rd(j) for j in p['js']) + '</script>\n')
    for k, v in {**ICONS, **email_parts(), **links}.items():
        body = body.replace('{{' + k + '}}', v)
    assert '{{' not in body, key
    if not full:
        return head + body
    return ('<!doctype html>\n<html lang="en" data-lang="en" data-mode="dark">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + head + '</head>\n<body>\n' + body + '</body>\n</html>\n')


def write(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(s)


def links(base, home):
    return {'HOME': home, 'SUPPORT': base + 'support.html', 'PRIVACY': base + 'privacy.html',
            'TERMS': base + 'terms.html', 'BASE': base}


# GitHub Pages site at the repo root. 404.html is served from any path, so it links absolutely.
for key, p in PAGES.items():
    l = links('/cc-chart-site/', '/cc-chart-site/') if key == '404' else links('', './')
    write(os.path.join(ROOT, p['out']), render(key, l, True))
# Artifact preview (build/, not committed): home page without skeleton, the rest as supporting full pages.
art = links('', 'index.html')
write(os.path.join(OUT, 'artifact', 'home.html'), render('home', art, False))
for key in ('support', 'privacy', 'terms'):
    write(os.path.join(OUT, 'artifact', PAGES[key]['out']), render(key, art, True))
print('ok')
