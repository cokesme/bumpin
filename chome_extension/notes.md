# Extensions
So svgs don't seem to work with the manifest image

1. turn on developer mode
2. load unpacked extension
3. check error logs in the settings

## tools
- [chrome-types from npm for typescript](https://www.npmjs.com/package/chrome-types)

## Possible folder structure
```
extension/
 |-- manifest.json
 |-- background.js
 |-- scripts/
    |_ content.js
    react.production.min.js
 |-- popup/
     |_ popup.html
     |_ popup.js
     |_ popup.css
 |_ images/
    |-- icon.png...
```