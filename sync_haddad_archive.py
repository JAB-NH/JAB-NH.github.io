import os
import sys
import json
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
import cv2
import numpy as np
from PIL import Image, ImageOps

SOURCE_ROOT = r"G:\My Drive\Agent_Bridge\Family_Photo_Project\Unsorted_Photos"
RESTORED_VAULT_ROOT = r"G:\My Drive\Agent_Bridge\Family_Photo_Project\Restored_Vault"
SITE_ROOT = r"c:\Users\j-a-b\.gemini\antigravity\scratch\google_site"
OUT_ROOT = os.path.join(SITE_ROOT, "assets", "img", "HaddadArchive")
MANIFEST_JS = os.path.join(OUT_ROOT, "manifest.js")
MANIFEST_JSON = os.path.join(OUT_ROOT, "manifest.json")

DECADES = [
    "Pre-1940s",
    "1940s",
    "1950s",
    "1960s",
    "1970s",
    "1980s",
    "1990s",
    "2000s",
    "2010s",
    "2020s",
]

FULL_MAX_DIM = 2200
FULL_QUALITY = 85
THUMB_MAX_DIM = 420
THUMB_QUALITY = 78


def apply_gallery_mat_rgb(img_rgb: np.ndarray) -> np.ndarray:
    """
    PHO Border Geometry Engine (gallery_mat):
    - Preserves Museum Exhibition Mat & Plaque (#FAF7F0) if already applied.
    - Otherwise trims perimeter white scanner slivers (up to 8% per edge where mean or p20 > 220)
      and applies a symmetrical 2.5% (min 20px) pure white (#FFFFFF) museum mat on all 4 sides.
    """
    h, w = img_rgb.shape[:2]
    if h < 40 or w < 40:
        return img_rgb

    # Check if warm-cream Museum Caption Plaque (#FAF7F0 -> RGB [250, 247, 240]) is already applied on all 4 corners
    corners_strip = [
        img_rgb[0:5, 0:5],
        img_rgb[0:5, w - 5 : w],
        img_rgb[h - 5 : h, 0:5],
        img_rgb[h - 5 : h, w - 5 : w],
    ]
    if all(np.all(np.abs(c.astype(int) - np.array([250, 247, 240])) <= 3) for c in corners_strip):
        return img_rgb

    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    max_h = int(h * 0.08)
    max_w = int(w * 0.08)
    thresh = 220

    top = 0
    for r in range(max_h):
        if np.mean(gray[r, :]) > thresh or np.percentile(gray[r, :], 20) > thresh:
            top = r + 1
        else:
            break

    bottom = 0
    for r in range(max_h):
        if np.mean(gray[h - 1 - r, :]) > thresh or np.percentile(gray[h - 1 - r, :], 20) > thresh:
            bottom = r + 1
        else:
            break

    left = 0
    for c in range(max_w):
        if np.mean(gray[:, c]) > thresh or np.percentile(gray[:, c], 20) > thresh:
            left = c + 1
        else:
            break

    right = 0
    for c in range(max_w):
        if np.mean(gray[:, w - 1 - c]) > thresh or np.percentile(gray[:, w - 1 - c], 20) > thresh:
            right = c + 1
        else:
            break

    y1, y2 = top, max(top + 100, h - bottom)
    x1, x2 = left, max(left + 100, w - right)
    trimmed = img_rgb[y1:y2, x1:x2]

    mat_px = max(20, int(min(trimmed.shape[:2]) * 0.025))
    return cv2.copyMakeBorder(
        trimmed,
        mat_px,
        mat_px,
        mat_px,
        mat_px,
        cv2.BORDER_CONSTANT,
        value=[255, 255, 255],
    )


def has_pure_white_mat(path: str) -> bool:
    """Checks whether an existing image file already has the pure white #FFFFFF (or #FAF7F0) mat."""
    if not os.path.isfile(path):
        return False
    try:
        with Image.open(path) as im:
            im_rgb = im.convert("RGB")
            w, h = im_rgb.size
            arr = np.asarray(im_rgb)
            # Check top-left, top-right, bottom-left, bottom-right 4x4 corners
            corners = [
                arr[0:4, 0:4],
                arr[0:4, w - 4 : w],
                arr[h - 4 : h, 0:4],
                arr[h - 4 : h, w - 4 : w],
            ]
            for c in corners:
                is_white = np.mean(c) >= 252.0
                is_cream = np.all(np.abs(c.astype(int) - np.array([250, 247, 240])) <= 6)
                if not (is_white or is_cream):
                    return False
            return True
    except Exception:
        return False


