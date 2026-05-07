from PIL import Image
import os

def optimize_image(input_path, output_path, quality=85):
    """Optimize an image file."""
    try:
        with Image.open(input_path) as img:
            # Preserve transparency for PNG and GIF
            if img.mode in ('RGBA', 'LA', 'P'):
                # For PNG, we can optimize without losing transparency
                img.save(output_path, optimize=True, quality=quality)
            else:
                # Convert to RGB if necessary (for JPEG)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.save(output_path, optimize=True, quality=quality)
    except Exception as e:
        # If optimization fails, copy the original
        import shutil
        shutil.copy2(input_path, output_path)
        raise e