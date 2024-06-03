Personal blog, mainly introducing AI related knowledge.

https://blog.aihub2022.top/

## Get started

### vercel analytics

Add js in `layouts/partials/head/script.html` is customized for the vercel Analytics.

### sidebar-left

The sidebar-left is customized. So, If the theme needs to be updated, we need to

- sync the sidebar-left from the theme `./sync-sidebar-left.sh`
- and then update the content with `layouts/partials/sidebar/qr_code.html`

### widget

- `categories/tag-cloud.html`, remove icon and add <a> tag to Category/Tags list
