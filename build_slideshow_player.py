import os
import io
import base64
from PIL import Image

HERON_SRC = r"c:\Users\j-a-b\.gemini\antigravity\scratch\food_tracker\extracted_kitchen\heron_luminous.png"
SITE_ROOT = r"c:\Users\j-a-b\.gemini\antigravity\scratch\google_site"
OUT_HTML = os.path.join(SITE_ROOT, "Norgem_Family_Slideshow_Player.html")


def get_heron_data_uri():
    with Image.open(HERON_SRC) as im:
        im.thumbnail((280, 280), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="PNG", optimize=True)
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        return f"data:image/png;base64,{b64}"


def build_slideshow_player():
    heron_uri = get_heron_data_uri()

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Norgem Enterprises — Family Decade Slideshow Player</title>
<link rel="icon" href="{heron_uri}">
<style>
  * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    user-select: none;
    -webkit-user-select: none;
  }}

  html, body {{
    width: 100vw;
    height: 100vh;
    background-color: #030712;
    color: #f8fafc;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    overflow: hidden;
  }}

  /* ==========================================================================
     LAUNCHER SCREEN (Norgem Enterprises Blue Heron Theme)
     ========================================================================== */
  #launcher-screen {{
    width: 100vw;
    height: 100vh;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 24px 20px;
    background:
      radial-gradient(circle at 50% 22%, rgba(14, 116, 144, 0.22) 0%, rgba(15, 23, 42, 0.55) 42%, #020617 80%);
  }}

  .launcher-card {{
    width: 100%;
    max-width: 880px;
    background: rgba(15, 23, 42, 0.82);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(56, 189, 248, 0.28);
    border-radius: 24px;
    padding: 28px 32px;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.75), 0 0 40px rgba(56, 189, 248, 0.08);
    margin: auto 0;
  }}

  .brand-header {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    margin-bottom: 22px;
  }}

  .heron-logo {{
    width: 120px;
    height: 120px;
    object-fit: contain;
    margin-bottom: 10px;
    animation: sentinel-pulse 7s ease-in-out infinite;
  }}

  @keyframes sentinel-pulse {{
    0%, 100% {{
      filter: brightness(0.88) drop-shadow(0 0 18px rgba(56, 189, 248, 0.28));
      transform: scale(1.0);
    }}
    50% {{
      filter: brightness(1.0) drop-shadow(0 0 32px rgba(56, 189, 248, 0.52));
      transform: scale(1.02);
    }}
  }}

  .brand-title {{
    font-size: 1.65rem;
    font-weight: 800;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #ffffff;
  }}

  .brand-subtitle {{
    font-size: 0.92rem;
    color: #38bdf8;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 600;
    margin-top: 3px;
  }}

  .step-box {{
    background: rgba(2, 6, 23, 0.65);
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-radius: 16px;
    padding: 18px 20px;
    margin-bottom: 16px;
  }}

  .step-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 12px;
  }}

  .step-title {{
    font-size: 1rem;
    font-weight: 700;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 10px;
  }}

  .step-badge {{
    width: 26px;
    height: 26px;
    border-radius: 50%;
    background: #0284c7;
    color: #ffffff;
    font-size: 0.82rem;
    font-weight: 800;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }}

  .folder-btn {{
    background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
    color: #ffffff;
    border: 1px solid #38bdf8;
    padding: 10px 20px;
    border-radius: 12px;
    font-size: 0.95rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }}

  .folder-btn:hover {{
    background: linear-gradient(135deg, #0369a1 0%, #075985 100%);
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.35);
    transform: translateY(-1px);
  }}

  .status-pill {{
    font-size: 0.85rem;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 999px;
    background: rgba(16, 185, 129, 0.15);
    color: #34d399;
    border: 1px solid rgba(16, 185, 129, 0.35);
  }}

  /* Mode & Decade Selector Buttons */
  .mode-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 14px;
  }}

  .random-btn {{
    flex: 1;
    min-width: 220px;
    padding: 13px 18px;
    border-radius: 14px;
    font-size: 1rem;
    font-weight: 800;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    background: rgba(30, 41, 59, 0.9);
    color: #cbd5e1;
    border: 2px solid rgba(148, 163, 184, 0.28);
  }}

  .random-btn.active {{
    background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    color: #020617;
    border-color: #fde68a;
    box-shadow: 0 0 24px rgba(245, 158, 11, 0.45);
  }}

  .decade-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(135px, 1fr));
    gap: 10px;
  }}

  .decade-btn {{
    padding: 11px 12px;
    border-radius: 12px;
    font-size: 0.92rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.18s ease;
    background: rgba(30, 41, 59, 0.75);
    color: #cbd5e1;
    border: 2px solid rgba(148, 163, 184, 0.22);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}

  .decade-btn:hover:not(:disabled) {{
    border-color: rgba(56, 189, 248, 0.6);
    color: #ffffff;
  }}

  .decade-btn.active {{
    background: linear-gradient(135deg, #0d9488 0%, #0f766e 100%);
    color: #ffffff;
    border-color: #5eead4;
    box-shadow: 0 0 18px rgba(20, 184, 166, 0.45);
  }}

  .decade-btn:disabled {{
    opacity: 0.35;
    cursor: not-allowed;
  }}

  .decade-count {{
    font-size: 0.75rem;
    padding: 2px 7px;
    border-radius: 999px;
    background: rgba(0, 0, 0, 0.35);
    color: #e2e8f0;
  }}

  /* Launch Controls Bar */
  .launch-row {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-top: 18px;
    padding-top: 18px;
    border-top: 1px solid rgba(148, 163, 184, 0.2);
  }}

  .settings-group {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 14px;
    font-size: 0.88rem;
    color: #cbd5e1;
  }}

  .settings-select {{
    background: #0f172a;
    color: #f8fafc;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 6px 10px;
    font-size: 0.88rem;
    font-weight: 600;
  }}

  .go-btn {{
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: #ffffff;
    border: 2px solid #6ee7b7;
    padding: 14px 38px;
    border-radius: 16px;
    font-size: 1.2rem;
    font-weight: 900;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 0.22s ease;
    box-shadow: 0 10px 28px rgba(16, 185, 129, 0.4);
    display: inline-flex;
    align-items: center;
    gap: 10px;
  }}

  .go-btn:hover:not(:disabled) {{
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 14px 36px rgba(16, 185, 129, 0.6);
  }}

  .go-btn:disabled {{
    opacity: 0.4;
    cursor: not-allowed;
    box-shadow: none;
  }}

  .cast-tip {{
    text-align: center;
    font-size: 0.8rem;
    color: #94a3b8;
    margin-top: 14px;
  }}

  /* ==========================================================================
     FULL-SCREEN SLIDESHOW STAGE (For Smart TV Casting)
     ========================================================================== */
  #slideshow-stage {{
    position: fixed;
    inset: 0;
    background-color: #000000;
    z-index: 100;
    display: none;
    align-items: center;
    justify-content: center;
  }}

  #slideshow-stage.active {{
    display: flex;
  }}

  #slideshow-stage.hide-cursor {{
    cursor: none;
  }}

  .slide-img {{
    position: absolute;
    inset: 0;
    width: 100vw;
    height: 100vh;
    object-fit: contain;
    opacity: 0;
    transition: opacity 0.9s ease-in-out;
    padding: 12px;
  }}

  .slide-img.visible {{
    opacity: 1;
  }}

  /* Subtle Corner Badge */
  .tv-badge {{
    position: absolute;
    top: 24px;
    left: 28px;
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(2, 6, 23, 0.65);
    backdrop-filter: blur(10px);
    padding: 8px 16px;
    border-radius: 999px;
    border: 1px solid rgba(56, 189, 248, 0.3);
    z-index: 110;
    transition: opacity 0.4s ease;
  }}

  /* Auto-hiding bottom HUD bar */
  .tv-hud {{
    position: absolute;
    bottom: 28px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(14px);
    padding: 10px 20px;
    border-radius: 999px;
    border: 1px solid rgba(56, 189, 248, 0.35);
    z-index: 110;
    transition: opacity 0.4s ease;
  }}

  .tv-hud.hidden-hud, .tv-badge.hidden-hud {{
    opacity: 0;
    pointer-events: none;
  }}

  .hud-btn {{
    background: rgba(30, 41, 59, 0.9);
    color: #f8fafc;
    border: 1px solid rgba(148, 163, 184, 0.3);
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.15s ease;
  }}

  .hud-btn:hover {{
    background: #0284c7;
    border-color: #38bdf8;
  }}
