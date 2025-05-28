import random
from .models import Blog, Category, Tags, User 
from django.core.files import File


def create_dummy_blogs():
    titles = [
        "Exploring the Future of AI", "10 Tips for Better Productivity", "The Secret Behind Healthy Living",
        "Top 5 Travel Destinations in 2025", "Understanding Django Models", "How to Master Python in 3 Months",
        "What Makes a Great Leader?", "The Science of Sleep", "Minimalist Lifestyle: Pros and Cons",
        "Is Remote Work Here to Stay?", "The Rise of Electric Vehicles", "Benefits of Daily Meditation",
        "A Beginner’s Guide to Investing", "Digital Art in the NFT Era", "How to Create a Personal Brand",
        "Ultimate Guide to Budgeting", "Top Programming Languages in 2025", "Building Habits That Stick",
        "Photography Tips for Beginners", "Mental Health Matters", "Why You Should Read More Books",
        "Creating Content That Converts", "Fitness Myths Debunked", "Eco-Friendly Living on a Budget",
        "Learning a New Language Fast", "How to Start a Side Hustle", "What is Blockchain Technology?",
        "Mastering Time Management", "Breaking Down Crypto Basics", "Interior Design for Small Spaces"
    ]

    categories = list(Category.objects.all())
    tags = list(Tags.objects.all())
    users = list(User.objects.all())

    image_path = 'media/bs1.jpg'  # Replace with your real image path

    for i in range(30):
        title = titles[i]
        text = f"This is a detailed article about '{title}'. It contains valuable insights and practical tips."

        blog = Blog.objects.create(
            title=title,
            text=text,
            cotegory=random.choice(categories) if categories else None,
            status=random.choice([Blog.SatusEnum.PUBLISHED, Blog.SatusEnum.DRAFT])
        )

        with open(image_path, 'rb') as img_file:
            blog.image.save(f'image_{i}.jpg', File(img_file), save=True)

        # Randomly add likes and seen users
        if users:
            blog.like.set(random.sample(users, k=random.randint(0, len(users))))
            blog.seen.set(random.sample(users, k=random.randint(0, len(users))))

        # Randomly assign hashtags
        if tags:
            blog.hash_tag.set(random.sample(tags, k=random.randint(1, min(3, len(tags)))))

        print(f"Created blog: {blog.title}")
