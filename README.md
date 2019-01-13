# Google Fonts Mirror

## Why I need this mirror

China GFW may block google fonts in some area, even `fonts.googleapis.com` has its own Beijin server. It's not 100% stable for us to use google fonts, after all, its named `Google` which is hated by the Chinese government.

Someone will choice to use Chinese native CDN provider, but they are not friendly for other countries' people.

This mirror serve google fonts by the CDN of Github Pages, help chinese guys to create global Web sites.

## Usage

Replace `{Font_Family}` to your font family name:

```html
<link href="https://fonts.joway.io/css/{Font_Family}.css" rel="stylesheet" />

->

<link href="https://fonts.joway.io/css/Open+Sans.css" rel="stylesheet" />
```

Define the font family in your css:

```css
.cls {
  font-family: "Open Sans", sans-serif;
}
```
