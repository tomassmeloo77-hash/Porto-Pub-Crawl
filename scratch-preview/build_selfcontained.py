#!/usr/bin/env python3
import base64, pathlib, re
root = pathlib.Path("/home/user/Porto-Pub-Crawl")
adir = root/"assets"; sp = root/"scratch-preview"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def mime(name):
    if name.endswith(".webp"): return "image/webp"
    if name.endswith(".jpg") or name.endswith(".jpeg"): return "image/jpeg"
    if name.endswith(".png"): return "image/png"
    if name.endswith(".mp4"): return "video/mp4"
    return "application/octet-stream"

html = (root/"index-b.html").read_text()
# strip responsive-image attributes so only the base src needs inlining
html = re.sub(r'\s(srcset|sizes|imagesrcset|imagesizes)="[^"]*"', '', html)

# which local files to inline (displayed assets); videos use the lighter preview encodes
FILEMAP = {
  "hero-video-desktop.mp4": sp/"evo-desktop.mp4",
  "hero-video-mobile.mp4":  sp/"evo-mobile.mp4",
}
# every assets/<name> token actually referenced
tokens = sorted(set(re.findall(r'assets/([A-Za-z0-9_\-.]+\.(?:webp|jpg|jpeg|png|mp4))', html)), key=len, reverse=True)
SKIP = {"hero-share.jpg","logo-email.png"}  # meta-only / unused
inlined=0; skipped=[]
for name in tokens:
    if name in SKIP: continue
    srcfile = FILEMAP.get(name, adir/name)
    if not pathlib.Path(srcfile).exists():
        skipped.append(name); continue
    # skip the heavy gallery clips to keep the file light (they'll just not lazy-load)
    if name in ("video-reel.mp4","video-clubfloor.mp4"): skipped.append(name); continue
    uri = "data:%s;base64,%s" % (mime(name), b64(srcfile))
    html = html.replace("assets/"+name, uri)
    inlined+=1

out = sp/"page-b-selfcontained.html"
out.write_text(html)
print("inlined",inlined,"skipped",skipped,"size", round(len(html)/1024/1024,2),"MB")
