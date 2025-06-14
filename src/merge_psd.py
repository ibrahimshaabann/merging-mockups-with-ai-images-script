from psd_tools import PSDImage
from PIL import Image

# --------------------------
# 1️⃣ CONFIG
# --------------------------
PSD_PATH = 'tshirt_mockups/tshirt_mockup4.psd'
AI_IMAGE_PATH = 'ai_generated_images/ai_design1.png'
OUTPUT_PATH = 'outputs/final_mockup.png'

TARGET_LAYER_GROUP = 'Design and Color T-Shirt'
TARGET_SUBLAYER = 'Your Design Withiut Sleeve (double click)'   # <<-- replace with your sublayer name

# --------------------------
# 2️⃣ OPEN PSD & BASE IMAGE
# --------------------------
psd = PSDImage.open(PSD_PATH)
print(f"✅ PSD image bbox{psd._bbox}")
print(f"✅ PSD image layers: {psd._layers}")
base_image = psd.composite()
print(f"✅ Base image composite created from PSD: {base_image.size}")
print(f"✅ Base image mode: {base_image.mode}")
print(f"✅ Base image format: {base_image.format}") 
print(f"✅ Base image info{base_image.info}")
print(f"✅ PSD opened: {PSD_PATH}")

# --------------------------
# 3️⃣ FIND TARGET GROUP
# --------------------------
target_group = None
for layer in psd:
    if layer.name == TARGET_LAYER_GROUP:
        target_group = layer
        break

if target_group is None:
    raise Exception(f"Layer group '{TARGET_LAYER_GROUP}' not found!")

print(f"✅ Found layer group: {target_group.name}")

# --------------------------
# 4️⃣ LIST SUBLAYERS
# --------------------------
print(f"📂 Sublayers inside '{TARGET_LAYER_GROUP}':")
for sublayer in target_group:
    print(f"  - {sublayer.name} (Visible: {sublayer.visible})")

# --------------------------
# 5️⃣ FIND TARGET SUBLAYER
# --------------------------
target_sublayer = None
for sublayer in target_group:
    if sublayer.name == TARGET_SUBLAYER:
        target_sublayer = sublayer
        print(f"✅ target sublayer size: {target_sublayer.size}")
        break

if target_sublayer is None:
    raise Exception(f"Sublayer '{TARGET_SUBLAYER}' not found!")

print(f"✅ Found sublayer: {target_sublayer.name}")

# --------------------------
# 6️⃣ GET SUBLAYER POSITION & SIZE
# --------------------------
x1, y1, x2, y2 = target_sublayer.bbox
layer_width = x2 - x1
layer_height = y2 - y1

print(f"📐 Sublayer bbox: {target_sublayer.bbox}")
print(f"   Width: {layer_width}, Height: {layer_height}")

# --------------------------
# 7️⃣ OPEN & RESIZE AI IMAGE
# --------------------------
design_image = Image.open(AI_IMAGE_PATH).convert("RGBA")
print(f"design_image size: {design_image.size}, mode: {design_image.mode}")


# Ensure the design image is resized to fit the sublayer

# if layer_width < layer_height:
#     # If the sublayer is wider than tall, fit to width
#     design_image = design_image.resize((layer_width, layer_width))
# else:
#     # If the sublayer is taller than wide, fit to height
#     design_image = design_image.resize((layer_height, layer_height))

design_image = design_image.resize((1500, 1500))

print(f"✅ Design image resized to sublayer size.")

# --------------------------
# 8️⃣ PASTE ON BASE COMPOSITE
# --------------------------
base_image.paste(design_image, (x1+300, y1+650), design_image)

# --------------------------
# 9️⃣ SAVE FINAL RESULT
# --------------------------
base_image.save(OUTPUT_PATH)
print(f"✅ Final merged mockup saved: {OUTPUT_PATH}")

