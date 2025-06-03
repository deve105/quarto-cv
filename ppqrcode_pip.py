
import qrcode
from PIL import Image, ImageDraw

profile = "https://deve105.github.io/me/"
buyme = "https://buymeacoffee.com/enriquezvdv"

qr = qrcode.QRCode(
    version=6,  # size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border
)

# Add data to the QR code
qr.add_data(buyme)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="#348b0e", back_color="white").convert('RGBA')
qr_width, qr_height = img.size

# Create pixel dog image
dog_size = int(qr_width * 0.3)  # 30% of QR code size
dog_img = Image.new('RGBA', (dog_size, dog_size), (0, 0, 0, 0))
draw = ImageDraw.Draw(dog_img)

# Define pixel size
pixel = max(1, dog_size // 15)
colors = {
    'B': (80, 50, 20, 255),     # Brown
    'D': (120, 80, 40, 255),    # Dark Brown
    'W': (255, 255, 255, 255),  # White
    'K': (0, 0, 0, 255),        # Black
    'P': (255, 180, 180, 255),  # Pink
    'T': (0, 0, 0, 0)           # Transparent
}

# Pixel art dog pattern (15x15 grid)
dog_pixels = [
    "TTTTTTTTTTTTTTT",
    "TTTTTBBBBBBTTT",
    "TTTBBBBBBBBBBTT",
    "TTBBBBBBBBBBBBT",
    "TBBBWWBBBWWBBBT",
    "TBBBWKBBBWKBBBT",
    "TBBBBBBBBBDBBBT",
    "TBBBBBPPPBBBBT",
    "TBBBBPPPPPBBBBT",
    "TTBBBBDDDBBBBBT",
    "TTTBBBBBBBBBTT",
    "TTBBBBTTTBBBBT",
    "TBBBBTTTTBBBBT",
    "TBBBBTTTTTBBBBT",
    "TTBBBTTTTTBBBT"
]

# Draw the pixel dog
for y, row in enumerate(dog_pixels):
    for x, p in enumerate(row):
        if p != 'T':  # Skip transparent pixels
            draw.rectangle(
                [(x * pixel, y * pixel), ((x + 1) * pixel, (y + 1) * pixel)],
                fill=colors[p]
            )

# Calculate position to place dog image in center of QR code
dog_pos = ((qr_width - dog_size) // 2, (qr_height - dog_size) // 2)

# Create white background circle for the dog
circle_img = Image.new('RGBA', (dog_size, dog_size), (0, 0, 0, 0))
circle_draw = ImageDraw.Draw(circle_img)
circle_draw.ellipse([(0, 0), (dog_size, dog_size)], fill=(255, 255, 255, 220))

# Paste the images
img.paste(circle_img, dog_pos, circle_img)
img.paste(dog_img, dog_pos, dog_img)

# Save the result
img.save("qrcode2.png")
