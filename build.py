#!/usr/bin/env python3
"""EasyTechPack v2.1 - Cycle 1 fixes applied"""
import os

OUT = "/root/.openclaw/workspace/easytechpack/index.html"

pages = [
    ("cover", "\U0001f4cb", "Cover Page", "Your brand info and logo - START HERE"),
    ("sketches", "\u270f\ufe0f", "Design Sketches", "Upload drawings of your garment from different angles"),
    ("fabric-placement", "\U0001f9f5", "Fabric List", "What fabrics you need and where each one goes"),
    ("trims", "\u2702\ufe0f", "Trims & Extras", "Zippers, buttons, labels, and other supplies"),
    ("bom", "\U0001f9f6", "Materials List", "Complete list of everything needed to make this garment"),
    ("measurements", "\U0001f4cf", "Measurements", "The actual sizes and dimensions for your garment"),
    ("construction", "\U0001faa5", "How It's Made", "Notes on how the pieces are sewn together"),
    ("stitch", "\U0001f517", "Stitch Details", "What stitches to use and where"),
    ("detail-sketches", "\U0001f4d0", "Close-Up Details", "Zoomed-in drawings of tricky construction areas"),
    ("how-to-measure", "\U0001f4d0", "How to Measure", "Diagrams showing WHERE to measure on the garment"),
    ("care-labels", "\U0001f3f7\ufe0f", "Care Instructions", "Washing, drying, and ironing instructions for the label"),
    ("grading", "\U0001f4ca", "Size Chart", "Measurements for each size (XS, S, M, L, XL)"),
    ("grading-rules", "\U0001f4ca", "Size Differences", "How much each measurement changes between sizes"),
    ("proto-tracking", "\U0001f52c", "Sample Tracking", "Track how each sample version matches your design"),
    ("comments", "\U0001f4ac", "Feedback Notes", "Notes and changes for each sample round"),
    ("cost", "\U0001f4b0", "Cost Calculator", "How much each piece costs to make"),
    ("colorways", "\U0001f3a8", "Color Options", "All the colors this garment will come in"),
    ("labels", "\U0001f3f7\ufe0f", "Labels & Tags", "Brand labels, size tags, and hang tags"),
    ("packaging", "\U0001f4e6", "Packaging", "How the garment is packed and shipped"),
    ("changelog", "\U0001f4dd", "Changes Log", "Keep track of all edits and updates"),
]

categories = {
    "DESIGN": ["cover", "sketches", "detail-sketches"],
    "MATERIALS": ["fabric-placement", "trims", "bom", "colorways"],
    "SIZING": ["measurements", "how-to-measure", "grading", "grading-rules"],
    "PRODUCTION": ["construction", "stitch", "care-labels", "proto-tracking", "comments"],
    "BUSINESS": ["cost", "labels", "packaging", "changelog"],
}

cat_icons = {"DESIGN": "\U0001f3a8", "MATERIALS": "\U0001f9f5", "SIZING": "\U0001f4cf", "PRODUCTION": "\U0001f52c", "BUSINESS": "\U0001f4b0"}

page_map = {p[0]: p for p in pages}

