import os
import glob

directory = r"e:\ui-ux-pro-max-skill\preview"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix viewport bug with overflow-x: clip
    content = content.replace("overflow-x: clip;", "overflow-x: hidden !important;")
    
    # Fix max-width: 100vw causing horizontal scrollbar issues
    content = content.replace("max-width: 100vw;", "max-width: 100%;")
    
    # Inject bulletproof mobile fixes right after universal box-sizing
    if "/* injected_mobile_fixes */" not in content:
        injection = """
    /* injected_mobile_fixes */
    html, body { overflow-x: hidden !important; max-width: 100% !important; }
    .container { overflow-x: hidden; max-width: 100%; }
    img, video { max-width: 100%; height: auto; }
    pre, .prompt-code-wrap, table, .table-wrapper { overflow-x: auto !important; max-width: 100%; -webkit-overflow-scrolling: touch; }
    p, a, span, h1, h2, h3, h4, h5, h6 { word-wrap: break-word; word-break: break-word; overflow-wrap: break-word; }
    /* Force specific elements that might overflow to be contained */
    .bg-glow, .bg-glow::before, .bg-glow::after { max-width: 100vw; overflow: hidden; }
    """
        
        # Try finding different variants of the universal selector
        if "*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }" in content:
            content = content.replace("*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }", "*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }\n" + injection)
        elif "*, *::before, *::after { box-sizing: border-box;" in content:
            content = content.replace("*, *::before, *::after { box-sizing: border-box;", "*, *::before, *::after { box-sizing: border-box;" + injection)
        else:
            # Fallback to inserting after body {
            content = content.replace("body {", injection + "\n    body {")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed {len(html_files)} HTML files for mobile responsiveness.")
