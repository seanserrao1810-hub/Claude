# AI Video Generation Prompts

For generating the UGC clip in Runway when a live creator shoot isn't available.

## Required input

A **publicly fetchable** image of the tee. The Shopify storefront
(`nwbqt1-e6.myshopify.com`) returns 403 to automated requests, so the product
page itself can't be scraped.

**The workaround:** Shopify's CDN serves images publicly even when the storefront
is password-protected. On the product page, right-click the image →
*Copy image address*. The result looks like:

```
https://cdn.shopify.com/s/files/1/xxxx/xxxx/files/<name>.jpg?v=1234567890
```

That URL will work. The `/products/...` page URL will not.

---

## Prompt 1 — Hero product motion (i2v)

Model `seedance-2` · ratio `9:16` · 720p · 5s · startFrame = product image

> Handheld phone footage of the sage green t-shirt hanging on a wooden hanger by
> a bright window in a lived-in bedroom. Slow natural tilt upward, subtle camera
> shake as if held by hand. Soft daylight rakes across the cotton, showing the
> weave texture and making the sage green shift from warm to cool. Shallow depth
> of field, background softly blurred. Natural color, no stylization, no text
> overlays. The garment stays exactly as shown in the reference — same color,
> same small black chest wordmark, same fit.

## Prompt 2 — Creator try-on (i2v)

Model `seedance-2` · ratio `9:16` · 720p · 5s · referenceImages = product image, tag `tee`

> A person in their twenties wearing @tee, filmed on a phone held at arm's length
> in a sunlit apartment. They turn slowly to show how the shirt falls, glance down
> at the chest print, then look back at the camera and give a small approving nod.
> Casual handheld framing, slightly off-center, natural window light, authentic
> vlog aesthetic. Neutral cream trousers. No text, no logos other than the one on
> the shirt.

## Prompt 3 — Fabric detail (i2v)

Model `seedance-2` · ratio `9:16` · 720p · 5s · startFrame = product image

> Extreme close-up, phone macro, of a hand running a thumb along the ribbed collar
> of the sage green t-shirt, then flicking a fingernail across the small black
> chest wordmark. Soft directional daylight, visible cotton weave, very shallow
> focus. Micro camera shake. Documentary realism, no stylization.

## Prompt 4 — Multi-shot sequence

`generate_multishot_video` · mode `custom` · ratio `9:16` · 1080p · 15s · firstSceneImage = product image

1. > Phone footage of a cardboard mailer being opened on a bed, a folded sage green t-shirt inside, handheld, natural light.
2. > The same sage green t-shirt held up to a bright window, slowly tilting so the green shifts warm to cool, cotton weave visible.
3. > Macro close-up of a thumb running along the ribbed collar and the small black chest wordmark, very shallow focus.
4. > A person wearing the shirt, turning slowly in a sunlit room, phone held at arm's length, casual vlog framing.
5. > The person facing the camera, shrugging with a small approving smile, then the shot cuts.

---

## Rules

- **Always pass the real product image** as `startFrame` or `referenceImages`. A
  text-only generation invents a lookalike tee — wrong green, wrong wordmark —
  and that's a fabricated product shot, not a review of this product.
- Keep the wordmark small and unemphasized. Models distort small text; a
  close-up on `FEESBEES` will render it as garbled letterforms.
- Generate **B-roll only.** Let AI handle the product and texture shots; the
  spoken review should be a real person. A synthetic talking head delivering a
  first-person product opinion is a fake testimonial, and platforms increasingly
  label it as such.
- If the clip is AI-generated, disclose it. Meta and TikTok both require an
  AI-content label, and both detect it independently of what you declare.
