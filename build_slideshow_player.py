import os
import io
import json
import base64
from PIL import Image

HERON_SRC = r"c:\Users\j-a-b\.gemini\antigravity\scratch\food_tracker\extracted_kitchen\heron_luminous.png"
SITE_ROOT = r"c:\Users\j-a-b\.gemini\antigravity\scratch\google_site"
MANIFEST_JS = os.path.join(SITE_ROOT, "assets", "img", "HaddadArchive", "manifest.js")
OUT_HTML = os.path.join(SITE_ROOT, "Norgem_Family_Slideshow_Player.html")


def get_heron_data_uri():
    with Image.open(HERON_SRC) as im:
        im.thumbnail((280, 280), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="PNG", optimize=True)
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        return f"data:image/png;base64,{b64}"


def load_compact_catalog():
    """
    Extracts a compact [decade, filename, caption] catalog of all 1,774 archive photos from manifest.js.
    This enables Norgem_Family_Slideshow_Player.html to auto-discover and merge ALL local decade subfolders
    (in the current folder, flat folder, or parent folder) across multiple downloads without any user action.
    """
    if not os.path.exists(MANIFEST_JS):
        return "[]"
    with open(MANIFEST_JS, "r", encoding="utf-8") as f:
        raw = f.read()
    idx = raw.find("{")
    r_idx = raw.rfind("}")
    if idx < 0 or r_idx < 0:
        return "[]"
    data = json.loads(raw[idx:r_idx + 1])
    compact = []
    for p in data.get("photos", []):
        compact.append([p.get("decade", ""), p.get("name", ""), p.get("caption", "") or ""])
    return json.dumps(compact, ensure_ascii=False, separators=(",", ":"))


