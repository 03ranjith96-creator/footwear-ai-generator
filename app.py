import random

def generate_product_content(name, category, features):
    descriptions = [
        f"{name} is a premium {category} designed for comfort and everyday style, featuring {features}.",
        f"Experience superior comfort with {name}, a {category} built with {features}.",
        f"{name} {category} combines style and performance with {features}."
    ]

    description = random.choice(descriptions)

    bullets = [
        f"Premium {category} design",
        f"Enhanced comfort with {features}",
        "Durable and lightweight construction",
        "Ideal for daily wear"
    ]

    seo_title = f"{name} {category} – Comfortable & Stylish | Walkshark"

    return description, bullets, seo_title


print("\nGenerating product content...\n")

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
