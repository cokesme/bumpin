# All the frameworks

# .NET 
ASP.NET is the main framework. MSFT a long time ago made Active Server Pages which had .asp files programmed in vbscript. Modern day use .aspx extension to donate asp.net coded in c#.

# Javascript notes
Used `fnm` to install the latest `nodejs` and enabled `corepack` to install `pnpm` then made `Vercel` account
## Nextjs setup

Used: https://github.com/vercel/next.js/tree/canary/packages/create-next-app
```
>pnpm create next-app
.../Local/pnpm/store/v3/tmp/dlx-2076     |   +1 +
Packages are hard linked from the content-addressable store to the virtual store.
  Content-addressable store is at: C:\Users\test\AppData\Local\pnpm\store\v3
  Virtual store is at:             ../../../../../AppData/Local/pnpm/store/v3/tmp/dlx-2076/node_modules/.pnpm
.../Local/pnpm/store/v3/tmp/dlx-2076     | Progress: resolved 1, reused 0, downloaded 1, added 1, done
√ What is your project named? ... awfl
√ Would you like to use TypeScript with this project? ... No / Yes
√ Would you like to use ESLint with this project? ... No / Yes
Creating a new Next.js app in C:\Users\test\Documents\code\awfl\client\next\awfl.

Using pnpm.

Installing dependencies:
- react
- react-dom
- next
- typescript
- @types/react
- @types/node
- @types/react-dom
- eslint
- eslint-config-next

Packages: +249
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Packages are hard linked from the content-addressable store to the virtual store.
  Content-addressable store is at: C:\Users\test\AppData\Local\pnpm\store\v3
  Virtual store is at:             node_modules/.pnpm
Downloading registry.npmjs.org/next/13.0.5: 8.56 MB/8.56 MB, done
Downloading registry.npmjs.org/typescript/4.9.3: 11.6 MB/11.6 MB, done
Downloading registry.npmjs.org/@next/swc-win32-x64-msvc/13.0.5: 25.7 MB/25.7 MB, done
Progress: resolved 261, reused 0, downloaded 249, added 249, done
node_modules/.pnpm/core-js-pure@3.26.1/node_modules/core-js-pure: Running postinstall script, done in 244ms

dependencies:
+ @types/node 18.11.9
+ @types/react 18.0.25
+ @types/react-dom 18.0.9
+ eslint 8.28.0
+ eslint-config-next 13.0.5
+ next 13.0.5
+ react 18.2.0
+ react-dom 18.2.0
+ typescript 4.9.3

Done in 1m 17.8s

Initializing project with template: default

Success! Created awfl at C:\Users\test\Documents\code\awfl\client\next\awfl
```

### ESlint
Not quite sure why this doesn't include the typescript linting since that is something I would expect based on: https://learntypescript.dev/12/l3-eslint
```
npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```
```
Copy
{
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 2018,
    "sourceType": "module"
  },
  "plugins": ["@typescript-eslint"],
  "extends": ["plugin:@typescript-eslint/recommended"]
}
```

# sorting
When you don't know js but want to add and sort some thing on a site

```js
temp1 = "<global var from dev console>"
var a = []; temp1.childNodes[0].childNodes.forEach(x=> a.push(x));
a.sort((b,c) => { return b.firstChild.attributes['aria-label'].value.localeCompare(c.firstChild.attributes['aria-label'].value,'en')})
a.forEach(x=>console.log(x.childNodes[0].attributes['aria-label'].value))
a.map(x=>temp1.firstElementChild.appendChild(x))
```

### React 
[devtools for react](https://reactjs.org/blog/2015/09/02/new-react-developer-tools.html#installation)