# Extensions
So svgs don't seem to work with the manifest image

1. turn on developer mode
2. load unpacked extension
3. check error logs in the settings

## tools
- [chrome-types from npm for typescript](https://www.npmjs.com/package/chrome-types)
- [csp](https://developer.chrome.com/docs/extensions/mv3/manifest/content_security_policy/)

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

"The popup
Many extensions use a popup (popup.html) to provide functionality, such as displaying a list of tabs, or additional information regarding the current tab. Users can easily find it by clicking on the extension toolbar icon. When the user navigates away it will automatically close.

The options page
The options page (options.html) provides a way for users to customize an extension, such as choosing which sites the extension will run on. Users can access the options page in several ways as described in Finding the options page." - https://developer.chrome.com/docs/extensions/mv3/architecture-overview/#html-files