</style>
</head>
<body>

<!-- Optional automatic online manifest loader when previewed directly on the website -->
<script src="assets/img/HaddadArchive/manifest.js?v=mat1" onerror=""></script>

<div id="launcher-screen">
  <div class="launcher-card">
    <!-- Norgem Enterprises & Blue Heron Header -->
    <div class="brand-header">
      <img src="{heron_uri}" alt="Norgem Enterprises Blue Heron" class="heron-logo">
      <div class="brand-title">Norgem Enterprises</div>
      <div class="brand-subtitle">Haddad Family Decade Slideshow &amp; Smart TV Viewer</div>
    </div>

    <!-- Step 1: Load Downloaded Folder (or Auto-Loaded Archive) -->
    <div class="step-box">
      <div class="step-header">
        <div class="step-title">
          <span class="step-badge">1</span>
          <span>Photo Source Folder</span>
        </div>
        <span id="source-status-pill" class="status-pill">No folder loaded yet</span>
      </div>
      <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:12px;">
        <p style="font-size:0.88rem; color:#94a3b8; max-width:520px; line-height:1.45;">
          After unzipping your downloaded Haddad Family photos, click <strong>Load Downloaded Photo Folder</strong> and select your unzipped folder. It automatically detects all Decade subfolders!
        </p>
        <div>
          <input type="file" id="folder-input" webkitdirectory directory multiple style="display:none" onchange="handleFolderSelect(event)">
          <button class="folder-btn" onclick="document.getElementById('folder-input').click()">
            <span>📂 Load Downloaded Photo Folder</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Step 2: Pick Random OR Highlight Any Number of Decades -->
    <div class="step-box">
      <div class="step-header">
        <div class="step-title">
          <span class="step-badge">2</span>
          <span>Pick <strong>Random Shuffle</strong> OR Select One or More <strong>Decades</strong> (Stay Highlighted)</span>
        </div>
        <span id="selection-summary" style="font-size:0.82rem; color:#38bdf8; font-weight:700;"></span>
      </div>

      <!-- Random All Button vs. Shuffle Selected Toggle -->
      <div class="mode-row">
        <button id="btn-random-all" class="random-btn active" onclick="activateRandomAllMode()">
          <span>🎲 RANDOM (All Decades Shuffle)</span>
        </button>
        <button id="btn-select-all-decades" class="random-btn" style="flex:0.6;" onclick="highlightAllDecades()">
          <span>☑️ Highlight All Decades</span>
        </button>
      </div>

      <!-- Decade Buttons (Stay Highlighted When Clicked) -->
      <div id="decade-buttons-grid" class="decade-grid">
        <!-- Populated dynamically -->
      </div>
    </div>

    <!-- Step 3: Interval & GO Button -->
    <div class="launch-row">
      <div class="settings-group">
        <label>
          Slide Speed:
          <select id="slide-interval" class="settings-select">
            <option value="4000">4 Seconds</option>
            <option value="6000" selected>6 Seconds (Recommended)</option>
            <option value="10000">10 Seconds</option>
            <option value="15000">15 Seconds</option>
          </select>
        </label>
        <label style="display:inline-flex; align-items:center; gap:6px; cursor:pointer;">
          <input type="checkbox" id="chk-shuffle-selected" checked style="width:16px; height:16px;">
          <span>Shuffle Order</span>
        </label>
      </div>

      <button id="btn-go" class="go-btn" onclick="startSlideshow()">
        <span>▶ GO (Full Screen)</span>
      </button>
    </div>

    <div class="cast-tip">
      💡 <strong>Smart TV Casting Tip:</strong> In Google Chrome, click the <strong>&#8942;</strong> menu (top-right) &rarr; <strong>Save and share</strong> &rarr; <strong>Cast...</strong> to beam this full-screen slideshow directly to your Smart TV.
    </div>
  </div>

  <div style="font-size:0.78rem; color:#64748b; text-align:center; padding-top:12px;">
    &copy; 2026 Norgem Enterprises &bull; James Allen Bates &bull; Sovereign Family Archival Viewer
  </div>
