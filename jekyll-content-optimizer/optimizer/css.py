import csscompressor
import os

def optimize_css(input_path, output_path):
    """Optimize a CSS file."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Compress CSS
        compressed = csscompressor.compress(content)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(compressed)
    except Exception as e:
        # If optimization fails, copy the original
        import shutil
        shutil.copy2(input_path, output_path)
        raise e