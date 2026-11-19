# Starter prompt for the Squarespace build

Use this in a Claude session that can control your browser: the Claude desktop app on your computer with the Claude in Chrome extension connected, and Chrome signed in to Squarespace. Open the session in a checkout of the `working` repo on branch `claude/serene-cerf-5mo7lv` so it can read these files.

Copy everything in the box.

```text
Build the Plan For Your Goals one-page site in Squarespace, using Claude in Chrome. I am signed in to Squarespace in Chrome.

Read these files first, in this order:
1. landing-page/BUILD-SHEET.md  (the order of work and the exact text to paste)
2. landing-page/planforyourgoals-landing-mockup.html  (what the page should look like)
3. landing-page/mockup/assets/  (logo, photo, SOEF logo, favicon)

Follow the build sheet's "Rules for whoever builds this" without exception:
- Do not publish the site. Keep it private, on the trial, on Squarespace's built-in address.
- Do not buy anything. Stop at any billing screen and tell me.
- Do not connect or change any domain or DNS.
- Do not change the live Secure On Every Front site. If you start from a copy of it, work only in the copy.
- Paste the two disclosure blocks exactly as written. Leave [FIRM EMAIL] as a marked placeholder; I will fill it in myself.
- Do not load redirects.txt. That is a launch-day step.
- Stop and ask me before any step that deletes something outside the new site, or when a screen does not match the build sheet in a way that matters.

Use Route A in step 1 (copy the SOEF site, then strip it) if the Duplicate website option exists. If it does not, use Route B and tell me.

Work one build-sheet step at a time. After the header, after each page section, and after the footer, take a screenshot and compare it with the mock-up before moving on.

When you finish, run the build sheet's step 8 checklist and report each line as done or not done, with the private preview address and desktop and phone screenshots. List anything you could not do and why.
```

## Before you start that session

- Have your disclosure file open so you can paste the firm email address into the footer disclosure when the build is done.
- The build session will ask Chrome for permission to act on squarespace.com. That prompt is expected.
- The new site is a trial. Squarespace will ask for a subscription only when you choose to take it live.
