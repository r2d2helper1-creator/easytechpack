# Cycle 1 Usability Report — Beginner (14-year-old) Perspective

**Tester:** A kid who has never used tech pack software before  
**Task:** Try to create a tech pack for a hoodie design  
**Date:** 2026-03-20

---

## 🔴 CRITICAL ISSUES

### 1. "Bill of Materials" — Nobody Knows What This Means
**Page:** Bill of Materials  
**Problem:** The term "Bill of Materials" is professional jargon. A 14-year-old has zero idea what this means. There's no tooltip, no help icon, no explanation. The subtitle says "All fabrics, trims, closures, labels, packaging" which helps a tiny bit but doesn't explain WHY you'd fill this in or what a "bill" even is in this context.  
**Expected:** Something like "Materials List" or "What You Need" with a one-line explanation like "List every material and supply needed to make this garment."

### 2. "SPI" Column is a Mystery
**Page:** Stitch Instructions  
**Problem:** The column header says "SPI" with no explanation. Nobody under 40 who isn't a seamstress knows what this means. There's a placeholder "12-14" but that doesn't explain the concept.  
**Expected:** At minimum a tooltip or header note: "SPI = Stitches Per Inch (how many stitches in one inch of seam)"

### 3. "Seam Allowance" is Confusing
**Page:** Stitch Instructions, Construction Details  
**Problem:** What is a seam allowance? The placeholder "1/2"" means nothing to a beginner. No explanation given.  
**Expected:** A small note like "The extra fabric beyond the stitch line" or a help icon.

### 4. "Tolerance" Column is Unexplained
**Page:** Measurement Specs, Proto Tracking  
**Problem:** Column says "Tolerance" with placeholder "+/- 0.5"". A kid won't know this means "how much the measurement can vary and still be OK."  
**Expected:** Header note: "Acceptable variation (e.g. +/- 0.5 inches)"

### 5. "Proto" / "Proto Tracking" — What?
**Page:** Proto Tracking  
**Problem:** The page is called "Proto Tracking" and mentions "P1 Actual", "P2 Actual", "PPS". None of this is explained. A kid thinks "proto" might be a type of protein or something. P1, P2, PPS — completely opaque.  
**Expected:** At least a subtitle explaining: "Track how sample garments match the original design specs. P1 = first sample, P2 = revised sample, PPS = pre-production sample."

### 6. "Grading Rules" — Double Page Confusion
**Pages:** Size Grading AND Grading Rules  
**Problem:** These two pages are confusingly similar. "Size Grading" has columns for XS/S/M/L/XL with actual measurements. "Grading Rules" has columns for XS→S, S→M, etc. The difference is NOT explained. A beginner has no idea why there are two pages for seemingly the same thing.  
**Expected:** Merge them, or clearly explain: "Size Grading = actual measurements per size. Grading Rules = how much each measurement changes between sizes."

### 7. "How to Measure" vs "Measurement Specs" — Also Confusing
**Pages:** How to Measure AND Measurement Specs  
**Problem:** Why are these two separate pages? They sound identical. "Measurement Specs" has Point of Measurement, Sample Size, Measurement, Tolerance, Unit. "How to Measure" has Measurement Point, Start Point, End Point, Method. A kid doesn't understand the difference.  
**Expected:** Combine them, or explain clearly: "Measurement Specs = the actual numbers. How to Measure = diagrams showing WHERE to measure."

---

## 🟡 MAJOR USABILITY ISSUES

### 8. No Welcome Screen or Onboarding
**Page:** Cover Page (landing page)  
**Problem:** When you first open the app, you land on "Cover Page" with zero context. There's no welcome message, no "Getting Started" guide, no "Here's what a tech pack is" explanation. A kid opens this and thinks: "What am I looking at? What do I do?"  
**Expected:** A welcome splash or inline guide: "Welcome! A tech pack is a document that tells a factory exactly how to make your clothing design. Start by filling in your brand name above, then work through each page in the sidebar."

### 9. 20 Pages in the Sidebar = Overwhelming
**Page:** Sidebar navigation  
**Problem:** The sidebar lists 20 different pages. That's overwhelming for anyone, let alone a kid. There's no indication of which ones to fill in first, which are optional, or which ones matter most for a hoodie.  
**Expected:** Group pages into categories (like "Design", "Materials", "Sizing", "Production") or mark pages as "Required" vs "Optional". Maybe a progress indicator showing which pages have data.

### 10. No Save Button — How Do I Save?
**Problem:** There's no visible "Save" button anywhere. The auto-save shows a tiny green "✓ Saved" text that flashes for 1.5 seconds in the top-right corner. A kid will have no idea their data is being saved. They'll close the browser tab and panic.  
**Expected:** A visible save button, or at least persistent text saying "Auto-saved" / "Last saved at 3:42 PM"