</div>

<!-- FULL-SCREEN SLIDESHOW VIEWER -->
<div id="slideshow-stage" onclick="handleStageClick(event)">
  <img id="slide-a" class="slide-img" src="" alt="Slide A">
  <img id="slide-b" class="slide-img" src="" alt="Slide B">

  <!-- Top-Left Decade & Norgem Badge -->
  <div id="tv-badge" class="tv-badge">
    <img src="{heron_uri}" alt="Heron" style="width:28px; height:28px; object-fit:contain;">
    <span id="tv-decade-label" style="font-weight:800; color:#38bdf8; font-size:0.95rem; letter-spacing:0.05em;">1950s</span>
    <span style="color:#64748b;">|</span>
    <span id="tv-photo-name" style="font-size:0.82rem; color:#cbd5e1;"></span>
    <span id="tv-counter" style="font-size:0.78rem; color:#94a3b8;"></span>
  </div>

  <!-- Bottom Floating Remote Control HUD -->
  <div id="tv-hud" class="tv-hud" onclick="event.stopPropagation()">
    <button class="hud-btn" onclick="stopSlideshow()">&larr; Change Decades</button>
    <button class="hud-btn" onclick="prevSlide()">&#10094; Prev</button>
    <button id="btn-pause-resume" class="hud-btn" onclick="togglePause()">⏸ Pause</button>
    <button class="hud-btn" onclick="nextSlide()">Next &#10095;</button>
    <button class="hud-btn" onclick="toggleFullscreen()">⛶ Full Screen</button>
  </div>
