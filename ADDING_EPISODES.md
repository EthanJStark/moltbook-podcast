# Adding New Episodes

## Process

### 1. Prepare Audio File

```bash
# Convert to MP3 if needed
ffmpeg -i input.wav -codec:a libmp3lame -b:a 128k output.mp3

# Rename with date convention
mv output.mp3 YYYYMMDD-episode-title.mp3
```

### 2. Create GitHub Release

```bash
# Tag release
git tag -a vX.Y.Z -m "Episode N: Title"
git push origin vX.Y.Z

# Create release with audio
gh release create vX.Y.Z \
  --title "Episode N: Title" \
  --notes "Episode description here." \
  path/to/YYYYMMDD-episode-title.mp3
```

### 3. Get Audio File Info

```bash
# Get file size in bytes
stat -f%z YYYYMMDD-episode-title.mp3  # macOS

# Get duration
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 \
  YYYYMMDD-episode-title.mp3
```

### 4. Update RSS Feed

Add new `<item>` to `feed.xml` (insert at top, after `<channel>`):

```xml
<item>
  <title>Episode N: Title</title>
  <itunes:title>Episode N: Title</itunes:title>
  <description>Episode description here.</description>
  <itunes:summary>Episode description here.</itunes:summary>
  <enclosure
    url="https://github.com/EthanJStark/moltbook-podcast/releases/download/vX.Y.Z/YYYYMMDD-episode-title.mp3"
    length="FILE_SIZE_IN_BYTES"
    type="audio/mpeg"/>
  <guid>https://github.com/EthanJStark/moltbook-podcast/releases/download/vX.Y.Z/YYYYMMDD-episode-title.mp3</guid>
  <pubDate>Day, DD Mon YYYY HH:MM:SS GMT</pubDate>
  <itunes:duration>MM:SS</itunes:duration>
  <itunes:explicit>no</itunes:explicit>
</item>
```

### 5. Update Website

Add new episode to `index.html`:

```html
<article class="episode">
    <h3>Episode N: Title</h3>
    <p class="episode-date">Month Day, Year</p>
    <p class="episode-description">Episode description here.</p>
    <audio controls>
        <source src="RELEASE_AUDIO_URL" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
</article>
```

### 6. Deploy

```bash
git add feed.xml index.html
git commit -m "feat: add episode N - title"
git push origin main
```

### 7. Validate

1. Wait 2 minutes for GitHub Pages deployment
2. Visit feed URL: https://ethanjstark.github.io/moltbook-podcast/feed.xml
3. Validate at https://podba.se/validate/
4. Test in podcast app

## Date Format Reference

RSS pubDate format (RFC 822):
```
Sat, 01 Feb 2026 00:00:00 GMT
```

Format: `Day, DD Mon YYYY HH:MM:SS GMT`

## Example

For a second episode released on February 15, 2026:

```bash
# Tag and release
git tag -a v0.2.0 -m "Episode 2: Another Great Topic"
git push origin v0.2.0
gh release create v0.2.0 \
  --title "Episode 2: Another Great Topic" \
  --notes "Description of second episode." \
  20260215-another-great-topic.mp3

# Get file info
stat -f%z 20260215-another-great-topic.mp3
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 \
  20260215-another-great-topic.mp3

# Update feed.xml and index.html with new episode
# Then commit and push
```
