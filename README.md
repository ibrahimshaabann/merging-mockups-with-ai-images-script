Absolutely — here’s your **full `README.md`** in clean Markdown, ready to copy and paste:

```markdown
# 🎨🧵 AI Design to Mockup Merger

This is a simple Python tool to **automate merging AI-generated designs onto PSD product mockups** — perfect for generating realistic product previews (like T-shirts) with minimal manual editing.

---

## 📂 Project Structure

```

merging-mockups-with-ai-images-script/
│
├── ai\_generated\_images/      # Place your AI-generated designs here
├── tshirt\_mockups/           # Place your PSD mockup files here
├── outputs/                  # Final merged images will be saved here
├── src/
│   ├── merge\_psd.py          # Main merging script
│   ├── requirements/         # Python dependencies
│
├── venv/                     # Python virtual environment (excluded by .gitignore)
└── .gitignore

````

---

## ⚙️ Features

✅ Open PSD mockup files  
✅ Select target layer group & sublayer  
✅ Automatically paste and resize AI designs  
✅ Output high-resolution merged product images  
✅ Works locally — no expensive design software needed

---

## 🚀 Quick Start

1️⃣ **Clone the repo**

```bash
git clone git@github.com:ibrahimshaabann/merging-mockups-with-ai-images-script.git
cd merging-mockups-with-ai-images-script
````

2️⃣ **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Install dependencies**

```bash
pip install -r src/requirements/requirements.txt
```

4️⃣ **Add your files**

* Place your **PSD mockup** in `tshirt_mockups/`
* Place your **AI-generated design** in `ai_generated_images/`

5️⃣ **Run the script**

```bash
python src/merge_psd.py
```

The final merged image will be saved to the `outputs/` folder.

---

## ⚡ Configuration

Edit `merge_psd.py` to:

* Set your PSD path
* Choose the target layer group and sublayer to insert your design

Example:

```python
PSD_PATH = 'tshirt_mockups/tshirt_mockup4.psd'
AI_IMAGE_PATH = 'ai_generated_images/ai_design1.png'
OUTPUT_PATH = 'outputs/final_mockup.png'

TARGET_LAYER_GROUP = 'Design and Color T-Shirt'
TARGET_SUBLAYER = 'Your Sublayer Name'
```

---

## 🗂️ Dependencies

* `psd-tools` — for PSD parsing
* `Pillow` — for image resizing & pasting

See `src/requirements/requirements.txt`.

---

## ❤️ Author

**Ibrahim Shaaban**
Backend Developer | Automation Enthusiast
📧 [ibrahimshaaban888@gmail.com](mailto:ibrahimshaaban888@gmail.com)

---

## 📜 License

MIT — use freely, contribute, and improve!

````

---

✅ **Copy this into a file named `README.md` in your project root**.  
✅ Commit & push it:  

```bash
git add README.md
git commit -m "Add detailed README"
git push origin main
````

Let me know if you’d like help writing badges or adding example images! 🚀✨
