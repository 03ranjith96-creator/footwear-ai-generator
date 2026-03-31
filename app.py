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


# User input
name = input("Enter product name: ")
category = input("Enter category: ")
features = input("Enter features: ")

desc, bullets, seo = generate_product_content(name, category, features)

print("\nDescription:\n", desc)
print("\nBullet Points:")
for b in bullets:
    print("-", b)
print("\nSEO Title:\n", seo)