### 11. "New Tech Pack" Deletes Everything Without Enough Warning
**Page:** Sidebar footer  
**Problem:** The "New Tech Pack" button says "Start a new tech pack? All data will be cleared." This is just a browser `confirm()` dialog. It's easy to accidentally click "OK". A kid who spent 30 minutes filling stuff in could lose everything.  
**Expected:** A bigger warning, maybe a modal that makes you type "DELETE" or shows exactly how many rows/pages have data before clearing.

### 12. Column Names Are Professional Jargon Throughout
**Multiple Pages:**
- "Color/Pantone" — kids don't know what Pantone is
- "Supplier" — kids don't have suppliers  
- "Placement" — vague without context
- "Label Type" — what types exist?
- "Attachment" (on Labels page) — attachment of what?
- "Component" (on Cost Sheet) — too vague

**Expected:** Each column should have placeholder text showing examples, and jargon should have brief explanations.

### 13. "Flat Sketches" — What Is a Flat Sketch?
**Page:** Flat Sketches  
**Problem:** The title says "Flat Sketches" and subtitle says "Upload front, back, and detail views." A kid doesn't know what a "flat sketch" is. Is it a drawing? A photo? Do I draw it in this app or upload one?  
**Expected:** "Upload drawings of your hoodie from different angles. A flat sketch is a simple black-and-white drawing showing what the garment looks like laid flat."

### 14. "Colorways" — Not a Real Word to Kids
**Page:** Colorways  
**Problem:** "Colorways" is industry jargon. A kid would say "colors" or "color options." The Pantone Code column is also confusing — kids don't have Pantone books.  
**Expected:** Call it "Color Options" and make the Pantone field optional with a note like "If you have a Pantone color code, enter it here. Otherwise just use the color picker."

---

## 🟠 MODERATE ISSUES

### 15. No Image Upload Guidance on Sketch Pages
**Pages:** Flat Sketches, Detail Sketches  
**Problem:** The upload area just says "Click to upload." No guidance on what file types are accepted, what size limit there is, or what makes a good sketch image.  
**Expected:** "Click to upload (JPG, PNG — max 5MB). Draw your design on paper, take a photo, and upload it here."

### 16. Image Compression Happens Silently
**Problem:** Images get silently compressed to 400px max dimension. A kid uploads a nice high-res photo and it becomes tiny and blurry with no explanation.  
**Expected:** A message saying "Image resized for storage. For best quality, use images under 500KB."

### 17. "Fabric Placement" Table — "Location" Has Preset Options But No Guidance
**Page:** Fabric Placement  
**Problem:** The "Location" column is a dropdown with options like "Body", "Lining", "Pocket Lining", etc. These are fine but a kid won't know what "Body" vs "Lining" means in garment terms.  
**Expected:** Hover tooltips on dropdown options explaining each one.

### 18. "Construction Details" — "Seam Type" Options Need Explanation
**Page:** Construction Details  
**Problem:** Dropdown options include "Plain", "Felled", "Bound", "Overlocked", "French", "Welt", "Lapped". A 14-year-old knows maybe 1 of these. No explanations given.  
**Expected:** Each option should have a brief description, or the most common options should be marked as "common/beginner" options.

### 19. "Stitch Instructions" — Too Many Columns
**Page:** Stitch Instructions  
**Problem:** 6 columns: Area, Stitch Type, SPI, Seam Allowance, Seam Construction, Notes. This is overwhelming. Stitch Type dropdown has 10 options including "Bartack", "Blind Hem", "Coverstitch" — all mystery words.  
**Expected:** Fewer columns for beginners, or group related columns. Maybe collapse SPI and Seam Allowance under an "Advanced" section.

### 20. Cost Sheet Doesn't Auto-Calculate Properly
**Page:** Cost Sheet  
**Problem:** The Subtotal column auto-calculates (cost × qty) which is nice, but it only shows in the rendered table, not in the edit state. Also, if you type letters in the Cost field, the subtotal shows $0.00 with no warning.  
**Expected:** Validate that Cost and Qty are numbers. Show a red error if someone types "fifteen" instead of "15".

### 21. "Pattern Department Comments" / "Sewing / Construction Comments"
**Page:** Comments Log  
**Problem:** This page has TWO separate tables — one for "Pattern Department" and one for "Sewing / Construction." A kid doesn't know what a pattern department is. The two tables look almost identical. Why are they separate?  
**Expected:** Combine into one "Feedback & Notes" table, or explain the difference clearly.

### 22. No Example Data to Learn From
**Problem:** Every page starts completely empty. A beginner has no reference for what good data looks like. "What should I put in the Material field? What's a typical width?"  
**Expected:** Either pre-populate with example hoodie data, or have a "Load Example" button that fills in sample data for a hoodie so kids can see what it looks like.

### 23. "PPS" Abbreviation in Proto Tracking
**Page:** Proto Tracking  
**Problem:** PPS column with no explanation. Even if you explain "Proto" somehow, "PPS" (Pre-Production Sample) is another layer of jargon.  
**Expected:** Spell it out or use a tooltip.