def process_one_photo(task):
    src_path, decade, filename, sync_vault, force = task
    stem, _ = os.path.splitext(filename)
    out_filename = f"{stem}.jpg"

    full_dir = os.path.join(OUT_ROOT, "full", decade)
    thumb_dir = os.path.join(OUT_ROOT, "thumbs", decade)
    full_path = os.path.join(full_dir, out_filename)
    thumb_path = os.path.join(thumb_dir, out_filename)

    vault_path = None
    if sync_vault and os.path.isdir(RESTORED_VAULT_ROOT):
        vault_dec_dir = os.path.join(RESTORED_VAULT_ROOT, decade)
        os.makedirs(vault_dec_dir, exist_ok=True)
        vault_path = os.path.join(vault_dec_dir, filename)

    src_mtime = os.path.getmtime(src_path)
    need_build = force
    if not need_build:
        if not (os.path.exists(full_path) and os.path.exists(thumb_path)):
            need_build = True
        elif os.path.getmtime(full_path) < src_mtime or os.path.getmtime(thumb_path) < src_mtime:
            need_build = True
        elif not has_pure_white_mat(full_path):
            need_build = True
        elif vault_path and (not os.path.exists(vault_path) or not has_pure_white_mat(vault_path)):
            need_build = True

    if need_build:
        with Image.open(src_path) as im:
            im = ImageOps.exif_transpose(im)
            if im.mode != "RGB":
                im = im.convert("RGB")
            arr_rgb = np.asarray(im)

        matted_rgb = apply_gallery_mat_rgb(arr_rgb)
        im_matted = Image.fromarray(matted_rgb)
        orig_w, orig_h = im_matted.size

        # Sync full-resolution Gallery Mat derivative to Restored_Vault if applicable
        if vault_path:
            try:
                im_matted.save(vault_path, format="JPEG", quality=95, subsampling=0)
            except Exception as e:
                print(f"[WARN] Could not write vault photo {vault_path}: {e}")

        # Full / Web Download version (with Gallery Mat baked in)
        if max(orig_w, orig_h) > FULL_MAX_DIM:
            im_full = im_matted.copy()
            im_full.thumbnail((FULL_MAX_DIM, FULL_MAX_DIM), Image.Resampling.LANCZOS)
            im_full.save(full_path, format="JPEG", quality=FULL_QUALITY, optimize=True, progressive=True)
            full_w, full_h = im_full.size
        else:
            im_matted.save(full_path, format="JPEG", quality=FULL_QUALITY, optimize=True, progressive=True)
            full_w, full_h = orig_w, orig_h

        # Thumbnail version (with Gallery Mat baked in)
        im_thumb = im_matted.copy()
        im_thumb.thumbnail((THUMB_MAX_DIM, THUMB_MAX_DIM), Image.Resampling.LANCZOS)
        im_thumb.save(thumb_path, format="JPEG", quality=THUMB_QUALITY, optimize=True, progressive=True)
    else:
        with Image.open(full_path) as im_full:
            full_w, full_h = im_full.size

    full_bytes = os.path.getsize(full_path)
    thumb_bytes = os.path.getsize(thumb_path)
    url_filename = urllib.parse.quote(out_filename)

    return {
        "id": f"{decade}/{out_filename}",
        "decade": decade,
        "name": out_filename,
        "thumb": f"assets/img/HaddadArchive/thumbs/{decade}/{url_filename}",
        "full": f"assets/img/HaddadArchive/full/{decade}/{url_filename}",
        "w": full_w,
        "h": full_h,
        "bytes": full_bytes,
        "thumb_bytes": thumb_bytes,
    }


