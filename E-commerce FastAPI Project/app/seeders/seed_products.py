from sqlalchemy.orm import Session
from app.Product.models import Product
from app.db.database import sessionLocal
from app.User.models import User  

# Sample product data (without created_by)
products_data = [
    {
        "name": "Wireless Mouse",
        "description": "Ergonomic wireless mouse with adjustable DPI",
        "price": 25.99,
        "stock": 100,
        "category": "Electronics",
        "image_url": "https://example.com/images/wireless_mouse.jpg"
    },
    {
        "name": "Mechanical Keyboard",
        "description": "RGB backlit mechanical keyboard with blue switches",
        "price": 79.99,
        "stock": 50,
        "category": "Electronics",
        "image_url": "https://example.com/images/mechanical_keyboard.jpg"
    },
    {
        "name": "Running Shoes",
        "description": "Comfortable running shoes for men and women",
        "price": 59.99,
        "stock": 200,
        "category": "Footwear",
        "image_url": "https://example.com/images/running_shoes.jpg"
    },
    {
        "name": "Water Bottle",
        "description": "Insulated stainless steel water bottle (1L)",
        "price": 19.99,
        "stock": 150,
        "category": "Accessories",
        "image_url": "https://example.com/images/water_bottle.jpg"
    },
]

def seed_products():
    db: Session = sessionLocal()
    try:
        # Get the first admin user
        admin = db.query(User).filter(User.role == "admin").first()
        if not admin:
            print("❌ No admin found. Please create an admin user before seeding products.")
            return

        for data in products_data:
            # Add created_by field to each product
            data_with_admin = data.copy()
            data_with_admin["created_by"] = admin.id

            # Check if product already exists to avoid duplicates
            existing = db.query(Product).filter_by(name=data["name"]).first()
            if not existing:
                product = Product(**data_with_admin)
                db.add(product)
        db.commit()
        print("✅ Products seeded successfully.")
    except Exception as e:
        db.rollback()
        print("❌ Error seeding products:", e)
    finally:
        db.close()

if __name__ == "__main__":
    seed_products()