### 24. Care Labels Page — "Symbol Type" is Vague
**Page:** Care Labels  
**Problem:** The dropdown says "Symbol Type" with options: Wash, Dry, Iron, Bleach, Dry Clean, Special Care. These are categories, not symbols. A kid might expect to see actual care symbols (the little icons on clothing tags).  
**Expected:** Rename to "Care Category" or show the actual care symbols alongside the text.

---

## 🔵 MINOR / POLISH ISSUES

### 25. Sidebar Icons Are Inconsistent
**Problem:** Some icons are emojis, some look like special characters. "📐" is used for BOTH "Detail Sketches" and "How to Measure" which is confusing. "📊" is used for both "Size Grading" and "Grading Rules."  
**Expected:** Unique icons for each page.

### 26. Page Numbers Show on Every Page but Aren't Real
**Problem:** Each page shows "Page X of 20" at the bottom, but these don't correspond to anything — they're just based on DOM order. In a printed tech pack, page numbers would matter. In this digital tool, they're just confusing.  
**Expected:** Remove or make them match the actual sidebar order.

### 27. "Confidential" Footer on Every Page
**Problem:** Every page ends with "CONFIDENTIAL PROPERTY OF YOUR BRAND. Unauthorized reproduction, disclosure or transmittal without written consent is strictly prohibited." This is legal boilerplate that a kid won't understand. It takes up space and adds visual noise.  
**Expected:** Make it optional or hide it by default with a toggle.

### 28. No Keyboard Shortcuts
**Problem:** No way to quickly navigate between pages with keyboard. Tab order through table cells is unpredictable.  
**Expected:** Arrow keys to navigate between sidebar items, or at least Ctrl+S to save.

### 29. "Add" Buttons Are Easy to Miss
**Problem:** The "+ Add Fabric", "+ Add Trim" etc. buttons are styled as dashed-border grey buttons at the bottom of each table. They're easy to overlook.  
**Expected:** Make them more prominent, or add a floating "+" button.

### 30. Delete Buttons Are Too Easy to Click
**Problem:** The × delete button on each row is small and right next to the input fields. No confirmation dialog. One accidental click and your row is gone.  
**Expected:** Add a confirmation: "Delete this row?" or an undo button that appears briefly.

### 31. No "Export to PDF" Success Feedback
**Problem:** After PDF export finishes, the loading overlay just disappears. No "Done! Your PDF has been downloaded" message.  
**Expected:** A brief success toast: "✅ PDF downloaded!"

### 32. Mobile Layout Collapses Sidebar But Table Experience Is Bad
**Problem:** On mobile (<768px), the sidebar becomes a hamburger menu, which is good. But the tables become very cramped with many columns. Horizontal scrolling on tables is not obvious.  
**Expected:** On mobile, show fewer columns or use a card layout for table rows.

### 33. No Data Validation Anywhere
**Problem:** You can type literally anything in any field. Numbers in text fields, text in number fields, emojis everywhere. No required fields. No format validation.  
**Expected:** At minimum, the date field should enforce date format. Cost fields should only accept numbers.

### 34. "Pack Date" Field — Why Is This Different from "Date"?
**Problem:** The top bar has a "Date" field. But what date? Today? The design date? The production date? A kid won't know what to put here.  
**Expected:** Label it "Design Date" or "Creation Date" with today's date auto-filled.

---

## 🔍 DATA PERSISTENCE CHECK

### 35. Data Saves to localStorage (Works, But...)
**Finding:** Data DOES auto-save to browser localStorage. Reloading the page preserves all entered data. Logo uploads are preserved as compressed data URLs.  
**Problem:** A kid doesn't know this. There's no mention of where data is saved. If they switch browsers or clear cookies, everything is gone. No cloud save, no export/import of the data file itself.  
**Expected:** At minimum, a "💾 Save Backup" button that downloads a JSON file, and a "📂 Load Backup" button to restore it. Also a note: "Your data is saved in this browser. If you clear your browser data, you'll lose it."

### 36. localStorage Has a Size Limit
**Problem:** Images are compressed to 400px, but localStorage typically has a 5-10MB limit. If a kid uploads many images, they'll hit the limit and get a raw "Storage full!" alert with no guidance on what to do.  
**Expected:** Better error message: "Storage is full! Try removing some images or using smaller photos."

---

## 📋 SUMMARY

| Category | Count |
|----------|-------|
| Critical (kid can't use the page) | 7 |
| Major (confusing/frustrating) | 8 |
| Minor (polish/UX) | 10 |
| Data/Save related | 2 |
| **Total issues** | **27** |

### Top 5 Things That Would Help a Beginner Most:

1. **Welcome/onboarding screen** explaining what a tech pack is and what to do first
2. **Plain language everywhere** — replace "Bill of Materials" with "Materials List", explain jargon with tooltips
3. **Example hoodie data** pre-loaded so kids can see what a completed tech pack looks like
4. **Group sidebar pages** into categories (Design, Materials, Sizing, Production) and mark required vs optional
5. **Add a "Save Backup" / "Load Backup" feature** so data isn't locked in one browser's localStorage