</div>

<script>
(function() {{
  const KNOWN_DECADES = [
    "Pre-1940s", "1940s", "1950s", "1960s", "1970s",
    "1980s", "1990s", "2000s", "2010s", "2020s", "Highlights"
  ];

  let allPhotos = []; // Each item: {{ decade, name, url }}
  let decadeCounts = {{}};
  let randomAllMode = true;
  let highlightedDecades = new Set();

  // Slideshow state
  let playlist = [];
  let currentIndex = 0;
  let slideTimer = null;
  let isPaused = false;
  let activeImgSlot = "a";
  let hudTimeout = null;

  function init() {{
    // If opened online or inside the website folder where window.HADDAD_ARCHIVE_MANIFEST is available, pre-load it!
    if (window.HADDAD_ARCHIVE_MANIFEST && Array.isArray(window.HADDAD_ARCHIVE_MANIFEST.photos)) {{
      allPhotos = window.HADDAD_ARCHIVE_MANIFEST.photos.map(p => ({{
        decade: p.decade,
        name: p.name,
        url: p.full + "?v=mat1"
      }}));
      recalcDecadeCounts();
      document.getElementById("source-status-pill").textContent =
        `✓ Ready: ${{allPhotos.length.toLocaleString()}} Archive Photos Detected`;
    }} else {{
      recalcDecadeCounts();
    }}
    renderDecadeButtons();
    updateSelectionSummary();
  }}

  function recalcDecadeCounts() {{
    decadeCounts = {{}};
    KNOWN_DECADES.forEach(d => decadeCounts[d] = 0);
    allPhotos.forEach(p => {{
      decadeCounts[p.decade] = (decadeCounts[p.decade] || 0) + 1;
    }});
  }}

  window.handleFolderSelect = function(event) {{
    const files = Array.from(event.target.files || []);
    const imageFiles = files.filter(f => /\\.(jpe?g|png|webp)$/i.test(f.name));
    if (imageFiles.length === 0) {{
      alert("No photo files (.jpg, .png) were found in the selected folder.");
      return;
    }}

    // Revoke previous object URLs if any
    allPhotos.forEach(p => {{
      if (p.isBlob && p.url) URL.revokeObjectURL(p.url);
    }});

    allPhotos = imageFiles.map(f => {{
      const rel = f.webkitRelativePath || f.name;
      const parts = rel.split("/");
      let detectedDecade = "Other";
      for (const part of parts) {{
        const match = KNOWN_DECADES.find(d => d.toLowerCase() === part.toLowerCase());
        if (match) {{
          detectedDecade = match;
          break;
        }}
      }}
      if (detectedDecade === "Other") {{
        // Check filename pattern Photo_1950s_...
        const m = f.name.match(/(Pre-1940s|1940s|1950s|1960s|1970s|1980s|1990s|2000s|2010s|2020s)/i);
        if (m) detectedDecade = m[1];
      }}
      return {{
        decade: detectedDecade,
        name: f.name,
        url: URL.createObjectURL(f),
        isBlob: true
      }};
    }});

    recalcDecadeCounts();
    document.getElementById("source-status-pill").textContent =
      `✓ Loaded ${{allPhotos.length.toLocaleString()}} Photos from Folder`;

    // Default to Random All mode when a new folder is loaded
    randomAllMode = true;
    highlightedDecades.clear();
    renderDecadeButtons();
    updateSelectionSummary();
  }};

  window.activateRandomAllMode = function() {{
    randomAllMode = true;
    highlightedDecades.clear();
    document.getElementById("chk-shuffle-selected").checked = true;
    renderDecadeButtons();
    updateSelectionSummary();
  }};

  window.highlightAllDecades = function() {{
    randomAllMode = false;
    highlightedDecades.clear();
    Object.keys(decadeCounts).forEach(d => {{
      if (decadeCounts[d] > 0) highlightedDecades.add(d);
    }});
    renderDecadeButtons();
    updateSelectionSummary();
  }};

  window.toggleDecadeHighlight = function(dec) {{
    randomAllMode = false;
    if (highlightedDecades.has(dec)) {{
      highlightedDecades.delete(dec);
      if (highlightedDecades.size === 0) {{
        randomAllMode = true;
      }}
    }} else {{
      highlightedDecades.add(dec);
    }}
    renderDecadeButtons();
    updateSelectionSummary();
  }};

  function renderDecadeButtons() {{
    const randomBtn = document.getElementById("btn-random-all");
    if (randomAllMode) {{
      randomBtn.classList.add("active");
    }} else {{
      randomBtn.classList.remove("active");
    }}

    const grid = document.getElementById("decade-buttons-grid");
    const decadesToShow = Object.keys(decadeCounts).filter(d => KNOWN_DECADES.includes(d) || decadeCounts[d] > 0);

    let html = "";
    decadesToShow.forEach(dec => {{
      const count = decadeCounts[dec] || 0;
      if (count === 0 && dec === "2020s") return;
      const isHighlighted = !randomAllMode && highlightedDecades.has(dec);
      const disabledAttr = (allPhotos.length > 0 && count === 0) ? "disabled" : "";
      html += `
        <button class="decade-btn ${{isHighlighted ? 'active' : ''}}" ${{disabledAttr}} onclick="toggleDecadeHighlight('${{dec}}')">
          <span>${{dec}}</span>
          <span class="decade-count">${{count.toLocaleString()}}</span>
        </button>
      `;
    }});
    grid.innerHTML = html;
  }}

  function updateSelectionSummary() {{
    const el = document.getElementById("selection-summary");
    const goBtn = document.getElementById("btn-go");
    if (allPhotos.length === 0) {{
      el.textContent = "Load your downloaded photo folder in Step 1 to begin";
      goBtn.disabled = true;
      return;
    }}
    goBtn.disabled = false;
    if (randomAllMode) {{
      el.textContent = `Mode: Random Shuffle Across All ${{allPhotos.length.toLocaleString()}} Photos`;
    }} else {{
      const list = Array.from(highlightedDecades);
      const count = allPhotos.filter(p => highlightedDecades.has(p.decade)).length;
      el.textContent = `Highlighted: ${{list.join(", ")}} (${{count.toLocaleString()}} photos)`;
    }}
  }}

  function shuffleArray(arr) {{
    const copy = arr.slice();
    for (let i = copy.length - 1; i > 0; i--) {{
      const j = Math.floor(Math.random() * (i + 1));
      const tmp = copy[i];
      copy[i] = copy[j];
      copy[j] = tmp;
    }}
    return copy;
  }}

  window.startSlideshow = function() {{
    if (allPhotos.length === 0) {{
      alert("Please load your downloaded photo folder in Step 1 first.");
      return;
    }}

    if (randomAllMode) {{
      playlist = shuffleArray(allPhotos);
    }} else {{
      const subset = allPhotos.filter(p => highlightedDecades.has(p.decade));
      const shouldShuffle = document.getElementById("chk-shuffle-selected").checked;
      playlist = shouldShuffle ? shuffleArray(subset) : subset;
    }}

    if (playlist.length === 0) {{
      alert("No photos found in the highlighted decades.");
      return;
    }}

    currentIndex = 0;
    isPaused = false;
    document.getElementById("btn-pause-resume").textContent = "⏸ Pause";

    const stage = document.getElementById("slideshow-stage");
    stage.classList.add("active");

    // Request browser full-screen so it fills the TV/Monitor cleanly
    if (document.documentElement.requestFullscreen) {{
      document.documentElement.requestFullscreen().catch(() => {{}});
    }}

    showSlide(0);
    scheduleNextSlide();
    wakeHud();
  }};

  function showSlide(idx) {{
    if (playlist.length === 0) return;
    currentIndex = (idx + playlist.length) % playlist.length;
    const item = playlist[currentIndex];

    const imgA = document.getElementById("slide-a");
    const imgB = document.getElementById("slide-b");

    if (activeImgSlot === "a") {{
      imgB.src = item.url;
      imgB.onload = () => {{
        imgB.classList.add("visible");
        imgA.classList.remove("visible");
        activeImgSlot = "b";
      }};
    }} else {{
      imgA.src = item.url;
      imgA.onload = () => {{
        imgA.classList.add("visible");
        imgB.classList.remove("visible");
        activeImgSlot = "a";
      }};
    }}

    document.getElementById("tv-decade-label").textContent = item.decade;
    document.getElementById("tv-photo-name").textContent = item.name.replace(/\\.[^.]+$/, "");
    document.getElementById("tv-counter").textContent = `(${{currentIndex + 1}} / ${{playlist.length.toLocaleString()}})`;
  }}

  function scheduleNextSlide() {{
    if (slideTimer) clearInterval(slideTimer);
    const ms = parseInt(document.getElementById("slide-interval").value, 10) || 6000;
    slideTimer = setInterval(() => {{
      if (!isPaused) {{
        showSlide(currentIndex + 1);
      }}
    }}, ms);
  }}

  window.nextSlide = function() {{
    showSlide(currentIndex + 1);
    scheduleNextSlide();
  }};

  window.prevSlide = function() {{
    showSlide(currentIndex - 1);
    scheduleNextSlide();
  }};

  window.togglePause = function() {{
    isPaused = !isPaused;
    document.getElementById("btn-pause-resume").textContent = isPaused ? "▶ Resume" : "⏸ Pause";
  }};

  window.toggleFullscreen = function() {{
    if (!document.fullscreenElement) {{
      document.documentElement.requestFullscreen().catch(() => {{}});
    }} else {{
      document.exitFullscreen().catch(() => {{}});
    }}
  }};

  window.stopSlideshow = function() {{
    if (slideTimer) clearInterval(slideTimer);
    slideTimer = null;
    document.getElementById("slideshow-stage").classList.remove("active");
    if (document.fullscreenElement) {{
      document.exitFullscreen().catch(() => {{}});
    }}
  }};

  function wakeHud() {{
    const hud = document.getElementById("tv-hud");
    const badge = document.getElementById("tv-badge");
    const stage = document.getElementById("slideshow-stage");
    hud.classList.remove("hidden-hud");
    badge.classList.remove("hidden-hud");
    stage.classList.remove("hide-cursor");

    if (hudTimeout) clearTimeout(hudTimeout);
    hudTimeout = setTimeout(() => {{
      if (stage.classList.contains("active") && !isPaused) {{
        hud.classList.add("hidden-hud");
        badge.classList.add("hidden-hud");
        stage.classList.add("hide-cursor");
      }}
    }}, 3500);
  }}

  window.handleStageClick = function() {{
    wakeHud();
  }};

  document.addEventListener("mousemove", () => {{
    if (document.getElementById("slideshow-stage").classList.contains("active")) {{
      wakeHud();
    }}
  }});

  document.addEventListener("keydown", function(e) {{
    const stage = document.getElementById("slideshow-stage");
    if (!stage.classList.contains("active")) return;
    wakeHud();
    if (e.key === "Escape") window.stopSlideshow();
    else if (e.key === "ArrowRight") window.nextSlide();
    else if (e.key === "ArrowLeft") window.prevSlide();
    else if (e.key === " ") {{
      e.preventDefault();
      window.togglePause();
    }}
  }});

  document.addEventListener("DOMContentLoaded", init);
}})();
</script>
</body>
</html>
"""
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {OUT_HTML} ({os.path.getsize(OUT_HTML) / 1024:.1f} KB)")


if __name__ == "__main__":
    build_slideshow_player()
