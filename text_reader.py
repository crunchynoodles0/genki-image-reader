import pytesseract
from PIL import Image, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Open the image
img = Image.open(r"genki_chapters/chapter13.png")

# Convert to grayscale (makes it easier for OCR)
img = img.convert("L")

enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.5)


# Extract text from the image
print(pytesseract.image_to_string(img, lang= 'jpn'))


