import streamlit as st
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


st.title("AI Footwear Product Generator")

name = st.text_input("Product Name")
category = st.text_input("Category")
features = st.text_input("Features")

if st.button("Generate"):
    desc, bullets, seo = generate_product_content(name, category, features)

    st.subheader("Description")
    st.write(desc)

    st.subheader("Bullet Points")
    for b in bullets:
        st.write(f"- {b}")

    st.subheader("SEO Title")
    st.write(seo)
