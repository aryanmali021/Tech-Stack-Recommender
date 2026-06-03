from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CareerRole:
    title: str
    domain: str
    level: str
    work_style: str
    description: str
    skills: tuple[tuple[str, int], ...]


CAREER_ROLES: tuple[CareerRole, ...] = (
    CareerRole(
        title="Data Scientist",
        domain="Data and AI",
        level="Intermediate",
        work_style="Analysis",
        description="Uses statistics, Python, SQL, and machine learning to find patterns and build data-driven solutions.",
        skills=(
            ("python", 5),
            ("machine learning", 5),
            ("statistics", 5),
            ("data analysis", 5),
            ("sql", 4),
            ("pandas", 4),
            ("numpy", 3),
            ("data visualization", 3),
            ("cloud", 4),
            ("experimentation", 2),
        ),
    ),
    CareerRole(
        title="Machine Learning Engineer",
        domain="Data and AI",
        level="Advanced",
        work_style="Engineering",
        description="Builds, deploys, and monitors machine learning models in production systems.",
        skills=(
            ("python", 5),
            ("machine learning", 5),
            ("deep learning", 4),
            ("mlops", 5),
            ("model deployment", 4),
            ("docker", 4),
            ("cloud", 3),
            ("tensorflow", 3),
            ("pytorch", 3),
            ("data pipelines", 3),
        ),
    ),
    CareerRole(
        title="AI Engineer",
        domain="Data and AI",
        level="Advanced",
        work_style="Engineering",
        description="Creates AI-powered products using ML models, LLMs, APIs, prompt design, and deployment workflows.",
        skills=(
            ("python", 5),
            ("machine learning", 5),
            ("deep learning", 4),
            ("generative ai", 5),
            ("llm", 5),
            ("nlp", 4),
            ("cloud", 2),
            ("api", 3),
            ("prompt engineering", 3),
            ("model deployment", 3),
        ),
    ),
    CareerRole(
        title="DevOps Engineer",
        domain="Cloud and Infrastructure",
        level="Intermediate",
        work_style="Operations",
        description="Automates software delivery, manages infrastructure, and keeps applications reliable in production.",
        skills=(
            ("linux", 5),
            ("docker", 5),
            ("kubernetes", 5),
            ("ci/cd", 5),
            ("cloud", 4),
            ("aws", 4),
            ("terraform", 4),
            ("monitoring", 3),
            ("git", 3),
            ("scripting", 3),
        ),
    ),
    CareerRole(
        title="Cloud Architect",
        domain="Cloud and Infrastructure",
        level="Advanced",
        work_style="Architecture",
        description="Designs scalable cloud systems using networking, security, automation, and service architecture.",
        skills=(
            ("cloud", 5),
            ("aws", 5),
            ("azure", 4),
            ("gcp", 4),
            ("networking", 5),
            ("security", 4),
            ("kubernetes", 4),
            ("terraform", 4),
            ("system design", 4),
            ("devops", 3),
        ),
    ),
    CareerRole(
        title="Backend Developer",
        domain="Software Development",
        level="Intermediate",
        work_style="Engineering",
        description="Builds APIs, databases, server-side features, and application logic for software products.",
        skills=(
            ("python", 5),
            ("java", 4),
            ("node.js", 4),
            ("api", 5),
            ("sql", 4),
            ("databases", 4),
            ("django", 3),
            ("flask", 3),
            ("microservices", 3),
            ("docker", 3),
        ),
    ),
    CareerRole(
        title="Frontend Developer",
        domain="Software Development",
        level="Beginner",
        work_style="Product",
        description="Creates user interfaces with HTML, CSS, JavaScript, component frameworks, and accessibility practices.",
        skills=(
            ("html", 5),
            ("css", 5),
            ("javascript", 5),
            ("react", 5),
            ("ui", 4),
            ("responsive design", 4),
            ("typescript", 3),
            ("accessibility", 3),
            ("api", 2),
            ("git", 2),
        ),
    ),
    CareerRole(
        title="Full Stack Developer",
        domain="Software Development",
        level="Intermediate",
        work_style="Product",
        description="Works across frontend, backend, APIs, databases, deployment, and product features.",
        skills=(
            ("javascript", 5),
            ("react", 4),
            ("node.js", 4),
            ("python", 3),
            ("api", 4),
            ("databases", 4),
            ("sql", 3),
            ("html", 3),
            ("css", 3),
            ("cloud", 2),
        ),
    ),
    CareerRole(
        title="Data Analyst",
        domain="Data and AI",
        level="Beginner",
        work_style="Analysis",
        description="Analyzes business data, creates dashboards, and explains insights using SQL and visualization tools.",
        skills=(
            ("sql", 5),
            ("excel", 5),
            ("data analysis", 5),
            ("power bi", 4),
            ("tableau", 4),
            ("statistics", 3),
            ("python", 3),
            ("data visualization", 4),
            ("business intelligence", 4),
            ("communication", 3),
        ),
    ),
    CareerRole(
        title="Cybersecurity Analyst",
        domain="Security",
        level="Intermediate",
        work_style="Operations",
        description="Protects systems by monitoring threats, analyzing incidents, and applying security controls.",
        skills=(
            ("security", 5),
            ("networking", 5),
            ("linux", 4),
            ("incident response", 5),
            ("siem", 4),
            ("risk analysis", 4),
            ("cloud", 3),
            ("python", 2),
            ("scripting", 3),
            ("compliance", 3),
        ),
    ),
)


