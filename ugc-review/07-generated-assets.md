# Generated Assets

Produced from the real product photo
(`WhatsAppImage2026-07-12at16.11.38_2.jpg`) via `generate_image` with the
product passed as a tagged reference.

> **⏳ These links expire.** The URLs carry signed tokens valid for roughly a day
> from generation (27 Jul 2026). Download both files now and re-host them —
> once the token lapses the link is dead and the still has to be regenerated.

---

## ✅ Still 1 — Try-on

Person in their twenties wearing the tee, sunlit apartment, candid phone framing, 9:16.

```
https://dnznrvs05pmza.cloudfront.net/gemini/gemini-3-pro-image/images/6597d0d8-9f50-4c05-8199-1001f4f4fa78/A_person_in_their_twenties_standing_in_a_sunlit_apartment_we.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMGFjY2RkMDQwNGJhMTRmMCIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc4NTIxNDA4NH0.zjwBwlaHZ34f-hV2SyiZ-bb__ThcNkE_PzF4SsCqWXs
```

## ✅ Still 2 — Hanger / window light

Tee on a wooden hanger by a window, raking daylight on the weave, 9:16.
This is the color-story shot from `03-shot-list.md` (Shot C).

```
https://dnznrvs05pmza.cloudfront.net/gemini/gemini-3-pro-image/images/6d7354e5-0f4b-4342-a5e6-140f08d44514/The_exact_sage_green_t_shirt_from__tee___same_color__same_re.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNWFkN2E2MDNlN2Q1ZTllYiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc4NTI2OTM3OX0.xZRmK3ED7x3Tz1l9lB1MqY-5yyMc4pOpkFMotlAqaVs
```

## ❌ Not generated — workspace limit reached

- Collar macro still (Shot E)
- All video clips — hero motion, fabric detail, try-on turn

---

## Inspect before you use these

Neither still was viewed. This container's network policy blocks Runway's CDN,
so the files could not be pulled back for inspection — the URLs are reported as
returned by the API, not as verified images.

Check in this order:

1. **The `FEESBEES` wordmark.** Image models reliably mangle small text. If the
   letterforms are wrong on the try-on shot, that shot is unusable as-is.
2. **The green.** It should read sage/matcha, not mint and not olive. Compare
   against the original product photo side by side.
3. **The fit.** Relaxed straight body, not tapered.

If the wordmark is garbled, the fix is to reframe wider so the logo is small
enough to read as a mark rather than as letters — or shoot that shot for real.

## To finish the video

Credits are the only blocker. Once the workspace has room:

1. Feed **Still 2** to `generate_video` as `startFrame` with the hero motion
   prompt from `06-runway-prompts.md`.
2. Feed **Still 1** with the try-on turn prompt.
3. Generate the collar macro still, then animate it.

Use the Runway CDN URLs above as `startFrame`, not the Shopify URL — see the
hostname trap section in `06-runway-prompts.md`.
