# Squarespace build sheet: Plan For Your Goals one-page site

Written 2026-11-19. Use with `planforyourgoals-landing-mockup.html` (what it should look like) and `mockup/assets/` (the image files). The mock-up is the reference; this sheet is the order of work and the exact text.

Squarespace menu names below are from memory of Squarespace 7.1 and may differ slightly from what is on screen. Where they differ, follow the screen.

## Rules for whoever builds this

1. **Do not publish.** The site stays on its trial, on Squarespace's built-in address, private.
2. **Do not buy anything.** No subscription, no domain, no add-on. Stop at any billing screen.
3. **Do not connect or change any domain or DNS.** That waits for the developer conversation.
4. **Do not change the live Secure On Every Front site.** If the build starts from a copy of it, work only in the copy.
5. **Paste the text exactly.** The two disclosure blocks are approved wording. No rewording, no trimming.
6. **Stop and ask** if a step would delete something outside the new site, or if a screen does not match this sheet in a way that matters.

## Step 1. Create the site

Pick one. The first is faster and matches SOEF's look exactly.

**Route A (recommended): copy the SOEF site, then strip it.**

1. In the Squarespace dashboard, open the menu on the Secure On Every Front site and choose Duplicate website. Confirm the option is there before relying on it.
2. Rename the copy **Plan For Your Goals**.
3. In the copy, delete every page (main navigation, not linked, and any store, blog or form pages).
4. In the copy, clear anything that came along and does not belong:
   - Code injection (header and footer) and any page-level code
   - Tracking pixels and analytics IDs under marketing or external-API settings
   - Announcement bar, pop-ups, cart icon, member areas
   - Connected accounts and form storage
5. Leave Site Styles (fonts, colours, buttons) as copied.

**Route B: start blank.** Create a new site from a blank template and set Site Styles by hand using step 2.

## Step 2. Site styles

Skip the values that Route A already carried over; just check them.

| Setting | Value |
|---|---|
| Heading font | Montserrat, weight 400 |
| Body font | Roboto, weight 400, base size about 1.1rem |
| Button font | Roboto, weight 500, capitals, letter spacing 0.05em |
| Button shape | Pill |
| Button colours | Background `#DA5B37`, text `#EAE6DD` |
| Navy | `#1B365D` |
| Cream | `#EAE6DD` |
| Gold | `#F0CD5F` |
| Orange | `#DA5B37` |
| Ink (text on light) | `#2D2D2A` |

Section colour pairs used on the page:

| Name in this sheet | Background | Text | Small label colour |
|---|---|---|---|
| Navy | `#1B365D` | `#EAE6DD` | `#F0CD5F` |
| Cream | `#EAE6DD` | `#2D2D2A` | `#2D2D2A` |
| Gold | `#F0CD5F` | `#2D2D2A` | `#2D2D2A` |

A 4px orange line (`#DA5B37`) separates sections where the sheet says "orange rule." A line block or a section divider both work.

## Step 3. Site settings

| Setting | Value |
|---|---|
| Site title | Plan For Your Goals, LLC |
| Logo | `mockup/assets/pfyg-logo-white.png` (white logo, for the navy header) |
| Browser icon | `mockup/assets/favicon.png` |
| Site availability | Private (trial default). Do not change |
| Home page SEO title | Plan For Your Goals, LLC \| Fiduciary Financial Planning \| Gulf Breeze, FL |
| Home page SEO description | Plan For Your Goals, LLC is a State of Florida registered investment adviser in Gulf Breeze, FL, and the advisory firm behind Secure On Every Front. |
| Tracking | None beyond Squarespace's built-in analytics. No ad pixels |

## Step 4. Header

Background navy. No navigation pages.

| Element | Text | Link |
|---|---|---|
| Logo (left) | image | Home |
| Text link (right) | Client login | `https://www.rightcapital.com/login?cobrand=Zi7CXrBhIY5Lisa3u-LbMA&type=client` (new tab) |
| Button (right) | Visit Secure On Every Front | `https://www.secureoneveryfront.com/?utm_source=planforyourgoals.com&utm_medium=referral&utm_campaign=firm-page&utm_content=header` (new tab) |

Squarespace's header takes one button and navigation links. Add "Client login" as an external navigation link. On phones, hide the header button if the header crowds; the hero has the same button.

## Step 5. The page

One page, set as the home page, web address `/`. Six sections in this order.

