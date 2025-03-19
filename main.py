from typing import List, Optional

import httpx
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


# Define our data models
@strawberry.type
class Book:
    id: int
    title: str
    author: str
    year: Optional[int] = None


# Sample data from Project Gutenberg API


async def fetch_gutenberg_books() -> List[Book]:
    url = "https://gutendex.com/books/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return [
            Book(
                id=idx + 1,
                title=book["title"],
                author=book["authors"][0]["name"] if book["authors"] else "Unknown",
                year=None,  # Gutenberg API doesn't provide publication year
            )
            for idx, book in enumerate(data["results"][:10])
        ]


# Define queries
@strawberry.type
class Query:
    @strawberry.field
    async def books(self) -> List[Book]:
        return await fetch_gutenberg_books()

    @strawberry.field
    async def book(self, id: int) -> Optional[Book]:
        books = await fetch_gutenberg_books()
        return next((book for book in books if book.id == id), None)


# Create GraphQL schema
schema = strawberry.Schema(query=Query)

# Create FastAPI app
app = FastAPI(title="FastAPI with Strawberry GraphQL")

# Add GraphQL route
graphql_app: GraphQLRouter = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to FastAPI with Strawberry GraphQL"}