SKILL_ALIASES: dict[str, tuple[str, ...]] = {
    "ml": ("machine learning",),
    "ai": ("artificial intelligence", "generative ai"),
    "gen ai": ("generative ai",),
    "llms": ("llm",),
    "nlp": ("natural language processing",),
    "aws cloud": ("aws", "cloud"),
    "amazon web services": ("aws", "cloud"),
    "azure cloud": ("azure", "cloud"),
    "google cloud": ("gcp", "cloud"),
    "gcp cloud": ("gcp", "cloud"),
    "k8s": ("kubernetes",),
    "cicd": ("ci/cd",),
    "ci cd": ("ci/cd",),
    "rest api": ("api",),
    "apis": ("api",),
    "database": ("databases",),
    "db": ("databases",),
    "js": ("javascript",),
    "ts": ("typescript",),
    "powerbi": ("power bi",),
}


def normalize_skill(value: str) -> str:
    normalized = " ".join(value.strip().lower().split())
    return normalized.replace("machine-learning", "machine learning")


def career_skill_names() -> set[str]:
    return {normalize_skill(skill) for role in CAREER_ROLES for skill, _weight in role.skills}


def tokenize_preferences(raw_skills: str | Iterable[str]) -> set[str]:
    if isinstance(raw_skills, str):
        parts = raw_skills.replace(";", ",").split(",")
    else:
        parts = raw_skills

    skills: set[str] = set()
    for part in parts:
        skill = normalize_skill(part)
        if not skill:
            continue
        skills.add(skill)
        skills.update(SKILL_ALIASES.get(skill, ()))
    return skills


def similarity_score(
    user_skills: set[str],
    role: CareerRole,
    *,
    preferred_domain: str = "Any",
    preferred_level: str = "Any",
    preferred_work_style: str = "Any",
) -> tuple[float, tuple[str, ...], tuple[str, ...]]:
    role_skill_weights = {normalize_skill(skill): weight for skill, weight in role.skills}
    matched_skills = sorted(user_skills & set(role_skill_weights))

    if not user_skills:
        return 0.0, (), tuple(role_skill_weights)[:4]

    matched_weight = sum(role_skill_weights[skill] for skill in matched_skills)
    role_weight_total = sum(role_skill_weights.values()) or 1
    known_user_skills = user_skills & career_skill_names()
    scoring_user_skills = known_user_skills or user_skills
    user_coverage = len(matched_skills) / len(scoring_user_skills)
    role_coverage = matched_weight / role_weight_total

    score = (user_coverage * 88) + (role_coverage * 12)
    if preferred_domain not in ("Any", role.domain):
        score -= 8
    if preferred_level not in ("Any", role.level):
        score -= 4
    if preferred_work_style not in ("Any", role.work_style):
        score -= 4

    missing_skills = tuple(
        skill for skill, _weight in sorted(role.skills, key=lambda item: item[1], reverse=True)
        if normalize_skill(skill) not in user_skills
    )
    return max(round(min(score, 100.0), 1), 0.0), tuple(matched_skills), missing_skills[:4]


def recommend(
    skills: str | Iterable[str],
    *,
    preferred_domain: str = "Any",
    preferred_level: str = "Any",
    preferred_work_style: str = "Any",
    limit: int = 5,
) -> list[dict[str, object]]:
    user_skills = tokenize_preferences(skills)
    results: list[dict[str, object]] = []

    for role in CAREER_ROLES:
        score, matched_skills, missing_skills = similarity_score(
            user_skills,
            role,
            preferred_domain=preferred_domain,
            preferred_level=preferred_level,
            preferred_work_style=preferred_work_style,
        )
        if score > 0:
            results.append(
                {
                    "title": role.title,
                    "domain": role.domain,
                    "level": role.level,
                    "work_style": role.work_style,
                    "description": role.description,
                    "skills": tuple(skill for skill, _weight in role.skills),
                    "matched_skills": matched_skills,
                    "missing_skills": missing_skills,
                    "score": score,
                }
            )

    return sorted(
        results,
        key=lambda row: (float(row["score"]), len(row["matched_skills"])),
        reverse=True,
    )[:limit]


def unique_options(attribute: str) -> list[str]:
    values = sorted({getattr(role, attribute) for role in CAREER_ROLES})
    return ["Any", *values]