### Section 1. Hero (Navy, orange rule at the bottom)

Two columns on desktop: text left, photo right. Stacked on phones, text first.

Small label (capitals, gold):

> Plan For Your Goals, LLC

Heading 1:

> The advisory firm behind Secure On Every Front.

Large paragraph:

> I'm David Roberts, CEPA®. Plan For Your Goals, LLC is my firm, a State of Florida registered investment adviser in Gulf Breeze. This page tells you who I am, how I'm paid, and where to go next.

Button: **Visit Secure On Every Front**
Link: `https://www.secureoneveryfront.com/?utm_source=planforyourgoals.com&utm_medium=referral&utm_campaign=firm-page&utm_content=hero` (new tab)

Small text under the button:

> For veteran business owners. Takes you to secureoneveryfront.com.

Photo: `mockup/assets/david-roberts.jpg`, square.
Alt text: David Roberts standing on the shore in Gulf Breeze, Florida
Caption: David Roberts, CEPA®

Below the two columns, a thin line, then three short facts side by side (stacked on phones):

| Bold line | Line under it |
|---|---|
| Registered investment adviser | State of Florida |
| Firm CRD 320683 | Check the firm's record at adviserinfo.sec.gov (link: `https://adviserinfo.sec.gov/firm/summary/320683`, new tab) |
| Gulf Breeze, Florida | Clients served online |

### Section 2. Who I am and what the firm does (Cream)

Two columns: text left, a bordered "Firm facts" box right (box background a shade lighter, `#F6F3EC`).

Heading 2:

> Who I am and what the firm does

Paragraphs:

> I'm the firm's investment adviser representative, its managing member and its Chief Compliance Officer. It is a one-adviser firm. When you work with Plan For Your Goals, you work with me.

> The firm provides financial planning for households and for business owners, ongoing planning, hourly consulting, and a financial education program. Planning advice is given only under a signed agreement. Nothing on this page is advice for your situation.

> I'm a military spouse. My wife, Teresa Roberts, Col (Ret.) USAF, is the veteran in our house. The firm's planning program for veteran business owners is called Secure On Every Front, and it has its own site.

Firm facts box (heading "Firm facts", then label and value rows):

| Label | Value |
|---|---|
| Legal name | Plan For Your Goals, LLC |
| Registration | State of Florida registered investment adviser. Small line under it: Registration does not imply a certain level of skill or training. |
| Adviser | David L. Roberts, CEPA®. Small line under it: Individual CRD 7152116 |
| Office | 5954 E Bay Blvd, Gulf Breeze, FL 32563 |
| Phone | (855) 696-8284 (link `tel:+18556968284`) |
| Email | david@secureoneveryfront.com (mail link) |
| Brochure | Form ADV Part 2A (link `https://planforyourgoals.link/ADV`, new tab) |

### Section 3. How I'm paid (Navy, orange rule top and bottom)

Heading 2:

> How I'm paid, and where my interests can conflict with yours

Large paragraph:

> You should know this before you hire any adviser. Here it is in plain words.

Three cream boxes side by side (stacked on phones). Box headings in orange.

**Fiduciary advice**

> When I give planning or investment advice under a signed agreement, I act as a fiduciary. I am required to put your interests first and to tell you about my conflicts of interest.

**Fees by invoice**

> Planning clients pay the firm by invoice. I do not take fees out of client accounts, and I do not hold client money or securities. If a client uses an outside investment manager, that manager deducts its own fee and the firm receives a share of it. That is a conflict of interest.

**Insurance**

> I am also an independent licensed insurance agent and may receive commissions on insurance products. That is a conflict of interest. Insurance recommendations are made as an agent, not as a fiduciary, and no client is required to buy a product through me.

Line under the boxes ("Form ADV Part 2A" is a link to `https://planforyourgoals.link/ADV`, new tab, gold):

> The full detail is in the firm's Form ADV Part 2A. Read it before you decide.

### Section 4. Hand-off to Secure On Every Front (Gold, orange rule at the bottom)

Two columns: logo, label and heading left; text right.

Left column

- Image: `mockup/assets/soef-logo.png`. Alt text: Secure On Every Front
- Small label (capitals): For veteran business owners
- Heading 2: Your next stop is Secure On Every Front.

Right column

> Secure On Every Front is the planning program I co-founded with Teresa. It is built for veteran business owners whose household, payroll and future all ride on one company. The work runs in three tracks, in this order.

