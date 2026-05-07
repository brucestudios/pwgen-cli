import jsmin
import os

def optimize_js(input_path, output_path):
    """Optimize a JavaScript file."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Minify JavaScript
        minified = jsmin.jsmin(content)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(minified)
    except Exception as e:
        # If optimization fails, copy the original
        import shutil
        shutil.copy2(input_path, output_path)
        raise e