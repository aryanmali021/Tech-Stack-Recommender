from __future__ import annotations

from recommender import recommend, unique_options


def choose_option(label: str, options: list[str]) -> str:
    print(f"\n{label}")
    for index, option in enumerate(options, start=1):
        print(f"  {index}. {option}")

    while True:
        selected = input("Choose a number: ").strip()
        if selected.isdigit() and 1 <= int(selected) <= len(options):
            return options[int(selected) - 1]
        print("Please enter a valid option number.")


def main() -> None:
    print("Career Recommendation System")
    print("Enter skills such as: Python, ML, Cloud, Docker, SQL, React")

    skills = input("\nYour skills, separated by commas: ").strip()
    domain = choose_option("Preferred career domain", unique_options("domain"))
    level = choose_option("Preferred experience level", unique_options("level"))
    work_style = choose_option("Preferred work style", unique_options("work_style"))

    recommendations = recommend(
        skills,
        preferred_domain=domain,
        preferred_level=level,
        preferred_work_style=work_style,
    )

    print("\nRecommended careers")
    print("-" * 72)
    if not recommendations:
        print("No matches found. Try skills such as Python, ML, Cloud, Docker, SQL, or React.")
        return

    for rank, role in enumerate(recommendations, start=1):
        matched = ", ".join(role["matched_skills"]) or "no direct skill match"
        missing = ", ".join(role["missing_skills"]) or "none"
        print(f"{rank}. {role['title']} ({role['score']}%)")
        print(f"   {role['domain']} | {role['level']} | {role['work_style']}")
        print(f"   Matched skills: {matched}")
        print(f"   Skills to improve: {missing}")
        print(f"   {role['description']}\n")


if __name__ == "__main__":
    main()
