
import os
from google import genai

MODEL = "gemini-3.8-flash"

def generate_content(topic, content_type, genre, tone):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY")
    )

    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: Please set your GEMINI_API_KEY first.")
        return None

    prompt = f"""
    You are a creative content writer.

    Topic or keywords: {topic}
    Content type: {content_type}
    Genre: {genre}
    Tone: {tone}

    Instructions:
    - Create original, engaging content based on the topic.
    - Match the selected content type, genre, and tone.
    - Give the content a suitable title.
    - For a short story, include a beginning, middle, and ending.
    - For a blog post, use clear paragraphs.
    - For a poem, use creative lines and imagery.
    - Avoid unnecessary explanations.
    """

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text
    except Exception as error:
        print(f"\nGeneration failed: {error}")
        return None


def main():
    print("\n===================================")
    print("     AI STORY / CONTENT GENERATOR")
    print("===================================")

    while True:
        topic = input("\nEnter a topic or keywords: ").strip()

        if not topic:
            print("Please enter a topic.")
            continue

        print("\nChoose content type:")
        print("1. Short Story")
        print("2. Blog Post")
        print("3. Poem")

        type_choice = input("Enter choice (1-3): ").strip()
        content_types = {
            "1": "Short Story",
            "2": "Blog Post",
            "3": "Poem"
        }

        if type_choice not in content_types:
            print("Invalid choice. Try again.")
            continue

        content_type = content_types[type_choice]

        genre = input(
            "Choose a genre (e.g. Fantasy, Mystery, Romance, Adventure): "
        ).strip() or "General"

        tone = input(
            "Choose a tone (e.g. Funny, Inspirational, Formal, Emotional): "
        ).strip() or "Engaging"

        while True:
            print("\nGenerating your content...")
            result = generate_content(
                topic, content_type, genre, tone
            )

            if result:
                print("\n========== GENERATED CONTENT ==========\n")
                print(result)

                save = input("\nSave this output? (y/n): ").strip().lower()
                if save == "y":
                    with open("generated_content.txt", "a", encoding="utf-8") as file:
                        file.write(f"\n\nType: {content_type}\n")
                        file.write(f"Topic: {topic}\n")
                        file.write(f"Genre: {genre} | Tone: {tone}\n\n")
                        file.write(result)
                        file.write("\n" + "=" * 50 + "\n")
                    print("Content saved to generated_content.txt")

            again = input(
                "\nGenerate another version with the same settings? (y/n): "
            ).strip().lower()

            if again != "y":
                break

        continue_choice = input(
            "\nCreate content on a new topic? (y/n): "
        ).strip().lower()

        if continue_choice != "y":
            print("\nThank you for using AI Content Generator!")
            break


if __name__ == "__main__":
    main()
