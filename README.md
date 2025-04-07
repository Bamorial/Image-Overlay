# Image-Overlay

This Python script generates a pixelated version of an image, applying a stylized "shadow" overlay texture to each pixel block. It's useful for creating aesthetic poster-like effects, low-res illustrations, or emoji/LEGO-style art.

---

## 🖼️ Example

| Original Image | Lego Overlay |
|----------------|------------------|
| ![Original](images/in.png) | ![Shadowed](images/out.png) |

## How It Works

1. The input image is resized to a low-resolution grid.
2. Each pixel becomes a `windowSize x windowSize` block of its original color.
3. A grayscale texture (like a shading or grain pattern) is applied on top of each block to simulate shadows.
4. The final image is a stylized mosaic.

## Getting Started

### 1. Install Requirements

This script requires Python 3 and the following libraries:

```bash
pip install numpy opencv-python
```
### 2. Set paths
  Set the paths to your input image, and the textures folder. You can find some examples in the images and textures folders.
```python
originImage = cv.imread("PATH_TO_THE_INPUT_PICTURE")
overlay_texture_path = "PATH_TO_THE_TEXTURE"
```
### 3. Run 
```bash
  python overlay.py
```
## Output 
  The script will:
  * Show the final mosaic in a window
  * Save it as output_image.png