def build_slideshow_player():
    heron_uri = get_heron_data_uri()
    compact_catalog_json = load_compact_catalog()

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
    padding: 20px 18px;
    background:
      radial-gradient(circle at 50% 22%, rgba(14, 116, 144, 0.22) 0%, rgba(15, 23, 42, 0.55) 42%, #020617 80%);
  }}

  .launcher-card {{
    width: 100%;
    max-width: 900px;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(56, 189, 248, 0.28);
    border-radius: 24px;
    padding: 26px 30px;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.75), 0 0 40px rgba(56, 189, 248, 0.08);
    margin: auto 0;
  }}

  .brand-header {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    margin-bottom: 18px;
  }}

  .heron-logo {{
    width: 108px;
    height: 108px;
    object-fit: contain;
    margin-bottom: 8px;
  }}

  .brand-title {{
    font-size: 1.55rem;
    font-weight: 800;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #ffffff;
  }}

  .brand-subtitle {{
    font-size: 0.9rem;
    color: #38bdf8;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 600;
    margin-top: 3px;
  }}

  .step-box {{
    background: rgba(2, 6, 23, 0.65);
    border: 1px solid rgba(148, 163, 184, 0.22);
    border-radius: 16px;
    padding: 16px 20px;
    margin-bottom: 14px;
  }}

  .step-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
  }}

  .step-title {{
    font-size: 0.98rem;
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

  .folder-btn-subtle {{
    background: rgba(30, 41, 59, 0.85);
    color: #cbd5e1;
    border: 1px solid rgba(148, 163, 184, 0.35);
    padding: 7px 14px;
    border-radius: 10px;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }}

  .folder-btn-subtle:hover {{
    background: rgba(51, 65, 85, 0.95);
    color: #ffffff;
    border-color: #38bdf8;
  }}

  .status-pill {{
    font-size: 0.85rem;
    font-weight: 700;
    padding: 6px 14px;
    border-radius: 999px;
    background: rgba(16, 185, 129, 0.16);
    color: #34d399;
    border: 1px solid rgba(16, 185, 129, 0.4);
  }}

  /* Auto-Start Toggle Switch Bar */
  .autostart-bar {{
    background: linear-gradient(135deg, rgba(14, 116, 144, 0.22) 0%, rgba(15, 23, 42, 0.8) 100%);
    border: 1px solid rgba(56, 189, 248, 0.35);
    border-radius: 16px;
    padding: 14px 20px;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 14px;
  }}

  .autostart-info {{
    display: flex;
    flex-direction: column;
    gap: 3px;
  }}

  .autostart-title {{
    font-size: 0.96rem;
    font-weight: 800;
    color: #f8fafc;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .autostart-desc {{
    font-size: 0.8rem;
    color: #94a3b8;
  }}

  .toggle-switch-wrap {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
  }}

  .toggle-label-state {{
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 0.05em;
    min-width: 34px;
    text-align: right;
  }}

  .toggle-switch {{
    position: relative;
    width: 54px;
    height: 28px;
    background: #334155;
    border-radius: 999px;
    border: 1px solid rgba(148, 163, 184, 0.4);
    transition: all 0.25s ease;
  }}

  .toggle-switch::after {{
    content: "";
    position: absolute;
    top: 2px;
    left: 3px;
    width: 22px;
    height: 22px;
    background: #f8fafc;
    border-radius: 50%;
    transition: all 0.25s ease;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
  }}

  .toggle-switch.on {{
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    border-color: #6ee7b7;
    box-shadow: 0 0 14px rgba(16, 185, 129, 0.45);
  }}

  .toggle-switch.on::after {{
    transform: translateX(25px);
  }}

  /* Mode & Decade Selector Buttons */
  .mode-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 12px;
    margin-bottom: 14px;
  }}

  .random-btn {{
    flex: 1;
    min-width: 210px;
    padding: 12px 18px;
    border-radius: 14px;
    font-size: 0.96rem;
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
    opacity: 0.28;
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
    margin-top: 14px;
    padding-top: 14px;
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
    padding: 13px 36px;
    border-radius: 16px;
    font-size: 1.15rem;
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
    font-size: 0.79rem;
    color: #94a3b8;
    margin-top: 12px;
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
    background: rgba(2, 6, 23, 0.72);
    backdrop-filter: blur(10px);
    padding: 8px 16px;
    border-radius: 999px;
    border: 1px solid rgba(56, 189, 248, 0.35);
    z-index: 110;
    transition: opacity 0.4s ease;
  }}

  /* Optional Photo Caption Pill Above HUD */
  .tv-caption {{
    position: absolute;
    bottom: 86px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(2, 6, 23, 0.85);
    color: #fde68a;
    border: 1px solid rgba(245, 158, 11, 0.45);
    padding: 8px 20px;
    border-radius: 14px;
    font-size: 0.98rem;
    font-weight: 700;
    max-width: 82vw;
    text-align: center;
    z-index: 110;
    display: none;
  }}

  /* Auto-hiding bottom HUD bar */
  .tv-hud {{
    position: absolute;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    background: rgba(15, 23, 42, 0.88);
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
<!-- INJECTED_ZIP_MANIFEST_PLACEHOLDER -->
<script src="assets/img/HaddadArchive/manifest.js?v=mat1" onerror=""></script>
</head>
<body>

<div id="launcher-screen">
  <div class="launcher-card">
    <!-- Norgem Enterprises & Blue Heron Header -->
    <div class="brand-header">
      <img src="{heron_uri}" alt="Norgem Enterprises Blue Heron" class="heron-logo">
      <div class="brand-title">Norgem Enterprises</div>
      <div class="brand-subtitle">Haddad Family Decade Slideshow &amp; Smart TV Viewer</div>
    </div>

    <!-- Auto-Detected Decades & Photo Status Bar (Zero Clicks Required + Automatic Multi-Download Merge) -->
    <div class="step-box">
      <div class="step-header">
        <div class="step-title">
          <span class="step-badge">✓</span>
          <span id="source-title-text">Automatic Decade &amp; Multi-Download Folder Detection</span>
        </div>
        <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
          <span id="source-status-pill" class="status-pill">Scanning decade folders...</span>
          <input type="file" id="folder-input" webkitdirectory directory multiple style="display:none" onchange="handleFolderSelect(event)">
          <button class="folder-btn-subtle" onclick="document.getElementById('folder-input').click()" title="Optional: Load a different folder from your computer">
            <span>📂 Change Folder</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Auto-Start Toggle Switch (Runs Last Selected Configuration Automatically When Turned ON) -->
    <div class="autostart-bar">
      <div class="autostart-info">
        <div class="autostart-title">
          <span>⚡ Auto-Start Slideshow on Launch</span>
        </div>
        <div class="autostart-desc">
          When turned <strong>ON</strong>, opening this Slideshow HTML automatically runs your last selected decade &amp; speed configuration without clicking anything.
        </div>
      </div>
      <div class="toggle-switch-wrap" onclick="toggleAutoStart()">
        <span id="autostart-state-label" class="toggle-label-state" style="color:#94a3b8;">OFF</span>
        <div id="autostart-switch" class="toggle-switch" role="switch" aria-checked="false"></div>
      </div>
    </div>

    <!-- Pick Random OR Highlight Any Number of Decades -->
    <div class="step-box">
      <div class="step-header">
        <div class="step-title">
          <span class="step-badge">★</span>
          <span>Pick <strong>Random Shuffle</strong> OR Select One or More <strong>Decades</strong> (Stay Highlighted)</span>
        </div>
        <span id="selection-summary" style="font-size:0.84rem; color:#38bdf8; font-weight:700;"></span>
      </div>

      <!-- Random All Button vs. Highlight All Decades -->
      <div class="mode-row">
        <button id="btn-random-all" class="random-btn active" onclick="activateRandomAllMode()">
          <span>🎲 RANDOM (All Decades Shuffle)</span>
        </button>
        <button id="btn-select-all-decades" class="random-btn" style="flex:0.65;" onclick="highlightAllDecades()">
          <span>☑️ Highlight All Decades</span>
        </button>
      </div>

      <!-- Decade Buttons (Stay Highlighted When Clicked) -->
      <div id="decade-buttons-grid" class="decade-grid">
        <!-- Populated dynamically -->
      </div>
    </div>

    <!-- Interval & GO Button -->
    <div class="launch-row">
      <div class="settings-group">
        <label>
          Slide Speed:
          <select id="slide-interval" class="settings-select" onchange="onSettingsChanged()">
            <option value="4000">4 Seconds</option>
            <option value="6000" selected>6 Seconds (Recommended)</option>
            <option value="10000">10 Seconds</option>
            <option value="15000">15 Seconds</option>
          </select>
        </label>
        <label style="display:inline-flex; align-items:center; gap:6px; cursor:pointer;">
          <input type="checkbox" id="chk-shuffle-selected" checked style="width:16px; height:16px;" onchange="onSettingsChanged()">
          <span>Shuffle Order</span>
        </label>
      </div>

      <button id="btn-go" class="go-btn" onclick="startSlideshow()">
        <span>▶ GO (Start Slideshow)</span>
      </button>
    </div>

    <div class="cast-tip">
      💡 <strong>Smart TV Casting Tip:</strong> In Google Chrome, click the <strong>&#8942;</strong> menu (top-right) &rarr; <strong>Save and share</strong> &rarr; <strong>Cast...</strong> to beam this full-screen slideshow directly to your Smart TV.
    </div>
  </div>

  <div style="font-size:0.78rem; color:#64748b; text-align:center; padding-top:10px;">
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

  <!-- Optional Family Caption Banner -->
  <div id="tv-caption" class="tv-caption"></div>

  <!-- Bottom Floating Remote Control HUD -->
  <div id="tv-hud" class="tv-hud" onclick="event.stopPropagation()">
    <button class="hud-btn" onclick="stopSlideshow()">&larr; Change Decades / Settings</button>
    <button class="hud-btn" onclick="prevSlide()">&#10094; Prev</button>
    <button id="btn-pause-resume" class="hud-btn" onclick="togglePause()">⏸ Pause</button>
    <button class="hud-btn" onclick="nextSlide()">Next &#10095;</button>
    <button id="btn-hud-autostart" class="hud-btn" onclick="toggleAutoStart()">⚡ Auto-Start: OFF</button>
    <button class="hud-btn" onclick="toggleFullscreen()">⛶ Full Screen</button>
  </div>
</div>

<script>
(function() {{
  const KNOWN_DECADES = [
    "Pre-1940s", "1940s", "1950s", "1960s", "1970s",
    "1980s", "1990s", "2000s", "2010s", "2020s", "Highlights"
  ];
  const PREFS_STORAGE_KEY = "norgem_family_slideshow_prefs_v2";
  const COMPACT_ARCHIVE_CATALOG = {compact_catalog_json};

  let allPhotos = []; // Each item: {{ decade, name, url, caption }}
  let decadeCounts = {{}};
  let randomAllMode = true;
  let highlightedDecades = new Set();
  let previouslySeenDecades = new Set();
  let newlyAddedDecadesCount = 0;
  let autoStartEnabled = false;

  // Slideshow state
  let playlist = [];
  let currentIndex = 0;
  let slideTimer = null;
  let isPaused = false;
  let activeImgSlot = "a";
  let hudTimeout = null;

  function loadSavedPreferences() {{
    try {{
      const raw = localStorage.getItem(PREFS_STORAGE_KEY);
      if (!raw) return;
      const prefs = JSON.parse(raw);
      if (typeof prefs.autoStart === "boolean") {{
        autoStartEnabled = prefs.autoStart;
      }}
      if (typeof prefs.randomAllMode === "boolean") {{
        randomAllMode = prefs.randomAllMode;
      }}
      if (Array.isArray(prefs.highlightedDecades)) {{
        highlightedDecades = new Set(prefs.highlightedDecades);
      }}
      if (Array.isArray(prefs.seenDecades)) {{
        previouslySeenDecades = new Set(prefs.seenDecades);
      }}
      if (prefs.slideInterval) {{
        const sel = document.getElementById("slide-interval");
        if (sel) sel.value = String(prefs.slideInterval);
      }}
      if (typeof prefs.shuffleSelected === "boolean") {{
        const chk = document.getElementById("chk-shuffle-selected");
        if (chk) chk.checked = prefs.shuffleSelected;
      }}
    }} catch (e) {{}}
    updateAutoStartUI();
  }}

  function savePreferences() {{
    try {{
      const currentAvailable = Object.keys(decadeCounts).filter(d => (decadeCounts[d] || 0) > 0);
      const prefs = {{
        autoStart: autoStartEnabled,
        randomAllMode: randomAllMode,
        highlightedDecades: Array.from(highlightedDecades),
        seenDecades: currentAvailable.length > 0 ? currentAvailable : Array.from(previouslySeenDecades),
        slideInterval: document.getElementById("slide-interval").value,
        shuffleSelected: document.getElementById("chk-shuffle-selected").checked
      }};
      localStorage.setItem(PREFS_STORAGE_KEY, JSON.stringify(prefs));
    }} catch (e) {{}}
  }}

  function updateAutoStartUI() {{
    const sw = document.getElementById("autostart-switch");
    const lbl = document.getElementById("autostart-state-label");
    const hudBtn = document.getElementById("btn-hud-autostart");
    if (sw) {{
      if (autoStartEnabled) {{
        sw.classList.add("on");
        sw.setAttribute("aria-checked", "true");
      }} else {{
        sw.classList.remove("on");
        sw.setAttribute("aria-checked", "false");
      }}
    }}
    if (lbl) {{
      lbl.textContent = autoStartEnabled ? "ON" : "OFF";
      lbl.style.color = autoStartEnabled ? "#34d399" : "#94a3b8";
    }}
    if (hudBtn) {{
      hudBtn.textContent = "⚡ Auto-Start: " + (autoStartEnabled ? "ON" : "OFF");
      hudBtn.style.borderColor = autoStartEnabled ? "#34d399" : "rgba(148, 163, 184, 0.3)";
    }}
  }}

  window.toggleAutoStart = function() {{
    autoStartEnabled = !autoStartEnabled;
    updateAutoStartUI();
    savePreferences();
  }};

  window.onSettingsChanged = function() {{
    savePreferences();
    if (document.getElementById("slideshow-stage").classList.contains("active")) {{
      scheduleNextSlide();
    }}
  }};

  function reconcilePreferencesWithLoadedDecades() {{
    const availableDecades = Object.keys(decadeCounts).filter(d => (decadeCounts[d] || 0) > 0);
    newlyAddedDecadesCount = 0;

    // Detect if the user downloaded & extracted additional decades since their last session
    const brandNewDecades = [];
    if (previouslySeenDecades.size > 0) {{
      availableDecades.forEach(d => {{
        if (!previouslySeenDecades.has(d)) {{
          brandNewDecades.push(d);
        }}
      }});
    }}
    newlyAddedDecadesCount = brandNewDecades.length;

    if (!randomAllMode) {{
      // Keep highlighted decades that exist on disk, AND automatically highlight any newly added decades!
      const validHighlighted = Array.from(highlightedDecades).filter(d => (decadeCounts[d] || 0) > 0);
      brandNewDecades.forEach(d => {{
        if (!validHighlighted.includes(d)) validHighlighted.push(d);
      }});
      if (validHighlighted.length > 0) {{
        highlightedDecades = new Set(validHighlighted);
      }} else {{
        highlightedDecades = new Set(availableDecades);
        randomAllMode = true;
      }}
    }}

    previouslySeenDecades = new Set(availableDecades);
    savePreferences();
  }}

  function probeImageExists(relUrl, timeoutMs) {{
    return new Promise(resolve => {{
      const img = new Image();
      let done = false;
      const timer = setTimeout(() => {{
        if (!done) {{
          done = true;
          resolve(false);
        }}
      }}, timeoutMs || 1100);
      img.onload = () => {{
        if (!done) {{
          done = true;
          clearTimeout(timer);
          resolve(true);
        }}
      }};
      img.onerror = () => {{
        if (!done) {{
          done = true;
          clearTimeout(timer);
          resolve(false);
        }}
      }};
      img.src = relUrl;
    }});
  }}

  async function autoProbeLocalExtractedFolders() {{
    // Group compact catalog by decade: [decade, name, caption]
    const byDecade = {{}};
    for (let i = 0; i < COMPACT_ARCHIVE_CATALOG.length; i++) {{
      const row = COMPACT_ARCHIVE_CATALOG[i];
      const dec = row[0];
      if (!byDecade[dec]) byDecade[dec] = [];
      byDecade[dec].push({{ decade: dec, name: row[1], caption: row[2] || "" }});
    }}

    // Step 1: Test candidate relative prefixes for every decade in parallel:
    //   1) ./{{dec}}/{{name}}  (standard decade subfolder alongside this HTML file)
    //   2) ./{{name}}          (flattened folder alongside this HTML file)
    //   3) ../{{dec}}/{{name}} (parent folder decade subfolder, in case user extracted a 2nd .ZIP into a child subfolder!)
    const decadesList = Object.keys(byDecade);
    const activeLocalDecades = [];

    await Promise.all(decadesList.map(async dec => {{
      const list = byDecade[dec] || [];
      // Pick 6 evenly spaced sample photos across the decade so partial-decade downloads are detected too!
      const sampleIndices = [0, Math.floor(list.length * 0.2), Math.floor(list.length * 0.4), Math.floor(list.length * 0.6), Math.floor(list.length * 0.8), list.length - 1];
      const uniqueSamples = Array.from(new Set(sampleIndices.filter(idx => idx >= 0 && idx < list.length))).map(idx => list[idx]);

      const prefixes = [`${{dec}}/`, "", `../${{dec}}/`];
      for (const pfx of prefixes) {{
        for (const c of uniqueSamples) {{
          if (await probeImageExists(`${{pfx}}${{c.name}}`, 750)) {{
            activeLocalDecades.push({{ dec, prefix: pfx }});
            return;
          }}
        }}
      }}
    }}));

    if (activeLocalDecades.length === 0) return [];

    // Step 2: For every detected decade folder, probe all photos in fast parallel batches of 64
    //         (This discovers ALL photos in each decade, including newly added photos merged into an existing decade!)
    const discovered = [];
    for (const info of activeLocalDecades) {{
      const list = byDecade[info.dec] || [];
      const batchSize = 64;
      for (let i = 0; i < list.length; i += batchSize) {{
        const chunk = list.slice(i, i + batchSize);
        const results = await Promise.all(chunk.map(async item => {{
          const url = `${{info.prefix}}${{item.name}}`;
          const ok = await probeImageExists(url, 950);
          return ok ? {{ decade: item.decade, name: item.name, url: url, caption: item.caption }} : null;
        }}));
        for (const r of results) {{
          if (r) discovered.push(r);
        }}
      }}
    }}
    return discovered;
  }}

  function finalizeLoadedPhotos(sourceDescription) {{
    recalcDecadeCounts();
    reconcilePreferencesWithLoadedDecades();
    const activeDecList = KNOWN_DECADES.filter(d => (decadeCounts[d] || 0) > 0);
    const pill = document.getElementById("source-status-pill");
    if (allPhotos.length > 0) {{
      const addedSuffix = newlyAddedDecadesCount > 0
        ? ` • +${{newlyAddedDecadesCount}} New Decade${{newlyAddedDecadesCount === 1 ? '' : 's'}} Merged`
        : "";
      pill.textContent = `✓ Ready: ${{allPhotos.length.toLocaleString()}} Photos Across ${{activeDecList.length}} Decade${{activeDecList.length === 1 ? '' : 's'}} (${{activeDecList.join(', ')}}${{addedSuffix}})`;
    }} else {{
      pill.textContent = sourceDescription || "Click 'Change Folder' to select your unzipped photo folder";
    }}
    renderDecadeButtons();
    updateSelectionSummary();

    // If Auto-Start Toggle is ON and photos are loaded, automatically launch the last selected slideshow configuration!
    if (autoStartEnabled && allPhotos.length > 0) {{
      setTimeout(() => {{
        window.startSlideshow();
      }}, 250);
    }}
  }}

  async function init() {{
    loadSavedPreferences();

    // If opened online on the website (http/https) where window.HADDAD_ARCHIVE_MANIFEST is loaded:
    if (window.location.protocol !== "file:" && window.HADDAD_ARCHIVE_MANIFEST && Array.isArray(window.HADDAD_ARCHIVE_MANIFEST.photos) && window.HADDAD_ARCHIVE_MANIFEST.photos.length > 0) {{
      allPhotos = window.HADDAD_ARCHIVE_MANIFEST.photos.map(p => ({{
        decade: p.decade,
        name: p.name,
        url: p.full + "?v=mat1",
        caption: p.caption || ""
      }}));
      finalizeLoadedPhotos();
      return;
    }}

    // Local Extracted Folder Engine (file:///):
    // PROTECTION AGAINST MULTI-DOWNLOAD OVERWRITES OR PARTIAL EXTRACTIONS:
    // Whether the user overwrote Norgem_Family_Slideshow_Player.html during a 2nd download, skipped overwriting it,
    // or added new decades / new photos to existing decade folders, we ALWAYS combine:
    //   1) The embedded NORGEM_EXTRACTED_ZIP_MANIFEST (instant 0ms load for the current ZIP), AND
    //   2) A live disk scan across all 11 decade folders (autoProbeLocalExtractedFolders)
    // into a deduplicated union so old and new decades/photos merge seamlessly with zero errors!
    const mergedMap = new Map();

    if (Array.isArray(window.NORGEM_EXTRACTED_ZIP_MANIFEST) && window.NORGEM_EXTRACTED_ZIP_MANIFEST.length > 0) {{
      window.NORGEM_EXTRACTED_ZIP_MANIFEST.forEach(p => {{
        const key = `${{p.decade}}/${{p.name}}`;
        mergedMap.set(key, {{
          decade: p.decade,
          name: p.name,
          url: p.url || `${{p.decade}}/${{p.name}}`,
          caption: p.caption || ""
        }});
      }});
      // Render immediately in 0ms from the embedded manifest while the background disk scan checks for any additional merged decades/photos!
      allPhotos = Array.from(mergedMap.values());
      finalizeLoadedPhotos();
    }}

    // Now scan the disk folder (and parent folder) for any pre-existing or newly added decades/photos and merge them in!
    const diskPhotos = await autoProbeLocalExtractedFolders();
    if (diskPhotos.length > 0) {{
      let addedFromDisk = 0;
      diskPhotos.forEach(p => {{
        const key = `${{p.decade}}/${{p.name}}`;
        if (!mergedMap.has(key)) {{
          mergedMap.set(key, p);
          addedFromDisk++;
        }}
      }});
      if (addedFromDisk > 0 || allPhotos.length === 0) {{
        // Sort merged photos chronologically by KNOWN_DECADES order and filename
        const decOrder = {{}};
        KNOWN_DECADES.forEach((d, idx) => decOrder[d] = idx);
        allPhotos = Array.from(mergedMap.values()).sort((a, b) => {{
          const da = decOrder[a.decade] !== undefined ? decOrder[a.decade] : 99;
          const db = decOrder[b.decade] !== undefined ? decOrder[b.decade] : 99;
          if (da !== db) return da - db;
          return a.name.localeCompare(b.name);
        }});
        finalizeLoadedPhotos();
      }}
      return;
    }}

    if (allPhotos.length === 0) {{
      finalizeLoadedPhotos("No local decade folders detected alongside this HTML file");
    }}
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

    const captionLookup = {{}};
    for (let i = 0; i < COMPACT_ARCHIVE_CATALOG.length; i++) {{
      const row = COMPACT_ARCHIVE_CATALOG[i];
      if (row[2]) captionLookup[row[1]] = row[2];
    }}

    // Merge newly selected folder files with any already loaded photos (deduplicated by decade/filename)
    const mergedMap = new Map();
    allPhotos.forEach(p => {{
      mergedMap.set(`${{p.decade}}/${{p.name}}`, p);
    }});

    imageFiles.forEach(f => {{
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
        const m = f.name.match(/(Pre-1940s|1940s|1950s|1960s|1970s|1980s|1990s|2000s|2010s|2020s)/i);
        if (m) detectedDecade = m[1];
      }}
      const key = `${{detectedDecade}}/${{f.name}}`;
      if (!mergedMap.has(key)) {{
        mergedMap.set(key, {{
          decade: detectedDecade,
          name: f.name,
          url: URL.createObjectURL(f),
          caption: captionLookup[f.name] || "",
          isBlob: true
        }});
      }}
    }});

    allPhotos = Array.from(mergedMap.values());
    finalizeLoadedPhotos();
  }};

  window.activateRandomAllMode = function() {{
    randomAllMode = true;
    highlightedDecades.clear();
    document.getElementById("chk-shuffle-selected").checked = true;
    savePreferences();
    renderDecadeButtons();
    updateSelectionSummary();
  }};

  window.highlightAllDecades = function() {{
    randomAllMode = false;
    highlightedDecades.clear();
    Object.keys(decadeCounts).forEach(d => {{
      if (decadeCounts[d] > 0) highlightedDecades.add(d);
    }});
    savePreferences();
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
    savePreferences();
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
      el.textContent = "Waiting for photo folder...";
      goBtn.disabled = true;
      return;
    }}
    goBtn.disabled = false;
    if (randomAllMode) {{
      el.textContent = `Mode: Random Shuffle Across All ${{allPhotos.length.toLocaleString()}} Loaded Photos`;
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
      alert("No photos are loaded yet.");
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
      playlist = shuffleArray(allPhotos);
    }}

    savePreferences();
    currentIndex = 0;
    isPaused = false;
    document.getElementById("btn-pause-resume").textContent = "⏸ Pause";

    const stage = document.getElementById("slideshow-stage");
    stage.classList.add("active");

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

    const capEl = document.getElementById("tv-caption");
    if (capEl) {{
      if (item.caption && item.caption.trim()) {{
        capEl.textContent = "🏷️ " + item.caption.trim();
        capEl.style.display = "block";
      }} else {{
        capEl.textContent = "";
        capEl.style.display = "none";
      }}
    }}
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