Three rows, each with a thin line above:

| Label | Name (heading font) | Line under it |
|---|---|---|
| Track 1 | Mission Capital Blueprint | Household security and owner pay. |
| Track 2 | Team Valuation Command | A team that carries more of the business, so less depends on the founder. |
| Track 3 | Walk-Away Authority Project | A coordinated plan for an eventual exit. |

Paragraph:

> Planning involves trade-offs. Results depend on your business, your household and the market, and no outcome is promised.

Button: **Visit Secure On Every Front**
Link: `https://www.secureoneveryfront.com/?utm_source=planforyourgoals.com&utm_medium=referral&utm_campaign=firm-page&utm_content=program` (new tab)

Small text under the button:

> You will leave this site and go to secureoneveryfront.com.

Then a thin line and the SOEF disclosure block in small type. **Approved wording. Paste exactly, both paragraphs.**

> Secure On Every Front is an education and planning program for veteran business owners, co-founded by David Roberts and Teresa Roberts, Col (Ret.) USAF. Content from Secure On Every Front, the VBO Lab, and its online community is general education only and is not individualized investment, tax, or legal advice.

> Advisory services are offered by Plan For Your Goals, LLC, a State of Florida Registered Investment Adviser. Insurance products and services are offered and sold through individually licensed and appointed agents.

### Section 5. Everyone else (Cream)

Two columns, text links only, no buttons. Headings in navy.

**Not a veteran business owner?**

> Email david@secureoneveryfront.com or call (855) 696-8284 and tell me what you are working on. I will tell you plainly whether the firm is a fit.

(Email is a mail link. Phone links to `tel:+18556968284`.)

**Already a client?**

> Your planning portal has not moved. Go to client login.

("Go to client login" links to `https://www.rightcapital.com/login?cobrand=Zi7CXrBhIY5Lisa3u-LbMA&type=client`, new tab.)

### Section 6. Footer (Navy)

Edit the site footer, not a page section. Three columns, then a thin line, then the disclosure.

Column 1

- Image: `mockup/assets/pfyg-logo-white.png`
- Plan For Your Goals, LLC
- 5954 E Bay Blvd, Gulf Breeze, FL 32563
- (855) 696-8284
- david@secureoneveryfront.com

Column 2, small gold label "Firm documents"

| Text | Link |
|---|---|
| Form ADV Part 2A | `https://planforyourgoals.link/ADV` (new tab) |
| Privacy Policy | `/privacy-policy` |
| Terms | `/terms` |
| Firm record at adviserinfo.sec.gov | `https://adviserinfo.sec.gov/firm/summary/320683` (new tab) |

Column 3, small gold label "Elsewhere"

| Text | Link |
|---|---|
| Secure On Every Front | `https://www.secureoneveryfront.com/?utm_source=planforyourgoals.com&utm_medium=referral&utm_campaign=firm-page&utm_content=footer` (new tab) |
| LinkedIn | `https://www.linkedin.com/in/david-roberts-planforyourgoals` (new tab) |
| Client login | `https://www.rightcapital.com/login?cobrand=Zi7CXrBhIY5Lisa3u-LbMA&type=client` (new tab) |

Disclosure, small type. **This is the WEBSITE block with the three changes David approved as CCO on 2026-11-19. Paste exactly.** One spot must be filled in by David: `[FIRM EMAIL]` is the firm's planforyourgoals.com address as it appears in his disclosure file. This sheet cannot carry it.

> Plan For Your Goals, LLC (PFYG), is a State of Florida registered investment adviser. PFYG may only transact business in those states in which it is registered or qualifies for an exemption or exclusion from registration requirements. PFYG's web site is limited to the dissemination of general information pertaining to its advisory services, together with access to additional investment-related information, articles written by third parties, firm written newsletters and/or publications, and third-party links. Accordingly, the publication of PFYG's web site on the Internet should not be construed by any consumer and/or prospective client as our Adviser's solicitation to effect, or attempt to effect transactions in securities, or the rendering of personalized investment advice for compensation, over the Internet. Any subsequent, direct communication by the Adviser with a prospective client shall be conducted by a representative that is either registered or qualifies for an exemption or exclusion from registration in the state where the prospective client resides. For information pertaining to the registration status of PFYG, please contact the state securities regulators for those states in which PFYG maintains a registration filing. A copy of PFYG's current written disclosure statement discussing PFYG's business operations, services, and fees is available at the SEC's investment adviser public information website – www.adviserinfo.sec.gov 320683 or from the Adviser upon written request, [FIRM EMAIL].

