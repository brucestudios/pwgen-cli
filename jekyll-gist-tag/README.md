# Jekyll Gist Tag

A Jekyll plugin that generates a page listing all public gists for a given GitHub username.

## Installation

1. Add this plugin to your Jekyll site's `_plugins` directory (or clone this repo into your site's `_plugins` directory).
2. Ensure you have the `net/http` and `json` libraries (they are part of Ruby's standard library).
3. Add the following to your site's `_config.yml`:

   ```yaml
   gist_tag_username: "your_github_username"
   ```

4. The plugin will generate a page at `/gist/your_github_username/index.html` listing all public gists.

## Usage

After installation and configuration, run your Jekyll site as usual. The plugin will generate a page for the specified GitHub username.

## Example

If your `_config.yml` contains:

```yaml
gist_tag_username: "octocat"
```

Then visiting `/gist/octocat/` on your site will show a list of all public gists for the user `octocat`.

## License

MIT