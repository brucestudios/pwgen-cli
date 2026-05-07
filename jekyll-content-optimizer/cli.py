import click
import os
import sys
from .optimizer.image import optimize_image
from .optimizer.html import optimize_html
from .optimizer.css import optimize_css
from .optimizer.js import optimize_js

@click.group()
def cli():
    """Jekyll Content Optimizer CLI."""
    pass

@cli.command()
@click.option('--source', '-s', required=True, help='Source directory (e.g., _site)')
@click.option('--output', '-o', required=True, help='Output directory for optimized files')
@click.option('--image-quality', '-q', default=85, help='Image quality (1-100)')
def optimize(source, output, image_quality):
    """Optimize all files in the source directory."""
    if not os.path.exists(source):
        click.echo(f"Error: Source directory '{source}' does not exist.", err=True)
        sys.exit(1)
    
    os.makedirs(output, exist_ok=True)
    
    for root, dirs, files in os.walk(source):
        # Skip directories that start with dot (like .git)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, source)
            dest_path = os.path.join(output, rel_path)
            
            # Ensure destination directory exists
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            # Optimize based on file extension
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                optimize_image(src_path, dest_path, quality=image_quality)
                click.echo(f"Optimized image: {rel_path}")
            elif file.lower().endswith('.html'):
                optimize_html(src_path, dest_path)
                click.echo(f"Optimized HTML: {rel_path}")
            elif file.lower().endswith('.css'):
                optimize_css(src_path, dest_path)
                click.echo(f"Optimized CSS: {rel_path}")
            elif file.lower().endswith('.js'):
                optimize_js(src_path, dest_path)
                click.echo(f"Optimized JS: {rel_path}")
            else:
                # Copy other files as-is
                import shutil
                shutil.copy2(src_path, dest_path)
                click.echo(f"Copied: {rel_path}")

@cli.command()
@click.option('--source', '-s', required=True, help='Source directory to watch')
@click.option('--output', '-o', required=True, help='Output directory for optimized files')
@click.option('--image-quality', '-q', default=85, help='Image quality (1-100)')
def watch(source, output, image_quality):
    """Watch for changes and optimize incrementally."""
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        click.echo("Error: watchdog is required for watch mode. Install with: pip install watchdog", err=True)
        sys.exit(1)
    
    class OptimizerHandler(FileSystemEventHandler):
        def on_modified(self, event):
            if not event.is_directory:
                click.echo(f"Detected change: {event.src_path}")
                # For simplicity, we re-run optimization on the whole site.
                # In a more advanced version, we would only optimize the changed file.
                ctx = click.get_current_context()
                ctx.invoke(optimize, source=source, output=output, image_quality=image_quality)
        
        def on_created(self, event):
            if not event.is_directory:
                click.echo(f"Detected new file: {event.src_path}")
                ctx = click.get_current_context()
                ctx.invoke(optimize, source=source, output=output, image_quality=image_quality)
    
    event_handler = OptimizerHandler()
    observer = Observer()
    observer.schedule(event_handler, source, recursive=True)
    observer.start()
    
    click.echo(f"Watching {source} for changes... Press Ctrl+C to stop.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    cli()