def main():
    force = "--force" in sys.argv
    t0 = time.time()
    os.makedirs(OUT_ROOT, exist_ok=True)
    tasks = []

    for dec in DECADES:
        dec_src = os.path.join(SOURCE_ROOT, dec)
        os.makedirs(os.path.join(OUT_ROOT, "full", dec), exist_ok=True)
        os.makedirs(os.path.join(OUT_ROOT, "thumbs", dec), exist_ok=True)
        if not os.path.isdir(dec_src):
            continue
        files = sorted(
            f for f in os.listdir(dec_src)
            if os.path.isfile(os.path.join(dec_src, f)) and f.lower().endswith((".jpg", ".jpeg", ".png"))
        )
        # Clean up any stale files in output that were moved out of this decade
        valid_out_names = {f"{os.path.splitext(f)[0]}.jpg" for f in files}
        for sub in ("full", "thumbs"):
            sub_dir = os.path.join(OUT_ROOT, sub, dec)
            for existing in os.listdir(sub_dir):
                if existing not in valid_out_names:
                    try:
                        os.remove(os.path.join(sub_dir, existing))
                    except OSError:
                        pass

        for f in files:
            tasks.append((os.path.join(dec_src, f), dec, f, True, force))

    # Also include existing curated photos in assets/img/HaddadFamily as a "Highlights" collection
    legacy_dir = os.path.join(SITE_ROOT, "assets", "img", "HaddadFamily")
    legacy_out_dec = "Highlights"
    if os.path.isdir(legacy_dir):
        os.makedirs(os.path.join(OUT_ROOT, "full", legacy_out_dec), exist_ok=True)
        os.makedirs(os.path.join(OUT_ROOT, "thumbs", legacy_out_dec), exist_ok=True)
        for f in sorted(os.listdir(legacy_dir)):
            src_p = os.path.join(legacy_dir, f)
            if os.path.isfile(src_p) and f.lower().endswith((".jpg", ".jpeg", ".png")):
                tasks.append((src_p, legacy_out_dec, f, False, force))

    print(f"Syncing & Gallery-Matting {len(tasks)} photos across decades (force={force}) using ThreadPoolExecutor...")
    results = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = [pool.submit(process_one_photo, t) for t in tasks]
        for idx, fut in enumerate(as_completed(futures), 1):
            results.append(fut.result())
            if idx % 250 == 0 or idx == len(tasks):
                print(f"  Processed {idx}/{len(tasks)} photos...")

    all_decades = DECADES + ([legacy_out_dec] if any(r["decade"] == legacy_out_dec for r in results) else [])
    dec_rank = {d: i for i, d in enumerate(all_decades)}
    results.sort(key=lambda r: (dec_rank.get(r["decade"], 99), r["name"]))

    total_full_mb = sum(r["bytes"] for r in results) / (1024 * 1024)
    total_thumb_mb = sum(r["thumb_bytes"] for r in results) / (1024 * 1024)

    decade_summary = {}
    for d in all_decades:
        d_items = [r for r in results if r["decade"] == d]
        decade_summary[d] = {
            "count": len(d_items),
            "bytes": sum(r["bytes"] for r in d_items),
        }

    manifest_payload = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_photos": len(results),
        "total_bytes": sum(r["bytes"] for r in results),
        "decades": all_decades,
        "decade_summary": decade_summary,
        "photos": [
            {
                "id": r["id"],
                "decade": r["decade"],
                "name": r["name"],
                "thumb": r["thumb"],
                "full": r["full"],
                "w": r["w"],
                "h": r["h"],
                "bytes": r["bytes"],
            }
            for r in results
        ],
    }

    with open(MANIFEST_JSON, "w", encoding="utf-8") as f:
        json.dump(manifest_payload, f, separators=(",", ":"))

    with open(MANIFEST_JS, "w", encoding="utf-8") as f:
        f.write("window.HADDAD_ARCHIVE_MANIFEST = ")
        json.dump(manifest_payload, f, separators=(",", ":"))
        f.write(";\n")

    dt = time.time() - t0
    print(f"Done in {dt:.1f}s! Total photos: {len(results)} | Full: {total_full_mb:.2f} MB | Thumbs: {total_thumb_mb:.2f} MB")


if __name__ == "__main__":
    main()
