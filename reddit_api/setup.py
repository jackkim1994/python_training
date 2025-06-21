from setuptools import setup, find_packages

setup(
    name="reddytics",
    version="0.1.0",
    description="A Reddit analytics SDK",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(include=["reddytics", "reddytics.*"]),
    install_requires=[
        "praw",
        "python-dotenv",
    ],
    python_requires='>=3.7',
)
