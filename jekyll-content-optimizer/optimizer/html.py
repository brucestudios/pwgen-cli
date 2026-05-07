import htmlmin
import os

def optimize_html(input_path, output_path):
    """Optimize an HTML file."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Minify HTML
        minified = htmlmin.minify(content, remove_empty_space=True, remove_all_empty_space=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(minified)
    except Exception as e:
        # If optimization fails, copy the original
        import shutil
        shutil.copy2(input_path, output_path)
        raise e