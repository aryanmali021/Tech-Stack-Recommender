import unittest

from recommender import recommend, tokenize_preferences


class CareerRecommendationTests(unittest.TestCase):
    def test_tokenizes_skills_and_aliases(self) -> None:
        self.assertEqual(
            tokenize_preferences(" Python, ML; AWS Cloud "),
            {"python", "ml", "machine learning", "aws cloud", "aws", "cloud"},
        )

    def test_python_ml_cloud_recommends_ai_data_roles(self) -> None:
        results = recommend("Python, ML, Cloud", limit=3)
        titles = [item["title"] for item in results]

        self.assertEqual(titles[0], "Data Scientist")
        self.assertIn("Machine Learning Engineer", titles)
        self.assertIn("AI Engineer", titles)
        self.assertGreaterEqual(results[0]["score"], 80)

    def test_devops_skills_recommend_infrastructure_roles(self) -> None:
        results = recommend("Cloud, Docker, Kubernetes, Linux, CI/CD", limit=3)
        titles = [item["title"] for item in results]

        self.assertEqual(titles[0], "DevOps Engineer")
        self.assertIn("Cloud Architect", titles)

    def test_backend_skills_recommend_backend_developer(self) -> None:
        results = recommend("Python, API, SQL, databases, Django", limit=3)

        self.assertEqual(results[0]["title"], "Backend Developer")
        self.assertIn("api", results[0]["matched_skills"])


if __name__ == "__main__":
    unittest.main()
