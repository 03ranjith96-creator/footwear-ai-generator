def generate_product_content(name, category, features):
    description = f"{name} is a premium {category} designed for comfort and everyday style. It features {features}."

    bullets = [
        f"Premium {category} design",
        f"Enhanced comfort with {features}",
        "Durable and lightweight",
        "Perfect for daily wear"
    ]

    seo_title = f"{name} {category} – Comfortable & Stylish | Walkshark"

    return description, bullets, seo_title


# Example products
products = [
    ("Wave Luxe", "Slides", "soft EVA sole and anti-slip grip"),
    ("Surf Line", "Sandals", "water-resistant upper and cushioned footbed"),
    ("Breezy Toe", "Flip Flops", "lightweight sole and flexible straps")
]

for name, category, features in products:
    desc, bullets, seo = generate_product_content(name, category, features)

    print("\n--- PRODUCT ---")
    print("Name:", name)
    print("Description:", desc)
    print("SEO Title:", seo)
    print("Bullets:")
    for b in bullets:
        print("-", b)
