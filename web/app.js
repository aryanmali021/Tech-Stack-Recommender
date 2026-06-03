const careerRoles = [
  {
    title: "Data Scientist",
    domain: "Data and AI",
    level: "Intermediate",
    workStyle: "Analysis",
    description: "Uses statistics, Python, SQL, and machine learning to find patterns and build data-driven solutions.",
    skills: [["python", 5], ["machine learning", 5], ["statistics", 5], ["data analysis", 5], ["sql", 4], ["pandas", 4], ["numpy", 3], ["data visualization", 3], ["cloud", 4], ["experimentation", 2]]
  },
  {
    title: "Machine Learning Engineer",
    domain: "Data and AI",
    level: "Advanced",
    workStyle: "Engineering",
    description: "Builds, deploys, and monitors machine learning models in production systems.",
    skills: [["python", 5], ["machine learning", 5], ["deep learning", 4], ["mlops", 5], ["model deployment", 4], ["docker", 4], ["cloud", 3], ["tensorflow", 3], ["pytorch", 3], ["data pipelines", 3]]
  },
  {
    title: "AI Engineer",
    domain: "Data and AI",
    level: "Advanced",
    workStyle: "Engineering",
    description: "Creates AI-powered products using ML models, LLMs, APIs, prompt design, and deployment workflows.",
    skills: [["python", 5], ["machine learning", 5], ["deep learning", 4], ["generative ai", 5], ["llm", 5], ["nlp", 4], ["cloud", 2], ["api", 3], ["prompt engineering", 3], ["model deployment", 3]]
  },
  {
    title: "DevOps Engineer",
    domain: "Cloud and Infrastructure",
    level: "Intermediate",
    workStyle: "Operations",
    description: "Automates software delivery, manages infrastructure, and keeps applications reliable in production.",
    skills: [["linux", 5], ["docker", 5], ["kubernetes", 5], ["ci/cd", 5], ["cloud", 4], ["aws", 4], ["terraform", 4], ["monitoring", 3], ["git", 3], ["scripting", 3]]
  },
  {
    title: "Cloud Architect",
    domain: "Cloud and Infrastructure",
    level: "Advanced",
    workStyle: "Architecture",
    description: "Designs scalable cloud systems using networking, security, automation, and service architecture.",
    skills: [["cloud", 5], ["aws", 5], ["azure", 4], ["gcp", 4], ["networking", 5], ["security", 4], ["kubernetes", 4], ["terraform", 4], ["system design", 4], ["devops", 3]]
  },
  {
    title: "Backend Developer",
    domain: "Software Development",
    level: "Intermediate",
    workStyle: "Engineering",
    description: "Builds APIs, databases, server-side features, and application logic for software products.",
    skills: [["python", 5], ["java", 4], ["node.js", 4], ["api", 5], ["sql", 4], ["databases", 4], ["django", 3], ["flask", 3], ["microservices", 3], ["docker", 3]]
  },
  {
    title: "Frontend Developer",
    domain: "Software Development",
    level: "Beginner",
    workStyle: "Product",
    description: "Creates user interfaces with HTML, CSS, JavaScript, component frameworks, and accessibility practices.",
    skills: [["html", 5], ["css", 5], ["javascript", 5], ["react", 5], ["ui", 4], ["responsive design", 4], ["typescript", 3], ["accessibility", 3], ["api", 2], ["git", 2]]
  },
  {
    title: "Full Stack Developer",
    domain: "Software Development",
    level: "Intermediate",
    workStyle: "Product",
    description: "Works across frontend, backend, APIs, databases, deployment, and product features.",
    skills: [["javascript", 5], ["react", 4], ["node.js", 4], ["python", 3], ["api", 4], ["databases", 4], ["sql", 3], ["html", 3], ["css", 3], ["cloud", 2]]
  },
  {
    title: "Data Analyst",
    domain: "Data and AI",
    level: "Beginner",
    workStyle: "Analysis",
    description: "Analyzes business data, creates dashboards, and explains insights using SQL and visualization tools.",
    skills: [["sql", 5], ["excel", 5], ["data analysis", 5], ["power bi", 4], ["tableau", 4], ["statistics", 3], ["python", 3], ["data visualization", 4], ["business intelligence", 4], ["communication", 3]]
  },
  {
    title: "Cybersecurity Analyst",
    domain: "Security",
    level: "Intermediate",
    workStyle: "Operations",
    description: "Protects systems by monitoring threats, analyzing incidents, and applying security controls.",
    skills: [["security", 5], ["networking", 5], ["linux", 4], ["incident response", 5], ["siem", 4], ["risk analysis", 4], ["cloud", 3], ["python", 2], ["scripting", 3], ["compliance", 3]]
  }
];

const skillAliases = {
  ml: ["machine learning"],
  ai: ["artificial intelligence", "generative ai"],
  "gen ai": ["generative ai"],
  llms: ["llm"],
  nlp: ["natural language processing"],
  "aws cloud": ["aws", "cloud"],
  "amazon web services": ["aws", "cloud"],
  "azure cloud": ["azure", "cloud"],
  "google cloud": ["gcp", "cloud"],
  "gcp cloud": ["gcp", "cloud"],
  k8s: ["kubernetes"],
  cicd: ["ci/cd"],
  "ci cd": ["ci/cd"],
  "rest api": ["api"],
  apis: ["api"],
  database: ["databases"],
  db: ["databases"],
  js: ["javascript"],
  ts: ["typescript"],
  powerbi: ["power bi"]
};

