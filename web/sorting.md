# When you don't know js but want to add and sort some thing on a site

```js
temp1 = "<global var from dev console>"
var a = []; temp1.childNodes[0].childNodes.forEach(x=> a.push(x));
a.sort((b,c) => { return b.firstChild.attributes['aria-label'].value.localeCompare(c.firstChild.attributes['aria-label'].value,'en')})
a.forEach(x=>console.log(x.childNodes[0].attributes['aria-label'].value))
a.map(x=>temp1.firstElementChild.appendChild(x))
```