# Podcast Feed Validation

## Last Validated: 2026-02-01

### Local XML Validation
- Status: ✅ Pass
- Tool: xmllint
- Issues: None

### Podbase Validator
- Status: ⏳ Pending manual validation
- URL: https://podba.se/validate/
- Feed URL to test: https://ethanjstark.github.io/moltbook-podcast/feed.xml
- Instructions: Visit the validator URL and enter the feed URL above

### RSS Feed Structure
- ✅ RSS 2.0 compliant
- ✅ iTunes namespace included
- ✅ Required iTunes tags present (author, summary, owner, explicit, category)
- ✅ Episode enclosure with audio URL
- ✅ Valid pubDate format (RFC 822)
- ✅ Artwork URL included

### Tested In Apps
- Apple Podcasts: ⏳ Not yet tested (user validation needed)
- Overcast: ⏳ Not yet tested
- Pocket Casts: ⏳ Not yet tested

### Known Issues
None

### Manual Testing Steps

To complete validation:

1. Visit https://podba.se/validate/
2. Enter feed URL: https://ethanjstark.github.io/moltbook-podcast/feed.xml
3. Review validation results
4. Test in podcast app:
   - Open Apple Podcasts (or your preferred app)
   - File → Add a Podcast by URL
   - Paste: https://ethanjstark.github.io/moltbook-podcast/feed.xml
   - Verify podcast appears with correct metadata
   - Test audio playback