const form = document.querySelector("#preference-form");
const resultsNode = document.querySelector("#results");
const scoreNote = document.querySelector("#score-note");
const resetButton = document.querySelector("#reset-button");

const fields = {
  skills: document.querySelector("#skills"),
  domain: document.querySelector("#domain"),
  level: document.querySelector("#level"),
  workStyle: document.querySelector("#work-style")
};

function normalizeSkill(value) {
  return value.trim().toLowerCase().replace(/\s+/g, " ").replace("machine-learning", "machine learning");
}

function careerSkillNames() {
  return new Set(careerRoles.flatMap((role) => role.skills.map(([skill]) => normalizeSkill(skill))));
}

function tokenizeSkills(raw) {
  const skills = new Set();
  raw
    .replaceAll(";", ",")
    .split(",")
    .map(normalizeSkill)
    .filter(Boolean)
    .forEach((skill) => {
      skills.add(skill);
      (skillAliases[skill] || []).forEach((alias) => skills.add(alias));
    });
  return skills;
}

function populateSelect(node, values) {
  node.innerHTML = "";
  ["Any", ...values].forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    node.appendChild(option);
  });
}

function uniqueValues(key) {
  return [...new Set(careerRoles.map((role) => role[key]))].sort();
}

function similarityScore(userSkills, role, filters) {
  const roleSkillWeights = new Map(role.skills.map(([skill, weight]) => [normalizeSkill(skill), weight]));
  const matchedSkills = [...userSkills].filter((skill) => roleSkillWeights.has(skill)).sort();

  if (!userSkills.size) {
    return { score: 0, matchedSkills: [], missingSkills: role.skills.slice(0, 4).map(([skill]) => skill) };
  }

  const matchedWeight = matchedSkills.reduce((sum, skill) => sum + roleSkillWeights.get(skill), 0);
  const totalWeight = role.skills.reduce((sum, [, weight]) => sum + weight, 0);
  const knownUserSkills = [...userSkills].filter((skill) => careerSkillNames().has(skill));
  const scoringSkillCount = knownUserSkills.length || userSkills.size;
  const userCoverage = matchedSkills.length / scoringSkillCount;
  const roleCoverage = matchedWeight / totalWeight;

  let score = userCoverage * 88 + roleCoverage * 12;
  if (filters.domain !== "Any" && filters.domain !== role.domain) score -= 8;
  if (filters.level !== "Any" && filters.level !== role.level) score -= 4;
  if (filters.workStyle !== "Any" && filters.workStyle !== role.workStyle) score -= 4;

  const missingSkills = role.skills
    .filter(([skill]) => !userSkills.has(normalizeSkill(skill)))
    .sort((a, b) => b[1] - a[1])
    .slice(0, 4)
    .map(([skill]) => skill);

  return {
    score: Number(Math.max(Math.min(score, 100), 0).toFixed(1)),
    matchedSkills,
    missingSkills
  };
}

function recommend() {
  const userSkills = tokenizeSkills(fields.skills.value);
  const filters = {
    domain: fields.domain.value,
    level: fields.level.value,
    workStyle: fields.workStyle.value
  };

  return careerRoles
    .map((role) => ({ ...role, ...similarityScore(userSkills, role, filters) }))
    .filter((role) => role.score > 0)
    .sort((a, b) => b.score - a.score || b.matchedSkills.length - a.matchedSkills.length)
    .slice(0, 5);
}

function renderRecommendations(roles) {
  resultsNode.innerHTML = "";
  scoreNote.textContent = roles.length ? `Top ${roles.length} careers` : "No matches";

  if (!roles.length) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.textContent = "No matches found. Try skills such as Python, ML, Cloud, Docker, SQL, React, Linux, or Kubernetes.";
    resultsNode.appendChild(empty);
    return;
  }

  roles.forEach((role) => {
    const card = document.createElement("article");
    card.className = "item-card";

    const badge = document.createElement("div");
    badge.className = "score-badge";
    badge.textContent = `${role.score}%`;

    const content = document.createElement("div");
    const title = document.createElement("h3");
    title.textContent = role.title;

    const meta = document.createElement("p");
    meta.className = "meta";
    meta.textContent = `${role.domain} | ${role.level} | ${role.workStyle}`;

    const description = document.createElement("p");
    description.className = "description";
    description.textContent = role.description;

    const chips = document.createElement("div");
    chips.className = "chips";
    role.matchedSkills.forEach((skill) => {
      const chip = document.createElement("span");
      chip.className = "chip match";
      chip.textContent = skill;
      chips.appendChild(chip);
    });

    role.missingSkills.slice(0, 3).forEach((skill) => {
      const chip = document.createElement("span");
      chip.className = "chip";
      chip.textContent = `learn: ${skill}`;
      chips.appendChild(chip);
    });

    content.append(title, meta, description, chips);
    card.append(badge, content);
    resultsNode.appendChild(card);
  });
}

function updateResults(event) {
  if (event) {
    event.preventDefault();
  }
  renderRecommendations(recommend());
}

function resetForm() {
  fields.skills.value = "Python, ML, Cloud";
  fields.domain.value = "Any";
  fields.level.value = "Any";
  fields.workStyle.value = "Any";
  updateResults();
}

populateSelect(fields.domain, uniqueValues("domain"));
populateSelect(fields.level, uniqueValues("level"));
populateSelect(fields.workStyle, uniqueValues("workStyle"));
form.addEventListener("submit", updateResults);
resetButton.addEventListener("click", resetForm);
updateResults();
