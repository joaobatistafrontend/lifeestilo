# Aura Luxury Aesthetics - Design System Style Guidelines

Este documento contém as diretrizes de estilo do Design System **Aura Luxury Aesthetics**.

## Brand & Style

This design system is crafted for a high-end facial harmonization clinic, embodying sophistication, clinical precision, and timeless beauty. The brand personality is poised, expert, and serene, targeting a discerning clientele that values subtle, natural enhancements and a premium experience.

The visual direction follows a **Modern Minimalist** aesthetic with a **Tactile** edge. It utilizes generous whitespace to evoke a sense of calm and hygiene, paired with high-end editorial layouts. The interface should feel like a digital extension of a physical luxury spa—quiet, intentional, and impeccably organized. We avoid unnecessary decorative elements, allowing the refined typography and photography of the human form to provide the visual narrative.

## Colors

The color palette is anchored in the clinic's heritage colors but elevated for a more editorial feel. 

- **Primary (#C4907E):** A refined rose-gold/terracotta tone used for accents, primary actions, and brand markers. It represents skin health and warmth.
- **Secondary (#FDF5F2):** Our "Champagne" base. This serves as the primary background color for most surfaces to avoid the clinical coldness of pure white.
- **Tertiary (#2D2926):** A deep, warm charcoal used for headings to provide high contrast without the harshness of pure black.
- **Neutral:** A range of soft grays derived from the primary hue to handle borders and secondary text.

Functional states (success, error) should be muted to match the palette—avoid vibrant neon colors. Use soft sage for success and a desaturated clay for errors.

## Typography

The typography strategy relies on a "High-Low" pairing. **Libre Caslon Text** provides an authoritative, literary elegance for headlines, suggesting a history of expertise. **Manrope** offers a clean, modern, and highly legible counterpoint for body copy and UI elements.

- **Headlines:** Always use Libre Caslon Text. For large display moments, use slight negative letter spacing to create a tighter, more "fashion-magazine" look.
- **Body:** Manrope should be set with generous line height (minimum 1.5x) to maintain the airy, spacious feel of the brand.
- **Labels:** Small labels and overlines should use Manrope in Uppercase with increased letter spacing to denote secondary hierarchy and categorization.

## Layout & Spacing

This design system employs a **Fixed Grid** for desktop to maintain a premium, controlled composition, and a **Fluid Grid** for mobile devices.

- **The 8px Rhythm:** All spacing (padding, margins, gaps) must be a multiple of 8px to ensure mathematical harmony.
- **Section Breathing Room:** We use aggressive vertical spacing (`section-gap`) between major content blocks. This "luxury of space" communicates that the brand is not rushed and values the client's peace.
- **Alignment:** Headlines should often be center-aligned in promotional sections but left-aligned for informational/service pages to maintain readability.

## Elevation & Depth

To maintain a sophisticated aesthetic, we avoid heavy, dark shadows. Depth is communicated through:

- **Tonal Layering:** Surfaces are differentiated by slight shifts in lightness (e.g., a `subtle-blush` card on a `secondary` background) rather than shadows.
- **Ambient Glows:** Where depth is required (such as modals or primary buttons), use extremely soft, diffused shadows tinted with the primary color (`#C4907E` at 10% opacity). The blur radius should be large (20px+) to create a "lift" rather than a "drop."
- **Glassmorphism:** For navigation bars and floating action overlays, use a backdrop blur (12px) with a semi-transparent `secondary` color fill. This maintains the "airy" feel while ensuring text legibility over photography.

## Shapes

The shape language is **Soft and Architectural**. While the clinic is a place of comfort, it is also a place of medical precision. 

- **Primary Elements:** Buttons and cards use a "Soft" (4px) corner radius. This provides a hint of approachable warmth without losing the professional structure of a clinical environment.
- **Media:** Photography of faces and procedures should occasionally use "Pill-shaped" or large "Rounded" containers to contrast against the structured grid, mimicking the organic curves of the human body.
- **Iconography:** Use light-stroke (1.5pt) icons with rounded caps and joins to match the soft-minimalist theme.

## Components

- **Buttons:**
  - *Primary:* Solid `primary_color`, white text, Manrope Bold, uppercase. No heavy shadows.
  - *Secondary:* Ghost style with a 1px border of `primary_color`.
- **Input Fields:** Minimalist design with only a bottom border (1px) in a neutral tone. The label floats above in `label-caps` when the field is active.
- **Cards:** Use `subtle-blush` backgrounds with no borders. Internal padding should be generous (32px) to prevent content from feeling cramped.
- **Chips/Tags:** Used for service categories (e.g., "Botox", "Fillers"). These should be pill-shaped with a very light `primary` tint and `body-sm` text.
- **Service Lists:** Use large, serif headlines for service names with a subtle 1px divider between items. On hover, the primary color should bleed in softly or an image thumbnail should appear.
- **Booking Widget:** This is a critical component. It should be treated as a "High-Elevation" element with a backdrop blur, making it appear as though it is floating gently over the content.
