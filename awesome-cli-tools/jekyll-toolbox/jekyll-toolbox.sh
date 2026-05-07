#!/bin/bash

# Jekyll Toolbox - Main script
# A collection of useful scripts for maintaining Jekyll sites

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_SITE_DIR="_site"

# Display help message
show_help() {
    cat << EOF
Jekyll Toolbox - A collection of useful scripts for maintaining Jekyll sites

Usage:
  $0 <command> [options]

Commands:
  check-links     Check for broken links in the generated Jekyll site
  generate-sitemap Generate a sitemap.xml file for the Jekyll site
  help            Show this help message

Examples:
  $0 check-links
  $0 check-links --dir ./my-site/_site
  $0 generate-sitemap --url https://example.com --dir ./_site
EOF
}

# Check links command
check_links() {
    local site_dir="$DEFAULT_SITE_DIR"
    local check_external=false
    
    # Parse options
    while [[ $# -gt 0 ]]; do
        case $1 in
            --dir)
                site_dir="$2"
                shift 2
                ;;
            --external)
                check_external=true
                shift
                ;;
            --help|-h)
                show_help
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # Validate site directory
    if [[ ! -d "$site_dir" ]]; then
        echo "Error: Site directory '$site_dir' does not exist."
        echo "Make sure you have built your Jekyll site first (jekyll build)."
        exit 1
    fi
    
    echo "Checking links in: $site_dir"
    
    # Find all HTML files
    local html_files
    html_files=$(find "$site_dir" -name "*.html" -type f)
    
    if [[ -z "$html_files" ]]; then
        echo "No HTML files found in $site_dir"
        exit 0
    fi
    
    local broken_count=0
    local total_checked=0
    
    # Process each HTML file
    while IFS= read -r file; do
        echo "Checking: $file"
        
        # Extract links (both internal and external)
        local links
        links=$(grep -oE 'href="[^"]+"' "$file" | cut -d'"' -f2)
        
        while IFS= read -r link; do
            # Skip empty links, anchors, and javascript links
            [[ -z "$link" || "$link" =~ ^# || "$link" =~ ^javascript: ]] && continue
            
            ((total_checked++))
            
            # Handle internal links (relative paths)
            if [[ ! "$link" =~ ^https?:// ]]; then
                # Resolve relative to site root
                local target_path
                if [[ "$link" =~ ^/ ]]; then
                    target_path="${site_dir}${link}"
                else
                    # Relative to current file's directory
                    target_path="$(dirname "$file")/$link"
                fi
                
                # Normalize path
                target_path=$(realpath -m "$target_path")
                
                if [[ ! -f "$target_path" ]]; then
                    echo "  BROKEN (internal): $link"
                    ((broken_count++))
                fi
            # Handle external links (if enabled)
            elif [[ "$check_external" == true ]]; then
                if ! curl -sSf --head --max-time 10 "$link" >/dev/null; then
                    echo "  BROKEN (external): $link"
                    ((broken_count++))
                fi
            fi
        done <<< "$links"
    done <<< "$html_files"
    
    echo ""
    echo "Link check complete."
    echo "Total links checked: $total_checked"
    echo "Broken links found: $broken_count"
    
    if [[ $broken_count -gt 0 ]]; then
        exit 1
    fi
}

# Generate sitemap command
generate_sitemap() {
    local site_dir="$DEFAULT_SITE_DIR"
    local site_url=""
    local changefreq="weekly"
    local priority="0.5"
    
    # Parse options
    while [[ $# -gt 0 ]]; do
        case $1 in
            --dir)
                site_dir="$2"
                shift 2
                ;;
            --url)
                site_url="$2"
                shift 2
                ;;
            --changefreq)
                changefreq="$2"
                shift 2
                ;;
            --priority)
                priority="$2"
                shift 2
                ;;
            --help|-h)
                show_help
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # Validate inputs
    if [[ ! -d "$site_dir" ]]; then
        echo "Error: Site directory '$site_dir' does not exist."
        exit 1
    fi
    
    if [[ -z "$site_url" ]]; then
        echo "Error: Site URL is required (--url)."
        exit 1
    fi
    
    # Ensure site_url doesn't end with slash
    site_url="${site_url%/}"
    
    echo "Generating sitemap for: $site_dir"
    echo "Site URL: $site_url"
    
    # Create sitemap header
    local sitemap_file="${site_dir}/sitemap.xml"
    {
        echo '<?xml version="1.0" encoding="UTF-8"?>'
        echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    } > "$sitemap_file"
    
    # Find all HTML files (excluding sitemap.xml itself)
    local html_files
    html_files=$(find "$site_dir" -name "*.html" -type f ! -name "sitemap.xml")
    
    local url_count=0
    
    while IFS= read -r file; do
        # Get relative path from site directory
        local relative_path
        relative_path="${file#"$site_dir"/}"
        
        # Skip if it's still the full path (not in site_dir)
        if [[ "$relative_path" == "$file" ]]; then
            continue
        fi
        
        # Create URL
        local url="${site_url}/${relative_path}"
        
        # Get last modification time
        local mod_time
        mod_time=$(date -r "$file" +"%Y-%m-%d")
        
        # Add URL entry to sitemap
        {
            echo "  <url>"
            echo "    <loc>$url</loc>"
            echo "    <lastmod>$mod_time</lastmod>"
            echo "    <changefreq>$changefreq</changefreq>"
            echo "    <priority>$priority</priority>"
            echo "  </url>"
        } >> "$sitemap_file"
        
        ((url_count++))
    done <<< "$html_files"
    
    # Close sitemap
    echo '</urlset>' >> "$sitemap_file"
    
    echo ""
    echo "Sitemap generated: $sitemap_file"
    echo "URLs included: $url_count"
}

# Main script logic
main() {
    if [[ $# -eq 0 ]]; then
        show_help
        exit 1
    fi
    
    case "$1" in
        check-links)
            shift
            check_links "$@"
            ;;
        generate-sitemap)
            shift
            generate_sitemap "$@"
            ;;
        help|-h|--help)
            show_help
            exit 0
            ;;
        *)
            echo "Unknown command: $1"
            show_help
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"