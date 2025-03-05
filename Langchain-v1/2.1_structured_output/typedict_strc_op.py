from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


model = ChatOpenAI(model="gpt-4o")


# * Example 1: Define a TypedDict for a product review
class ReviewDict(TypedDict):
    """TypedDict for a product review."""

    product_name: str
    review: str
    rating: int


review_dict: ReviewDict = {
    "product_name": "Apple Watch",
    "review": "I love my Apple Watch! It's so easy to use and has so many great features. The fitness tracking is really helpful and the notifications are super convenient.",
    "rating": 5,
}

result = model.invoke(
    f"Please write a review of a product based on the following input: {review_dict}"
)
print(result.content)


# * Example 2: Define a TypedDict for a product review
class Review(TypedDict):
    summary: str
    sentiment: str


structure_model = model.with_structured_output(Review)

result = structure_model.invoke(
    """ The Hardware is great, but the software is a bit slow.  There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update soon. """
)
print(result)
print(result["summary"])
print(result["sentiment"])


# * Example 3: Define a TypedDict using Annotated


class ReviewAnnotated(TypedDict):
    key_themes: Annotated[list[str], "Write a list of key themes from the review."]
    summary: Annotated[str, "Write a summary of the review."]
    sentiment: Annotated[
        str, "Classify the sentiment of the review as positive, negative, or neutral."
    ]
    pros: Annotated[list[str], "Write a list of pros of the product."]
    cons: Annotated[list[str], "Write a list of cons of the product."]
    name: Annotated[str, "Write the name of the product"]


structure_model = model.with_structured_output(ReviewAnnotated)

result = structure_model.invoke(
    """ The Hardware is great Iphone 16, but the software is a bit slow.  There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update soon. """
)
print(result)
print(result["summary"])
print(result["sentiment"])
print(result["key_themes"])
print(result["pros"])
print(result["cons"])
print(result["name"])
