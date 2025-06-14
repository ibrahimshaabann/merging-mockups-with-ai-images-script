from psd_tools import PSDImage
from PIL import Image

# --------------------------
# 1️⃣ CONFIG
# --------------------------
PSD_PATH = 'tshirt_mockups/tshirt_mockup4.psd'
AI_IMAGE_PATH = 'ai_generated_images/ai_design1.png'
OUTPUT_PATH = 'outputs/final_mockup_with_shadows.png'

TARGET_LAYER_GROUP = 'Design and Color T-Shirt'
TARGET_SUBLAYER = 'Your Design Withiut Sleeve (double click)'   # typo? adjust spelling if needed!

# Shadow & Light layers to overlay
OVERLAY_LAYERS = ['More Shadow', 'Light', 'Light and Shadow T-Shirt']

# --------------------------
# 2️⃣ OPEN PSD & BASE IMAGE
# --------------------------
psd = PSDImage.open(PSD_PATH)
base_image = psd.composite().convert("RGBA")
print(f"✅ PSD opened: {PSD_PATH}")

# --------------------------
# 3️⃣ FIND TARGET GROUP
# --------------------------
target_group = next((layer for layer in psd if layer.name == TARGET_LAYER_GROUP), None)
if not target_group:
    raise Exception(f"Layer group '{TARGET_LAYER_GROUP}' not found!")

print(f"✅ Found layer group: {target_group.name}")

# --------------------------
# 4️⃣ FIND TARGET SUBLAYER
# --------------------------
target_sublayer = next((layer for layer in target_group if layer.name == TARGET_SUBLAYER), None)
if not target_sublayer:
    raise Exception(f"Sublayer '{TARGET_SUBLAYER}' not found!")

print(f"✅ Found sublayer: {target_sublayer.name}")

# --------------------------
# 5️⃣ Get sublayer bbox
# --------------------------
x1, y1, x2, y2 = target_sublayer.bbox
layer_width = x2 - x1
layer_height = y2 - y1

print(f"📐 Sublayer bbox: {target_sublayer.bbox}")

# --------------------------
# 6️⃣ Open & Resize AI Design
# --------------------------
design_image = Image.open(AI_IMAGE_PATH).convert("RGBA")
design_image = design_image.resize((1300, 1300), Image.LANCZOS)

print(f"✅ Design image resized to: {design_image.size}")

# --------------------------
# 7️⃣ Paste design on base
# --------------------------
base_image.paste(design_image, (x1, y1), design_image)

print(f"✅ Design pasted at: {(x1, y1)}")

# --------------------------
# 8️⃣ Overlay shadow & light layers
# --------------------------
for layer_name in OVERLAY_LAYERS:
    overlay_layer = next((layer for layer in target_group if layer.name == layer_name), None)
    if not overlay_layer:
        raise Exception(f"Overlay layer '{layer_name}' not found!")

    overlay_image = overlay_layer.composite().convert("RGBA")

    # Paste the overlay at its bbox location
    ox1, oy1, _, _ = overlay_layer.bbox

    # Create a transparent RGBA the same size as base
    temp = Image.new("RGBA", base_image.size)
    temp.paste(overlay_image, (ox1, oy1), overlay_image)

    # Blend with base image
    base_image = Image.alpha_composite(base_image, temp)

    print(f"✅ Applied overlay: {layer_name}")

# --------------------------
# 9️⃣ Save final result
# --------------------------
base_image.save(OUTPUT_PATH)
print(f"✅ Final mockup with shadows saved: {OUTPUT_PATH}")