> Please remember that different types of investments involve varying degrees of risk, and there can be no assurance that the future performance of any specific investment or investment strategy (including those undertaken or recommended by the Adviser), will be profitable or equal any historical performance level(s).

> This website and information are provided for guidance and information purposes only. Investments involve risk and unless otherwise stated, are not guaranteed. Be sure to first consult with a qualified financial adviser and/or tax professional before implementing any strategy. This website and information are not intended to provide investment, tax, or legal advice.

> Insurance products and services are offered and sold through individually licensed and appointed insurance agents.

> Throughout this website we have provided links to various other websites. While PFYG believes this information to be current and valuable to its clients and is reasonably reliable and does not contain untrue statements of material facts, or misleading information. PFYG provides these links on a strictly informational basis only and cannot be held liable for the accuracy, time sensitive nature, or viability of any information shown on these sites. Some content may be dated. All such information is provided solely for convenience purposes only and all users thereof should be guided accordingly.

> The opinions expressed herein are those of the firm and are subject to change without notice. The opinions referenced are as of the date of publication and are subject to change due to changes in the market or economic conditions and may not necessarily come to pass. Any opinions, projections, or forward-looking statements expressed herein are solely those of the author, may differ from the views or opinions expressed by other areas of the firm, and are only for general informational purposes as of the date indicated.

> Copyright © 2026 Plan For Your Goals, LLC. All rights reserved.

## Step 6. Two more pages (not in the navigation)

Create both under "Not linked" so they exist but stay out of the header.

| Page | Web address | Content |
|---|---|---|
| Privacy Policy | `/privacy-policy` | Copy the body of `https://www.planforyourgoals.com/privacy-policy/` word for word, from the "Privacy Policy" heading through the last paragraph before the site footer. Keep "Last updated: March 30, 2022" and the PDF link (`https://planforyourgoals.link/Privacy`) |
| Terms | `/terms` | Copy the body of `https://www.planforyourgoals.com/terms/` word for word, from "Terms & Conditions" through the "Contact Us" details |

Do not edit either text during the build. Four things in them are out of date and are David's to decide (see "Open items" below).

## Step 7. Redirects

`redirects.txt` holds 73 lines, one for each old page and post, in Squarespace's URL-mapping format. **Do not load it during the build.** It only matters once planforyourgoals.com points at this site. Loading it is a launch-day step.

## Step 8. Check before handing back

- [ ] Site is still private and on the trial. Nothing was purchased. No domain was touched.
- [ ] The live SOEF site is unchanged.
- [ ] All six sections are present in order and match the mock-up at desktop and phone widths.
- [ ] Every link opens the right place: SOEF (four tagged links), client login (three), Form ADV (three), SEC lookup (two), LinkedIn, phone, email, Privacy Policy, Terms.
- [ ] Both disclosure blocks read exactly as in this sheet. The only open spot is `[FIRM EMAIL]`, or David has filled it.
- [ ] CEPA® shows the ® and appears only beside David's name.
- [ ] The words "free," "no obligation," "guarantee" and "fee-only" appear nowhere outside the approved disclosure text ("are not guaranteed" is part of it).
- [ ] No tracking code, pop-up or announcement bar came over from the SOEF copy.
- [ ] Screenshots taken of the finished page at desktop and phone widths, and the private preview address noted for David.

## Open items for David (not part of the build)

1. **Fill `[FIRM EMAIL]`** in the footer disclosure.
2. **Confirm the office address** matches Form ADV. The old site calls it "Branch Office."
3. **Confirm the brochure short link** serves the 11/5/2026 brochure and does not point at a file on the WordPress site.
4. **Check "How I'm paid"** sentence by sentence against Form ADV Part 2A.
5. **Privacy Policy and Terms carry stale details**, copied as they stand:
   - Both show the old phone number (850) 786-3400.
   - Terms says "Branch Office."
   - Terms describes the site as "a Business Site and a Blog Site" that offers "services around retirement planning." The new site is neither.
   - Your disclosure file says the Terms page matched the WARRANTIES block on 2026-09-28. The live Terms page today is a different, longer text dated June 14, 2021, and I did not find the WARRANTIES wording on it. Decide which text the new Terms page should carry.
6. **Sign and file the advertising review record** once the built page is final.
