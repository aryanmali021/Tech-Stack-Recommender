# Career Recommendation System

Internship Project 3 for DecodeLabs: a recommendation system that accepts user skills, compares them against job-role skill profiles, and recommends suitable careers.

## What It Does

- Accepts user skills such as `Python, ML, Cloud`.
- Compares those skills against career roles like Data Scientist, DevOps Engineer, Backend Developer, Cloud Architect, AI Engineer, and more.
- Displays ranked careers with match percentages.
- Shows matched skills and skills the user can improve for each career.
- Includes both a browser interface and a Python CLI.

## Example

Input:

```text
Python, ML, Cloud
```

Output:

```text
1. Data Scientist
2. Machine Learning Engineer
3. AI Engineer
```

## Run the Web App

Open this file in a browser:

```text
web/index.html
```

## Run the CLI

```powershell
.\.venv\Scripts\python.exe app.py
```

## Run Tests

```powershell
.\.venv\Scripts\python.exe -m unittest discover -v
```

## Matching Logic

The recommender normalizes the user's skills, expands common aliases such as `ML` to `machine learning`, and compares the result with weighted skill profiles for each job role. A role gets a higher score when it matches more of the user's entered skills and when the matched skills are important for that career.
