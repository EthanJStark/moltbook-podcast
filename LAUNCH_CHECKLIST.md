# Launch Checklist

## Pre-Launch
- [x] Repository created and GitHub Pages enabled
- [x] Audio files converted to podcast-optimized MP3
- [x] Audio uploaded to GitHub Releases
- [x] RSS feed created with valid iTunes tags
- [x] Podcast artwork added (3000x3000px)
- [x] Website landing page created
- [x] Feed validated locally with xmllint

## Testing (User Validation Required)
- [ ] Website accessible and functional at https://ethanjstark.github.io/moltbook-podcast/
- [ ] Audio plays in web browser
- [ ] RSS feed validates at https://podba.se/validate/
- [ ] Podcast loads in Apple Podcasts
- [ ] Episode plays in podcast app
- [ ] Mobile responsive design works
- [ ] Tested on multiple devices

## Automated Testing Completed
- [x] GitHub Pages deployment successful
- [x] RSS feed XML syntax valid
- [x] Artwork URL accessible (200 OK)
- [x] Audio file URL accessible (302 redirect to CDN)
- [x] Website index.html accessible (200 OK)
- [x] Feed.xml accessible (200 OK)

## Documentation
- [x] README updated with subscribe instructions
- [x] Episode addition guide created (ADDING_EPISODES.md)
- [x] Validation documentation created (VALIDATION.md)
- [x] Launch checklist created (this file)

## Launch
- [ ] Announce podcast availability
- [ ] Share RSS feed link
- [ ] Monitor for feed errors
- [ ] Test episode downloads
- [ ] Gather feedback from listeners

## Post-Launch
- [ ] Plan next episode
- [ ] Monitor analytics (if configured)
- [ ] Address any reported issues

## Manual Testing Instructions

### Test Website
1. Visit: https://ethanjstark.github.io/moltbook-podcast/
2. Verify artwork displays
3. Test audio player controls
4. Check responsive design on mobile

### Test RSS Feed
1. Visit: https://podba.se/validate/
2. Enter: https://ethanjstark.github.io/moltbook-podcast/feed.xml
3. Review validation results

### Test in Podcast App
1. Open Apple Podcasts (or preferred app)
2. File → Add a Podcast by URL
3. Paste: https://ethanjstark.github.io/moltbook-podcast/feed.xml
4. Verify podcast appears with correct title and artwork
5. Verify episode appears with correct metadata
6. Play episode and verify audio loads