# Build HTML
html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EasyTechPack v2.1</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f5f5f5;color:#222;display:flex;height:100vh;overflow:hidden}
.sidebar{width:250px;background:#1a1a2e;color:#fff;display:flex;flex-direction:column;flex-shrink:0;z-index:100}
.sidebar-header{padding:20px;border-bottom:1px solid #333}
.sidebar-header h1{font-size:18px;font-weight:700;letter-spacing:-.5px}
.sidebar-header p{font-size:11px;color:#888;margin-top:4px}
.sidebar-nav{flex:1;overflow-y:auto;padding:8px 0}
.nav-category{padding:8px 20px 4px;font-size:10px;font-weight:700;color:#666;text-transform:uppercase;letter-spacing:1px}
.nav-item{padding:9px 20px 9px 28px;cursor:pointer;font-size:13px;color:#aaa;transition:all .15s;display:flex;align-items:center;gap:8px}
.nav-item:hover{background:#16213e;color:#fff}
.nav-item.active{background:#0f3460;color:#fff;border-left:3px solid #e94560}
.nav-item .nav-badge{margin-left:auto;font-size:9px;background:#333;padding:1px 6px;border-radius:8px;color:#888}
.nav-item.has-data .nav-badge{background:#0f3460;color:#4caf50}
.nav-icon{width:16px;text-align:center;font-size:13px}
.sidebar-footer{padding:15px 20px;border-top:1px solid #333}
.sidebar-footer .save-status{font-size:10px;color:#4caf50;margin-bottom:8px;text-align:center}
.export-btn{width:100%;padding:10px;background:#e94560;color:#fff;border:none;border-radius:6px;font-size:13px;font-weight:600;cursor:pointer;margin-bottom:6px}
.export-btn:hover{background:#c73b54}
.btn-row{display:flex;gap:6px;margin-bottom:6px}
.btn-row button{flex:1;padding:7px;background:transparent;color:#888;border:1px solid #444;border-radius:6px;font-size:11px;cursor:pointer}
.btn-row button:hover{color:#fff;border-color:#888}
.menu-toggle{display:none;position:fixed;top:12px;left:12px;z-index:200;background:#1a1a2e;color:#fff;border:none;border-radius:6px;padding:8px 12px;font-size:18px;cursor:pointer}
.sidebar-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:99}
.save-indicator{position:fixed;top:12px;right:20px;font-size:11px;color:#4caf50;opacity:0;transition:opacity .3s;z-index:50;background:#fff;padding:4px 10px;border-radius:4px;box-shadow:0 1px 3px rgba(0,0,0,.1)}
.save-indicator.show{opacity:1}
.main{flex:1;display:flex;flex-direction:column;overflow:hidden}
.topbar{background:#fff;border-bottom:1px solid #ddd;padding:12px 24px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0;flex-wrap:wrap;gap:8px}
.topbar-fields{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.topbar-fields label{font-size:10px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:.5px}
.topbar-fields input{border:1px solid #ddd;border-radius:4px;padding:5px 8px;font-size:13px;width:140px}
.topbar-fields input:focus{outline:none;border-color:#0f3460}
.file-name{font-size:9px;color:#aaa;font-family:monospace}
.page-content{flex:1;overflow-y:auto;padding:24px}
.page{display:none}.page.active{display:block}
.page-title{font-size:20px;font-weight:700;margin-bottom:4px}
.page-subtitle{font-size:13px;color:#666;margin-bottom:6px}
.page-tip{font-size:12px;color:#888;background:#f0f7ff;border-left:3px solid #4a90d9;padding:10px 14px;border-radius:0 6px 6px 0;margin-bottom:20px;line-height:1.5}
table{width:100%;border-collapse:collapse;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08);margin-bottom:16px}
th{background:#f8f9fa;font-size:10px;font-weight:600;color:#666;text-transform:uppercase;letter-spacing:.5px;padding:10px 12px;text-align:left;border-bottom:2px solid #e9ecef;white-space:nowrap}
th .tip{display:block;font-size:9px;font-weight:400;color:#999;text-transform:none;letter-spacing:0;margin-top:2px}
td{padding:8px 12px;border-bottom:1px solid #f0f0f0;font-size:13px}
tr:last-child td{border-bottom:none}
td input,td select,td textarea{border:none;background:transparent;width:100%;font-size:13px;padding:3px 0;font-family:inherit}
td input:focus,td select:focus,td textarea:focus{outline:none;background:#fffbe6}
td textarea{resize:vertical;min-height:28px}
.add-row{padding:8px 16px;background:#f0f0f0;border:1px dashed #ccc;border-radius:6px;color:#888;font-size:13px;cursor:pointer;width:100%;margin-top:4px}
.add-row:hover{background:#e8e8e8;color:#555;border-color:#999}
.del-btn{background:none;border:none;color:#ccc;cursor:pointer;font-size:16px;padding:0 4px;opacity:.5}
.del-btn:hover{color:#e94560;opacity:1}
.logo-upload{display:flex;align-items:center;gap:20px;margin-bottom:20px}
.logo-preview{width:120px;height:120px;border:2px dashed #ddd;border-radius:8px;display:flex;align-items:center;justify-content:center;overflow:hidden;background:#fafafa;cursor:pointer}
.logo-preview img{max-width:100%;max-height:100%;object-fit:contain}
.logo-preview span{font-size:12px;color:#aaa}
.cover-box{background:#fff;border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,.08);padding:30px;max-width:600px}
.cover-row{margin-bottom:14px}
.cover-row label{display:block;font-size:10px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px}
.cover-row input,.cover-row textarea{width:100%;border:1px solid #ddd;border-radius:4px;padding:8px 12px;font-size:14px}
.cover-row textarea{height:80px;resize:vertical;font-family:inherit}
.cover-row input:focus,.cover-row textarea:focus{outline:none;border-color:#0f3460}
.sketch-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin-bottom:16px}
.sketch-card{background:#fff;border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,.08);overflow:hidden}
.sketch-card-img{height:180px;background:#fafafa;display:flex;align-items:center;justify-content:center;border-bottom:1px solid #eee;overflow:hidden;cursor:pointer}
.sketch-card-img img{max-width:100%;max-height:100%;object-fit:contain}
.sketch-card-input{padding:10px}
.sketch-card-input label{font-size:10px;font-weight:600;color:#888;text-transform:uppercase}
.sketch-card-input input{width:100%;border:1px solid #ddd;border-radius:4px;padding:5px 8px;font-size:13px;margin-top:3px}
.sketch-card-input input:focus{outline:none;border-color:#0f3460}
.export-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:1000;align-items:center;justify-content:center}
.export-overlay.show{display:flex}
.export-box{background:#fff;border-radius:12px;padding:40px;text-align:center;max-width:400px}
.export-box h2{margin-bottom:10px}.export-box p{color:#666;margin-bottom:20px}
.export-box .spinner{width:40px;height:40px;border:3px solid #eee;border-top-color:#e94560;border-radius:50%;animation:spin .8s linear infinite;margin:0 auto 15px}
@keyframes spin{to{transform:rotate(360deg)}}
.toast{position:fixed;bottom:20px;right:20px;background:#333;color:#fff;padding:12px 20px;border-radius:8px;font-size:13px;z-index:2000;opacity:0;transition:opacity .3s;max-width:350px}
.toast.show{opacity:1}
.toast.success{background:#4caf50}.toast.error{background:#e94560}.toast.info{background:#2196f3}
.confidential{font-size:9px;color:#bbb;text-align:center;padding:12px;margin-top:16px;border-top:1px solid #f0f0f0;font-style:italic}
.page-num{font-size:9px;color:#ddd;text-align:right;padding:4px 0}
.welcome-overlay{display:flex;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:3000;align-items:center;justify-content:center}
.welcome-overlay.hide{display:none}
.welcome-box{background:#fff;border-radius:16px;padding:40px;max-width:520px;text-align:center}
.welcome-box h1{font-size:24px;margin-bottom:8px}
.welcome-box p{color:#666;line-height:1.6;margin-bottom:16px;text-align:left}
.welcome-box ul{color:#444;text-align:left;margin:0 0 20px 20px;line-height:1.8}
.welcome-box button{padding:12px 32px;background:#e94560;color:#fff;border:none;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer}
.welcome-box button:hover{background:#c73b54}
.confirm-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:2000;align-items:center;justify-content:center}
.confirm-modal.show{display:flex}
.confirm-box{background:#fff;border-radius:12px;padding:30px;max-width:400px;text-align:center}
.confirm-box h2{margin-bottom:10px}.confirm-box p{color:#666;margin-bottom:20px}
.confirm-box .btns{display:flex;gap:10px;justify-content:center}
.confirm-box .btns button{padding:10px 24px;border:none;border-radius:6px;font-size:14px;cursor:pointer}
.confirm-box .btn-cancel{background:#eee;color:#333}.confirm-box .btn-confirm{background:#e94560;color:#fff}
.comments-section{margin-bottom:24px}
.comments-section h3{font-size:14px;font-weight:600;margin-bottom:10px;color:#444}
@media(max-width:768px){
.sidebar{position:fixed;left:-250px;top:0;height:100vh;transition:left .25s ease}
.sidebar.open{left:0}
.menu-toggle{display:block}
.sidebar-overlay.show{display:block}
.topbar{padding:12px 16px 12px 50px}
.topbar-fields{gap:8px}
.topbar-fields input{width:100px}
.page-content{padding:16px}
.sketch-grid{grid-template-columns:1fr}
.cover-box{padding:20px}
}
</style>
</head>
<body>
"""

# Welcome overlay
html += """<div class="welcome-overlay" id="welcome">
<div class="welcome-box">
<h1>\U0001f4c8 Welcome to EasyTechPack!</h1>
<p>A <strong>tech pack</strong> is a document that tells a factory exactly how to make your clothing design. Think of it as a recipe for your garment!</p>
<ul>
<li><strong>Fill in your brand info</strong> at the top of the page</li>
<li><strong>Work through the sidebar</strong> from top to bottom</li>
<li><strong>Upload sketches</strong> of your design (draw on paper, take a photo!)</li>
<li><strong>List your materials</strong> and measurements</li>
<li><strong>Export as PDF</strong> when you're done to send to a factory</li>
</ul>
<p style="font-size:12px;color:#888;text-align:center">Don't worry about filling in everything perfectly.<br>You can always come back and edit later!</p>
<button onclick="closeWelcome()">Let's Go!</button>
</div>
</div>"""

# Confirm modal
html += """<div class="confirm-modal" id="confirm-modal">
<div class="confirm-box">
<h2 id="confirm-title">Are you sure?</h2>
<p id="confirm-msg">This cannot be undone.</p>
<div class="btns">
<button class="btn-cancel" onclick="confirmCancel()">Cancel</button>
<button class="btn-confirm" id="confirm-ok">Delete</button>
</div>
</div>
</div>"""

# Toast
html += '<div class="toast" id="toast"></div>\n'

# Sidebar toggle + save indicator
html += """<button class="menu-toggle" onclick="toggleSidebar()">&#9776;</button>
<div class="sidebar-overlay" onclick="toggleSidebar()"></div>
<div class="save-indicator" id="save-indicator">&#10003; Saved</div>
"""

# Sidebar
html += '<div class="sidebar">\n<div class="sidebar-header">\n<h1>&#128208; EasyTechPack</h1>\n<p>v2.1 - Clothing Tech Pack Builder</p>\n</div>\n<div class="sidebar-nav">\n'

for cat, page_ids in categories.items():
    html += f'<div class="nav-category">{cat_icons.get(cat, "")} {cat}</div>\n'
    for pid in page_ids:
        p = page_map[pid]
        html += f'<div class="nav-item" data-page="{pid}"><span class="nav-icon">{p[1]}</span> {p[2]}<span class="nav-badge" id="badge-{pid}"></span></div>\n'

html += """</div>
<div class="sidebar-footer">
<div class="save-status" id="save-status">Auto-saving enabled</div>
<button class="export-btn" onclick="exportPDF()">&#128196; Export PDF</button>
<div class="btn-row">
<button onclick="loadExample()">&#128218; Load Example</button>
<button onclick="newTechPack()">&#128465; New</button>
</div>
<div class="btn-row">
<button onclick="saveBackup()">&#128190; Save Backup</button>
<button onclick="document.getElementById('load-backup-input').click()">&#128194; Load Backup</button>
<input type="file" id="load-backup-input" accept=".json" style="display:none" onchange="loadBackup(this)">
</div>
</div>
</div>
"""

# Main content
html += """<div class="main">
<div class="topbar">
<div class="topbar-fields">
<div><label>Brand Name</label><br><input type="text" id="brand-name" placeholder="Your Brand" oninput="debouncedSave()"></div>
<div><label>Style Name</label><br><input type="text" id="style-name" placeholder="e.g. Classic Hoodie" oninput="debouncedSave()"></div>
<div><label>Design Date</label><br><input type="date" id="pack-date" oninput="debouncedSave()"></div>
<div><label>Version</label><br><input type="text" id="pack-version" placeholder="v1.0" oninput="debouncedSave()"></div>
<span class="file-name" id="file-name"></span>
</div>
</div>
<div class="page-content">
"""

# Page tips (plain language guidance)
tips = {
    "cover": "Start here! Fill in your brand name and logo. This is the first page anyone sees in your tech pack.",
    "sketches": "Draw your garment on paper (front, back, side views), take a photo with your phone, and upload it here. Black and white drawings work best!",
    "fabric-placement": "List every fabric you'll use and where it goes on the garment. For example: 'Cotton jersey' on the 'Body', 'Rib knit' on the 'Cuffs'.",
    "trims": "List all the extras: zippers, buttons, labels, drawstrings, elastic. Add photos if you have them so the factory knows exactly what you want.",
    "bom": "This is your complete shopping list. Everything the factory needs to buy to make your garment. Check your sketches to make sure you didn't miss anything!",
    "measurements": "The actual numbers for your garment. Tip: take measurements from a similar garment you already own that fits well!",
    "construction": "General notes about how the garment is sewn together. For example: 'Side seams should be flatlocked' or 'Hood is lined'.",
    "stitch": "The specific stitches used. Don't worry if you don't know stitch types - just describe what you see on similar garments you like.",
    "detail-sketches": "Upload close-up drawings of tricky areas: pocket construction, zipper details, seam finishes. The more detail, the better!",
    "how-to-measure": "Diagrams showing exactly WHERE to measure. This helps the factory measure the same way you do.",
    "care-labels": "The washing instructions that go on the label inside your garment. You can usually get these from your fabric supplier.",
    "grading": "Your garment in different sizes. Start with one size (like M) and then figure out the measurements for other sizes.",
    "grading-rules": "How much each measurement changes between sizes. For example: chest might grow 2cm from M to L. Ask your factory for help!",
    "proto-tracking": "When the factory makes a sample, you check it and note what needs to change. Track each round of samples here.",
    "comments": "Write down everything that needs fixing after you check a sample. Separate pattern changes (sizing) from sewing changes (construction).",
    "cost": "Add up all your material costs to see how much each piece costs to make. This helps you set your selling price.",
    "colorways": "List all the colors your garment will come in. You can use the color picker or enter Pantone codes if you have them.",
    "labels": "Your brand label, size tag, and care label. Note where each one goes and what it looks like.",
    "packaging": "How the garment is packed: poly bag, hang tag, box. Include any special instructions.",
    "changelog": "Keep a record of all changes you make. This helps when working with factories!",
}

# Generate pages
for i, (pid, icon, title, desc) in enumerate(pages):
    active = ' active' if i == 0 else ''
    html += f'<div class="page{active}" id="page-{pid}">\n'
    html += f'<h2 class="page-title">{title}</h2>\n'
    html += f'<p class="page-subtitle">{desc}</p>\n'
    if pid in tips:
        html += f'<div class="page-tip">{tips[pid]}</div>\n'
    
    # Page-specific content
    if pid == "cover":
        html += '''<div class="cover-box">
<div class="logo-upload">
<div class="logo-preview" id="logo-preview" onclick="document.getElementById('logo-input').click()"><span>Click to upload logo</span></div>
<input type="file" id="logo-input" accept="image/*" onchange="handleLogo(this)" style="display:none">
</div>
<div class="cover-row"><label>Designer Name</label><input type="text" id="designer-name" placeholder="Your name" oninput="debouncedSave()"></div>
<div class="cover-row"><label>Season</label><input type="text" id="season" placeholder="e.g. Spring 2026" oninput="debouncedSave()"></div>
<div class="cover-row"><label>Description</label><textarea id="style-desc" placeholder="Describe your garment..." oninput="debouncedSave()"></textarea></div>
</div>'''
    elif pid == "sketches":
        html += '<div class="sketch-grid" id="sketch-grid"></div>\n<button class="add-row" onclick="addSketch(\'sketches\')">+ Add Sketch</button>\n'
    elif pid == "detail-sketches":
        html += '<div class="sketch-grid" id="detail-grid"></div>\n<button class="add-row" onclick="addSketch(\'details\')">+ Add Detail Sketch</button>\n'
    elif pid == "how-to-measure":
        html += '<div class="sketch-grid" id="htm-grid"></div>\n<table><thead><tr><th>Measurement Point<span class="tip">What you\'re measuring</span></th><th>Start Point<span class="tip">Where the tape starts</span></th><th>End Point<span class="tip">Where the tape ends</span></th><th>How to Measure<span class="tip">Describe the method</span></th><th></th></tr></thead><tbody id="htm-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'htm\')">+ Add Measurement Method</button>\n'
    elif pid == "fabric-placement":
        html += '<table><thead><tr><th>Fabric Name<span class="tip">e.g. Cotton Jersey</span></th><th>Description<span class="tip">Weight, stretch, etc.</span></th><th>Color<span class="tip">Color name or Pantone code</span></th><th>Location<span class="tip">Where on the garment</span></th><th>Notes</th><th></th></tr></thead><tbody id="fab-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'fab\')">+ Add Fabric</button>\n'
    elif pid == "trims":
        html += '<table><thead><tr><th>Type<span class="tip">Zipper, button, label, etc.</span></th><th>Description</th><th>Supplier</th><th>Color</th><th>Size</th><th>Placement<span class="tip">Where on garment</span></th><th></th></tr></thead><tbody id="trim-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'trim\')">+ Add Trim</button>\n'
    elif pid == "bom":
        html += '<table><thead><tr><th>Material<span class="tip">What it is</span></th><th>Description</th><th>Color/Pantone</th><th>Supplier</th><th>Width</th><th>Qty Needed</th><th>Unit<span class="tip">yards, meters, pcs</span></th><th></th></tr></thead><tbody id="bom-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'bom\')">+ Add Material</button>\n'
    elif pid == "measurements":
        html += '<table><thead><tr><th>Measurement Point<span class="tip">e.g. Chest, Length, Sleeve</span></th><th>Sample Size<span class="tip">e.g. M, L</span></th><th>Measurement<span class="tip">The actual number</span></th><th>Tolerance<span class="tip">Acceptable +/- variation</span></th><th>Unit<span class="tip">inches or cm</span></th><th></th></tr></thead><tbody id="meas-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'meas\')">+ Add Measurement</button>\n'
    elif pid == "construction":
        html += '<table><thead><tr><th>Area/Component<span class="tip">e.g. Side seam, Collar</span></th><th>Seam Type</th><th>Notes</th><th></th></tr></thead><tbody id="const-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'const\')">+ Add Note</button>\n'
    elif pid == "stitch":
        html += '<table><thead><tr><th>Area</th><th>Stitch Type</th><th>SPI<span class="tip">Stitches Per Inch - how tight the stitch is</span></th><th>Seam Allowance<span class="tip">Extra fabric beyond stitch line</span></th><th>Construction</th><th>Notes</th><th></th></tr></thead><tbody id="stitch-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'stitch\')">+ Add Stitch Detail</button>\n'
    elif pid == "care-labels":
        html += '<table><thead><tr><th>Care Category<span class="tip">Wash, Dry, Iron, etc.</span></th><th>Instruction<span class="tip">e.g. Machine wash cold, tumble dry low</span></th><th>Language</th><th>Notes</th><th></th></tr></thead><tbody id="care-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'care\')">+ Add Care Instruction</button>\n'
    elif pid == "grading":
        html += '<div style="overflow-x:auto"><table><thead><tr><th>Measurement Point</th><th>XS</th><th>S</th><th>M</th><th>L</th><th>XL</th><th></th></tr></thead><tbody id="grade-body"></tbody></table></div>\n<button class="add-row" onclick="addRow(\'grade\')">+ Add Size</button>\n'
    elif pid == "grading-rules":
        html += '<div class="page-tip">Grading rules = how much each measurement changes between sizes. Example: if chest goes up 2cm from S to M, the rule is +2.</div>\n<table><thead><tr><th>Measurement</th><th>XS to S<span class="tip">Change</span></th><th>S to M</th><th>M to L</th><th>L to XL</th><th>XL to XXL</th><th>Notes</th><th></th></tr></thead><tbody id="grule-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'grule\')">+ Add Rule</button>\n'
    elif pid == "proto-tracking":
        html += '<div class="page-tip"><strong>Sample Tracking:</strong> When the factory sends you a sample garment, you check it and record the actual measurements. P1 = 1st sample, P2 = 2nd sample (after changes), PPS = final pre-production sample.</div>\n<table><thead><tr><th>Measurement</th><th>Your Spec<span class="tip">What you want</span></th><th>P1 Actual<span class="tip">1st sample measurement</span></th><th>P1 Notes</th><th>P2 Actual</th><th>P2 Notes</th><th>PPS Final</th><th>Tolerance<span class="tip">OK range +/-</span></th><th>Status</th><th></th></tr></thead><tbody id="proto-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'proto\')">+ Add Point</button>\n'
    elif pid == "comments":
        html += '''<div class="comments-section"><h3>\U0001f4c8 Pattern/Sizing Changes</h3>
<p class="page-tip" style="margin-bottom:12px">Changes to measurements, fit, or proportions. These go to the pattern maker.</p>
<table><thead><tr><th>Date</th><th>Sample #<span class="tip">Which sample round</span></th><th>What Needs to Change</th><th>What Was Done</th><th>Status</th><th></th></tr></thead><tbody id="pattern-body"></tbody></table>
<button class="add-row" onclick="addRow(\'pattern\')">+ Add Note</button>
</div>
<div class="comments-section"><h3>\U0001fa9a Sewing/Construction Changes</h3>
<p class="page-tip" style="margin-bottom:12px">Changes to stitching, seams, or construction details. These go to the sewing team.</p>
<table><thead><tr><th>Date</th><th>Sample #</th><th>What Needs to Change</th><th>What Was Done</th><th>Status</th><th></th></tr></thead><tbody id="sewing-body"></tbody></table>
<button class="add-row" onclick="addRow(\'sewing\')">+ Add Note</button>
</div>'''
    elif pid == "cost":
        html += '<table><thead><tr><th>Item<span class="tip">Fabric, zipper, labor, etc.</span></th><th>Cost per Unit ($)<span class="tip">Price per piece/yard</span></th><th>Qty Needed</th><th>Subtotal</th><th>Notes</th><th></th></tr></thead><tbody id="cost-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'cost\')">+ Add Cost Item</button>\n<div style="margin-top:16px;background:#fff;border-radius:8px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.08);display:inline-block"><strong>Total cost per garment: $<span id="cost-total">0.00</span></strong></div>\n'
    elif pid == "colorways":
        html += '<table><thead><tr><th>Color Name<span class="tip">e.g. Midnight Blue</span></th><th>Pantone Code<span class="tip">Optional - e.g. 19-4024</span></th><th>Color Picker</th><th>Notes</th><th></th></tr></thead><tbody id="color-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'color\')">+ Add Color</button>\n'
    elif pid == "labels":
        html += '<table><thead><tr><th>Label Type<span class="tip">Main label, size tag, care label</span></th><th>Placement<span class="tip">Where on garment</span></th><th>Size<span class="tip">Dimensions of label</span></th><th>Material<span class="tip">Woven, printed, etc.</span></th><th>Attachment<span class="tip">Sewn in, heat transfer, etc.</span></th><th></th></tr></thead><tbody id="label-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'label\')">+ Add Label</button>\n'
    elif pid == "packaging":
        html += '<table><thead><tr><th>Item<span class="tip">Poly bag, hang tag, box, etc.</span></th><th>Material</th><th>Size/Dimensions</th><th>Qty per Garment</th><th>Notes</th><th></th></tr></thead><tbody id="pack-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'pack\')">+ Add Item</button>\n'
    elif pid == "changelog":
        html += '<table><thead><tr><th>Date</th><th>Version</th><th>What Changed</th><th>Who Changed It</th><th>Status</th><th></th></tr></thead><tbody id="log-body"></tbody></table>\n<button class="add-row" onclick="addRow(\'log\')">+ Add Entry</button>\n'
    
    html += f'<div class="page-num" id="page-num-{pid}"></div>\n'
    html += f'<div class="confidential">CONFIDENTIAL PROPERTY OF <span class="conf-brand">YOUR BRAND</span>. Unauthorized reproduction or disclosure prohibited.</div>\n'
    html += '</div>\n'

# Export overlay
html += """</div></div>
<div class="export-overlay" id="export-overlay">
<div class="export-box"><div class="spinner"></div><h2>Generating PDF...</h2><p id="export-status">Rendering...</p></div>
</div>
<script>
"""

# JavaScript
html += r"""
function eH(s){if(!s)return'';return String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
const SK='easytechpack_v2_1',MI=400;
function gS(){try{return JSON.parse(localStorage.getItem(SK))||{}}catch(e){return{}}}
function sS(d){try{localStorage.setItem(SK,JSON.stringify(d));showSave();updateBadges()}catch(e){alert('Storage full! Try removing some images.')}}
function showSave(){const e=document.getElementById('save-indicator');e.classList.add('show');clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('show'),2000);const s=document.getElementById('save-status');if(s)s.textContent='Saved at '+new Date().toLocaleTimeString()}
let _st;function debouncedSave(){clearTimeout(_st);_st=setTimeout(saveAll,400)}
function gSt(k){return gS()[k]||[]}
function sSt(k,d){const s=gS();s[k]=d;sS(s)}
function cImg(u,cb){const i=new Image();i.onload=function(){const c=document.createElement('canvas');let w=i.width,h=i.height;if(w>MI||h>MI){if(w>h){h=Math.round(h*MI/w);w=MI}else{w=Math.round(w*MI/h);h=MI}}c.width=w;c.height=h;c.getContext('2d').drawImage(i,0,0,w,h);cb(c.toDataURL('image/jpeg',.7))};i.src=u}
function toast(msg,type){const t=document.getElementById('toast');t.textContent=msg;t.className='toast show '+(type||'');setTimeout(()=>t.className='toast',3000)}
let _confirmCb=null;
function showConfirm(title,msg,cb){document.getElementById('confirm-title').textContent=title;document.getElementById('confirm-msg').textContent=msg;document.getElementById('confirm-modal').classList.add('show');_confirmCb=cb;document.getElementById('confirm-ok').onclick=function(){document.getElementById('confirm-modal').classList.remove('show');if(_confirmCb)_confirmCb()}}
function confirmCancel(){document.getElementById('confirm-modal').classList.remove('show')}
function closeWelcome(){document.getElementById('welcome').classList.add('hide');localStorage.setItem(SK+'_welcomed','1')}
function saveAll(){
const s=gS();
['brand-name','style-name','pack-date','pack-version','designer-name','season','style-desc'].forEach(id=>{const el=document.getElementById(id);if(el)s[id.replace(/-/g,'_')]=el.value});
s.logoDataUrl=gS().logoDataUrl;sS(s);updateFileName();updateConfidential()
}
function loadAll(){
const s=gS();
const m={'brand-name':'brand_name','style-name':'style_name','pack-date':'pack_date','pack-version':'pack_version','designer-name':'designer_name','season':'season','style-desc':'style_desc'};
Object.entries(m).forEach(([id,k])=>{if(s[k])document.getElementById(id).value=s[k]});
if(s.logoDataUrl)showLogo(s.logoDataUrl);
if(!localStorage.getItem(SK+'_welcomed'))document.getElementById('welcome').classList.remove('hide');
else document.getElementById('welcome').classList.add('hide');
updateFileName();updateConfidential()
}
function updateFileName(){const b=document.getElementById('brand-name').value||'BRAND';const st=document.getElementById('style-name').value||'STYLE';const d=document.getElementById('pack-date').value||new Date().toISOString().split('T')[0];const el=document.getElementById('file-name');if(el)el.textContent=b.replace(/\s+/g,'-')+'-'+st.replace(/\s+/g,'-')+'-'+d}
function updateConfidential(){const b=document.getElementById('brand-name').value||'YOUR BRAND';document.querySelectorAll('.conf-brand').forEach(el=>el.textContent=b.toUpperCase())}
function updateBadges(){const pages=['cover','sketches','fabric-placement','trims','bom','measurements','construction','stitch','detail-sketches','how-to-measure','care-labels','grading','grading-rules','proto-tracking','comments','cost','colorways','labels','packaging','changelog'];pages.forEach(p=>{const b=document.getElementById('badge-'+p);if(!b)return;const keys={cover:['brand_name'],sketches:['sketches'],details:['details'],fab:['fab'],trim:['trim'],bom:['bom'],meas:['meas'],const:['const'],stitch:['stitch'],htm:['htm'],care:['care'],grade:['grade'],grule:['grule'],proto:['proto'],pattern:['pattern'],sewing:['sewing'],cost:['cost'],color:['color'],label:['label'],pack:['pack'],log:['log']};const k=keys[p]||keys[p.replace(/-/g,'')];if(!k)return;const st=gS();let hasData=false;k.forEach(key=>{if(st[key]&&st[key].length>0)hasData=true});const nav=document.querySelector(`.nav-item[data-page="${p}"]`);if(nav){if(hasData){nav.classList.add('has-data');b.textContent='\u2713'}else{nav.classList.remove('has-data');b.textContent=''}}})}
function handleLogo(input){const f=input.files[0];if(!f)return;const r=new FileReader();r.onload=()=>cImg(r.result,c=>{showLogo(c);const s=gS();s.logoDataUrl=c;sS(s)});r.readAsDataURL(f)}
function showLogo(src){document.getElementById('logo-preview').innerHTML='<img src="'+eH(src)+'" alt="Logo">'}
function toggleSidebar(){document.querySelector('.sidebar').classList.toggle('open');document.querySelector('.sidebar-overlay').classList.toggle('show')}
function newTechPack(){showConfirm('Start New Tech Pack?','This will delete ALL your current data. Consider saving a backup first!',()=>{localStorage.removeItem(SK);location.reload()})}
function saveBackup(){const d=gS();const b=new Blob([JSON.stringify(d,null,2)],{type:'application/json'});const u=URL.createObjectURL(b);const a=document.createElement('a');a.href=u;const bn=document.getElementById('brand-name').value||'backup';const dt=new Date().toISOString().split('T')[0];a.download=bn.replace(/\s+/g,'-')+'-techpack-'+dt+'.json';a.click();URL.revokeObjectURL(u);toast('Backup saved!','success')}
function loadBackup(input){const f=input.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{try{const d=JSON.parse(r.result);localStorage.setItem(SK,JSON.stringify(d));toast('Backup loaded! Reloading...','success');setTimeout(()=>location.reload(),1000)}catch(e){toast('Invalid backup file!','error')}};r.readAsText(f)}
function loadExample(){
showConfirm('Load Example Data?','This will replace your current data with a sample hoodie tech pack.',()=>{
const s={brand_name:'Cool Kid Streetwear',style_name:'Classic Hoodie',pack_date:new Date().toISOString().split('T')[0],pack_version:'v1.0',designer_name:'Alex Chen',season:'Spring 2026',style_desc:'A classic pullover hoodie with kangaroo pocket, ribbed cuffs and hem, and drawstring hood.',
fab:[{name:'French Terry',desc:'350gsm cotton/poly blend, soft brushed interior',color:'Charcoal Grey',location:'Body',notes:'Main body fabric'},{name:'Rib Knit',desc:'1x1 rib, 95% cotton 5% elastane',color:'Charcoal Grey',location:'Cuff',notes:'Cuffs and hem band'},{name:'Jersey',desc:'Lightweight cotton jersey',color:'Charcoal Grey',location:'Hood',notes:'Hood lining'}],
trim:[{type:'Drawstring',desc:'Flat cotton drawstring, 120cm',supplier:'',color:'Black',size:'1cm wide',placement:'Hood'},{type:'Label',desc:'Woven main label',supplier:'',color:'Black/White',size:'5cm x 2cm',placement:'Center back neck'},{type:'Hang Tag',desc:'Branded card hang tag',supplier:'',color:'',size:'8cm x 5cm',placement:'Hood drawstring'}],
bom:[{material:'French Terry',desc:'350gsm',color:'Charcoal Grey',supplier:'',width:'60"',qty:'1.5',unit:'yards'},{material:'Rib Knit',desc:'1x1 rib',color:'Charcoal Grey',supplier:'',width:'36"',qty:'0.3',unit:'yards'},{material:'Drawstring',desc:'Flat cotton',color:'Black',supplier:'',width:'',qty:'1',unit:'pc'},{material:'Thread',desc:'Matching polyester',color:'Charcoal Grey',supplier:'',width:'',qty:'1',unit:'cone'}],
meas:[{point:'Chest (1" below armhole)',size:'M',meas:'24"',tol:'+/- 0.5"',unit:'inches'},{point:'Body Length (HPS to hem)',size:'M',meas:'28"',tol:'+/- 0.5"',unit:'inches'},{point:'Sleeve Length',size:'M',meas:'25"',tol:'+/- 0.5"',unit:'inches'},{point:'Hem Width',size:'M',meas:'18"',tol:'+/- 0.25"',unit:'inches'}],
const:[{area:'Side seams',seam:'Overlocked',notes:'Serged together'},{area:'Shoulder seams',seam:'Plain',notes:'Topstitched'},{area:'Hem',seam:'Folded',notes:'Double needle coverstitch'}],
stitch:[{area:'Side seams',type:'Overlock',spi:'12',allowance:'3/8"',construction:'Overlocked',notes:''},{area:'Hem',type:'Coverstitch',spi:'10',allowance:'1"',construction:'Folded',notes:'Double needle'}],
color:[{name:'Charcoal Grey',pantone:'18-0601',swatch:'#4a4a4a',notes:'Main colorway'},{name:'Black',pantone:'19-0303',swatch:'#1a1a1a',notes:'2nd colorway'}],
label:[{type:'Main Label',placement:'Center back neck',dimensions:'5cm x 2cm',material:'Woven',attachment:'Sewn in'},{type:'Size Tag',placement:'Below main label',dimensions:'3cm x 2cm',material:'Printed',attachment:'Sewn in'},{type:'Care Label',placement:'Left side seam',dimensions:'5cm x 7cm',material:'Printed satin',attachment:'Sewn in'}],
packaging:[{item:'Poly Bag',material:'Clear PE',dimensions:'12" x 16"',qty:'1',notes:'Biodegradable'},{item:'Hang Tag',material:'Card stock',dimensions:'8cm x 5cm',qty:'1',notes:'Branded'}],
grade:[{point:'Chest',xs:'22"',s:'23"',m:'24"',l:'25"',xl:'26"'}],
sS(s);loadAll();renderAll();toast('Example hoodie loaded! \U0001f3af','success')})
}

// Navigation
document.querySelectorAll('.nav-item').forEach(item=>{
item.addEventListener('click',()=>{
document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
item.classList.add('active');
document.getElementById('page-'+item.dataset.page).classList.add('active');
if(window.innerWidth<=768)toggleSidebar()
})});

// Generic table
function renderTable(bid,cols,rows){
const tb=document.getElementById(bid);if(!tb)return;tb.innerHTML='';
rows.forEach((row,i)=>{
const tr=document.createElement('tr');
cols.forEach(c=>{const td=document.createElement('td');
if(c.type==='select'){td.innerHTML='<select onchange="uF(\''+c.s+'\','+i+',\''+c.k+'\',this.value)">'+(c.opts||[]).map(o=>'<option'+(row[c.k]===o?' selected':'')+'>'+o+'</option>').join('')+'</select>'}
else if(c.type==='color'){td.innerHTML='<input type="color" value="'+eH(row[c.k]||'#000000')+'" style="width:40px;height:30px;border:none;padding:0;cursor:pointer" onchange="uF(\''+c.s+'\','+i+',\''+c.k+'\',this.value)">'}
else if(c.type==='textarea'){td.innerHTML='<textarea oninput="uF(\''+c.s+'\','+i+',\''+c.k+'\',this.value)" placeholder="'+eH(c.p||'')+'">'+eH(row[c.k]||'')+'</textarea>'}
else{td.innerHTML='<input type="text" value="'+eH(row[c.k]||'')+'" placeholder="'+eH(c.p||'')+'" oninput="uF(\''+c.s+'\','+i+',\''+c.k+'\',this.value)">'}
tr.appendChild(td)});
const td=document.createElement('td');td.innerHTML='<button class="del-btn" onclick="dR(\''+cols[0].s+'\','+i+')" title="Delete row">&times;</button>';tr.appendChild(td);tb.appendChild(tr)})}
function addRow(t){const d={fab:{name:'',desc:'',color:'',location:'Body',notes:''},trim:{type:'Zipper',desc:'',supplier:'',color:'',size:'',placement:''},bom:{material:'',desc:'',color:'',supplier:'',width:'',qty:'',unit:''},meas:{point:'',size:'',meas:'',tol:'',unit:''},const:{area:'',seam:'Plain',notes:''},stitch:{area:'',type:'Single Needle',spi:'',allowance:'',construction:'Plain',notes:''},htm:{point:'',start:'',end:'',method:''},care:{type:'Wash',instruction:'',language:'EN',notes:''},grade:{point:'',xs:'',s:'',m:'',l:'',xl:''},grule:{point:'',xs_s:'',s_m:'',m_l:'',l_xl:'',xl_xxl:'',notes:''},proto:{point:'',spec:'',p1:'',p1c:'',p2:'',p2c:'',pps:'',tol:'',status:'Pending'},pattern:{date:new Date().toISOString().split('T')[0],proto:'1',comment:'',action:'',status:'Pending'},sewing:{date:new Date().toISOString().split('T')[0],proto:'1',comment:'',action:'',status:'Pending'},cost:{component:'',cost:'',qty:'',notes:''},color:{name:'',pantone:'',swatch:'#000000',notes:''},label:{type:'',placement:'',dimensions:'',material:'',attachment:''},pack:{item:'',material:'',dimensions:'',qty:'',notes:''},log:{date:new Date().toISOString().split('T')[0],version:'',change:'',by:'',status:'Pending'}};const r=gSt(t);r.push({...d[t]});sSt(t,r);renderAll();toast('Row added','info')}
function dR(t,i){showConfirm('Delete this row?','This will remove the data permanently.',()=>{const r=gSt(t);r.splice(i,1);sSt(t,r);renderAll();toast('Row deleted','info')})}
function uF(t,i,k,v){const r=gSt(t);if(r[i])r[i][k]=v;sSt(t,r)}

// Sketches
function addSketch(t){const k=t==='sketches'?'sketches':'details';const r=gSt(k);r.push({image:'',label:'',notes:''});sSt(k,r);renderSketches(t)}
function renderSketches(t){const k=t==='sketches'?'sketches':'details';const gid=t==='sketches'?'sketch-grid':'detail-grid';const g=document.getElementById(gid);if(!g)return;const rows=gSt(k);g.innerHTML='';if(!rows.length){g.innerHTML='<div style="color:#888;font-size:13px;padding:20px">No sketches yet. Click "+ Add Sketch" to upload drawings of your garment.</div>';return}
rows.forEach((r,i)=>{const c=document.createElement('div');c.className='sketch-card';const id=document.createElement('div');id.className='sketch-card-img';id.onclick=()=>document.getElementById('sf-'+t+'-'+i).click();if(r.image){const img=document.createElement('img');img.src=r.image;id.appendChild(img)}else{const sp=document.createElement('span');sp.textContent='\U0001f4f7 Click to upload';id.appendChild(sp)}c.appendChild(id);const fi=document.createElement('input');fi.type='file';fi.accept='image/*';fi.style.display='none';fi.id='sf-'+t+'-'+i;fi.onchange=function(){const f=this.files[0];if(!f)return;const rd=new FileReader();rd.onload=()=>cImg(rd.result,cp=>{const rw=gSt(k);rw[i].image=cp;sSt(k,rw);renderSketches(t)});rd.readAsDataURL(f)};c.appendChild(fi);const ld=document.createElement('div');ld.className='sketch-card-input';const ll=document.createElement('label');ll.textContent='Label';ld.appendChild(ll);const li=document.createElement('input');li.type='text';li.value=r.label||'';li.placeholder='e.g. Front View';li.oninput=function(){const rw=gSt(k);rw[i].label=this.value;sSt(k,rw)};ld.appendChild(li);c.appendChild(ld);const nd=document.createElement('div');nd.className='sketch-card-input';const nl=document.createElement('label');nl.textContent='Notes';nd.appendChild(nl);const ni=document.createElement('input');ni.type='text';ni.value=r.notes||'';ni.placeholder='Any details...';ni.oninput=function(){const rw=gSt(k);rw[i].notes=this.value;sSt(k,rw)};nd.appendChild(ni);c.appendChild(nd);const dd=document.createElement('div');dd.style.padding='8px 12px';dd.style.textAlign='right';const db=document.createElement('button');db.className='del-btn';db.innerHTML='&times;';db.onclick=()=>{showConfirm('Delete sketch?','',()=>{const rw=gSt(k);rw.splice(i,1);sSt(k,rw);renderSketches(t)})};dd.appendChild(db);c.appendChild(dd);g.appendChild(c)})}

function renderColor(){const tb=document.getElementById('color-body');if(!tb)return;const rows=gSt('color');tb.innerHTML='';rows.forEach((r,i)=>{const tr=document.createElement('tr');['name','pantone'].forEach(k=>{const td=document.createElement('td');td.innerHTML='<input value="'+eH(r[k]||'')+'" placeholder="'+(k==='name'?'e.g. Midnight Blue':'e.g. 19-4024 (optional)')+'" oninput="uF(\'color\','+i+',\''+k+'\',this.value)">';tr.appendChild(td)});const sw=document.createElement('td');sw.innerHTML='<input type="color" value="'+eH(r.swatch||'#000000')+'" style="width:40px;height:30px;border:none;padding:0;cursor:pointer" onchange="uF(\'color\','+i+',\'swatch\',this.value)">';tr.appendChild(sw);const nt=document.createElement('td');nt.innerHTML='<input value="'+eH(r.notes||'')+'" placeholder="Notes" oninput="uF(\'color\','+i+',\'notes\',this.value)">';tr.appendChild(nt);const dt=document.createElement('td');const db=document.createElement('button');db.className='del-btn';db.innerHTML='&times;';db.onclick=()=>dR('color',i);dt.appendChild(db);tr.appendChild(dt);tb.appendChild(tr)})}

function calcCost(){const r=gSt('cost');const t=r.reduce((s,x)=>s+(parseFloat(x.cost)||0)*(parseInt(x.qty)||0),0);const e=document.getElementById('cost-total');if(e)e.textContent=t.toFixed(2)}

function renderAll(){
renderTable('fab-body',[{k:'name',p:'e.g. French Terry',fn:'uF',s:'fab'},{k:'desc',p:'Weight, feel',fn:'uF',s:'fab'},{k:'color',p:'Color name',fn:'uF',s:'fab'},{k:'location',p:'',fn:'uF',s:'fab',type:'select',opts:['Body','Lining','Hood','Hood Lining','Pocket','Pocket Lining','Cuff','Hem','Collar','Trim','Other']},{k:'notes',p:'Notes',fn:'uF',s:'fab'}],gSt('fab'));
renderTable('trim-body',[{k:'type',p:'',fn:'uF',s:'trim',type:'select',opts:['Drawstring','Zipper','Button','Snap','Hook','Elastic','Label','Hang Tag','Embroidery','Patch','Rivet','Grommet','Other']},{k:'desc',p:'Description',fn:'uF',s:'trim'},{k:'supplier',p:'Supplier',fn:'uF',s:'trim'},{k:'color',p:'Color',fn:'uF',s:'trim'},{k:'size',p:'Size',fn:'uF',s:'trim'},{k:'placement',p:'Where on garment',fn:'uF',s:'trim'}],gSt('trim'));
renderTable('bom-body',[{k:'material',p:'e.g. Cotton',fn:'uF',s:'bom'},{k:'desc',p:'Description',fn:'uF',s:'bom'},{k:'color',p:'Color',fn:'uF',s:'bom'},{k:'supplier',p:'Supplier',fn:'uF',s:'bom'},{k:'width',p:'e.g. 60"',fn:'uF',s:'bom'},{k:'qty',p:'Amount',fn:'uF',s:'bom'},{k:'unit',p:'yards/m/p',fn:'uF',s:'bom'}],gSt('bom'));
renderTable('meas-body',[{k:'point',p:'e.g. Chest width',fn:'uF',s:'meas'},{k:'size',p:'e.g. M',fn:'uF',s:'meas'},{k:'meas',p:'e.g. 24"',fn:'uF',s:'meas'},{k:'tol',p:'+/- 0.5"',fn:'uF',s:'meas'},{k:'unit',p:'in/cm',fn:'uF',s:'meas'}],gSt('meas'));
renderTable('const-body',[{k:'area',p:'e.g. Side seam',fn:'uF',s:'const'},{k:'seam',p:'',fn:'uF',s:'const',type:'select',opts:['Plain','Overlocked','Felled','Bound','French','Lapped','Other']},{k:'notes',p:'Notes',fn:'uF',s:'const'}],gSt('const'));
renderTable('stitch-body',[{k:'area',p:'Area',fn:'uF',s:'stitch'},{k:'type',p:'',fn:'uF',s:'stitch',type:'select',opts:['Single Needle','Double Needle','Overlock','Flatlock','Chain','Safety','Bartack','Coverstitch','Blind Hem','Other']},{k:'spi',p:'12-14',fn:'uF',s:'stitch'},{k:'allowance',p:'1/2"',fn:'uF',s:'stitch'},{k:'construction',p:'',fn:'uF',s:'stitch',type:'select',opts:['Plain','Overlocked','Felled','Bound','French','Other']},{k:'notes',p:'Notes',fn:'uF',s:'stitch'}],gSt('stitch'));
renderTable('htm-body',[{k:'point',p:'e.g. Chest',fn:'uF',s:'htm'},{k:'start',p:'Where tape starts',fn:'uF',s:'htm'},{k:'end',p:'Where tape ends',fn:'uF',s:'htm'},{k:'method',p:'How to measure',fn:'uF',s:'htm'}],gSt('htm'));
renderTable('care-body',[{k:'type',p:'',fn:'uF',s:'care',type:'select',opts:['Wash','Dry','Iron','Bleach','Dry Clean','Special Care']},{k:'instruction',p:'e.g. Machine wash cold',fn:'uF',s:'care'},{k:'language',p:'EN',fn:'uF',s:'care'},{k:'notes',p:'Notes',fn:'uF',s:'care'}],gSt('care'));
renderTable('grade-body',[{k:'point',p:'Measurement',fn:'uF',s:'grade'},{k:'xs',p:'',fn:'uF',s:'grade'},{k:'s',p:'',fn:'uF',s:'grade'},{k:'m',p:'',fn:'uF',s:'grade'},{k:'l',p:'',fn:'uF',s:'grade'},{k:'xl',p:'',fn:'uF',s:'grade'}],gSt('grade'));
renderTable('grule-body',[{k:'point',p:'Measurement',fn:'uF',s:'grule'},{k:'xs_s',p:'+/-',fn:'uF',s:'grule'},{k:'s_m',p:'',fn:'uF',s:'grule'},{k:'m_l',p:'',fn:'uF',s:'grule'},{k:'l_xl',p:'',fn:'uF',s:'grule'},{k:'xl_xxl',p:'',fn:'uF',s:'grule'},{k:'notes',p:'Notes',fn:'uF',s:'grule'}],gSt('grule'));
renderTable('proto-body',[{k:'point',p:'Measurement',fn:'uF',s:'proto'},{k:'spec',p:'What you want',fn:'uF',s:'proto'},{k:'p1',p:'1st sample',fn:'uF',s:'proto'},{k:'p1c',p:'Notes',fn:'uF',s:'proto'},{k:'p2',p:'2nd sample',fn:'uF',s:'proto'},{k:'p2c',p:'Notes',fn:'uF',s:'proto'},{k:'pps',p:'Final',fn:'uF',s:'proto'},{k:'tol',p:'+/-',fn:'uF',s:'proto'},{k:'status',p:'',fn:'uF',s:'proto',type:'select',opts:['Pending','Received','Approved','Rejected']}],gSt('proto'));
renderTable('pattern-body',[{k:'date',p:'Date',fn:'uF',s:'pattern'},{k:'proto',p:'1, 2, PPS',fn:'uF',s:'pattern'},{k:'comment',p:'What needs changing',fn:'uF',s:'pattern',type:'textarea'},{k:'action',p:'What was done',fn:'uF',s:'pattern',type:'textarea'},{k:'status',p:'',fn:'uF',s:'pattern',type:'select',opts:['Pending','In Progress','Done']}],gSt('pattern'));
renderTable('sewing-body',[{k:'date',p:'Date',fn:'uF',s:'sewing'},{k:'proto',p:'1, 2, PPS',fn:'uF',s:'sewing'},{k:'comment',p:'What needs changing',fn:'uF',s:'sewing',type:'textarea'},{k:'action',p:'What was done',fn:'uF',s:'sewing',type:'textarea'},{k:'status',p:'',fn:'uF',s:'sewing',type:'select',opts:['Pending','In Progress','Done']}],gSt('sewing'));
const ct=document.getElementById('cost-body');if(ct){const r=gSt('cost');ct.innerHTML='';r.forEach((x,i)=>{const sub=(parseFloat(x.cost)||0)*(parseInt(x.qty)||0);const tr=document.createElement('tr');tr.innerHTML='<td><input value="'+eH(x.component||'')+'" placeholder="e.g. Fabric" oninput="uF(\'cost\','+i+',\'component\',this.value)"></td><td><input value="'+eH(x.cost||'')+'" placeholder="0.00" type="number" step="0.01" oninput="uF(\'cost\','+i+',\'cost\',this.value)"></td><td><input value="'+eH(x.qty||'')+'" placeholder="1" type="number" oninput="uF(\'cost\','+i+',\'qty\',this.value)"></td><td>$'+sub.toFixed(2)+'</td><td><input value="'+eH(x.notes||'')+'" placeholder="Notes" oninput="uF(\'cost\','+i+',\'notes\',this.value)"></td><td><button class="del-btn" onclick="dR(\'cost\','+i+')">&times;</button></td>';ct.appendChild(tr)});calcCost()}
renderColor();
renderTable('label-body',[{k:'type',p:'e.g. Main label',fn:'uF',s:'label'},{k:'placement',p:'Center back neck',fn:'uF',s:'label'},{k:'dimensions',p:'5cm x 2cm',fn:'uF',s:'label'},{k:'material',p:'Woven/Printed',fn:'uF',s:'label'},{k:'attachment',p:'Sewn in',fn:'uF',s:'label'}],gSt('label'));
renderTable('pack-body',[{k:'item',p:'e.g. Poly bag',fn:'uF',s:'pack'},{k:'material',p:'Clear PE',fn:'uF',s:'pack'},{k:'dimensions',p:'12" x 16"',fn:'uF',s:'pack'},{k:'qty',p:'1',fn:'uF',s:'pack'},{k:'notes',p:'Notes',fn:'uF',s:'pack'}],gSt('pack'));
renderTable('log-body',[{k:'date',p:'Date',fn:'uF',s:'log'},{k:'version',p:'v1.0',fn:'uF',s:'log'},{k:'change',p:'What changed',fn:'uF',s:'log'},{k:'by',p:'Who',fn:'uF',s:'log'},{k:'status',p:'',fn:'uF',s:'log',type:'select',opts:['Pending','In Progress','Done']}],gSt('log'));
renderSketches('sketches');renderSketches('details');updateBadges()}

// PDF Export
async function exportPDF(){
if(typeof html2canvas==='undefined'){toast('PDF library not loaded. Check internet.','error');return}
const ov=document.getElementById('export-overlay');const st=document.getElementById('export-status');
ov.classList.add('show');
try{const{jsPDF}=window.jspdf;const pdf=new jsPDF('p','mm','a4');const pw=210,ph=297,mg=15;
const pids=Array.from(document.querySelectorAll('.page')).map(p=>p.id.replace('page-',''));
for(let pi=0;pi<pids.length;pi++){st.textContent='Rendering: '+pids[pi]+' ('+(pi+1)+'/'+pids.length+')';
const el=document.getElementById('page-'+pids[pi]);el.style.display='block';el.style.position='absolute';el.style.left='-9999px';el.style.width='800px';el.style.background='#fff';el.style.padding='20px';
try{const cv=await html2canvas(el,{scale:1.5,useCORS:true,logging:false,backgroundColor:'#ffffff'});
const id=cv.toDataURL('image/jpeg',.95);const iw=pw-mg*2;const ih=(cv.height*iw)/cv.width;
if(pi>0)pdf.addPage();pdf.setFontSize(8);pdf.setTextColor(150);const b=document.getElementById('brand-name').value||'EasyTechPack';const sn=document.getElementById('style-name').value||'';pdf.text(b+' - '+sn+' - Page '+(pi+1),mg,10);
if(ih>ph-mg*2){const sp=Math.ceil(ih/(ph-mg*2));for(let s=0;s<sp;s++){if(s>0){pdf.addPage();pdf.setFontSize(8);pdf.setTextColor(150)}const sy=s*(ph-mg*2)*(cv.width/iw);const sh=Math.min((ph-mg*2)*(cv.width/iw),cv.height-sy);const tc=document.createElement('canvas');tc.width=cv.width;tc.height=sh;tc.getContext('2d').drawImage(cv,0,sy,cv.width,sh,0,0,cv.width,sh);const ti=tc.toDataURL('image/jpeg',.95);pdf.addImage(ti,'JPEG',mg,15,iw,Math.min((sh*iw)/cv.width,ph-30))}}else{pdf.addImage(id,'JPEG',mg,15,iw,ih)}}catch(e){console.error('PDF error:',pids[pi])}
el.style.display='';el.style.position='';el.style.left='';el.style.width='';el.style.background='';el.style.padding=''}
const bn=(document.getElementById('brand-name').value||'TechPack').replace(/\s+/g,'-');const sn2=(document.getElementById('style-name').value||'Style').replace(/\s+/g,'-');pdf.save(bn+'_'+sn2+'.pdf');toast('PDF downloaded! \u2705','success')}catch(e){toast('Export failed: '+e.message,'error')}
ov.classList.remove('show')}

function init(){loadAll();renderAll();if(!document.getElementById('pack-date').value){document.getElementById('pack-date').value=new Date().toISOString().split('T')[0];saveAll()}}
init();
</script></body></html>
"""

with open(OUT, 'w') as f:
    f.write(html)
print(f"Written {len(html)} bytes to {OUT}")
